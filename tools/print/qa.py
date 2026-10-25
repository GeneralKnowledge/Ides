"""Checks on the typeset interior and the imposed sheets.

Everything here reads the PDFs back (poppler's pdftotext/pdffonts and pypdf)
rather than trusting the typesetter: page sizes, embedded fonts, glyph
coverage, the extracted reading text against the manuscript, page furniture,
widows and orphans, short pages, hyphenation, and the imposition.
"""

from __future__ import annotations

import difflib
import html
import re
import struct
import subprocess
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

from pypdf import PdfReader

import impose

MM = 72 / 25.4


# ---- Geometry (must match book1.typ) ----------------------------------------

@dataclass(frozen=True)
class Geometry:
    trim_w: float = 129 * MM
    trim_h: float = 198 * MM
    inside: float = 19 * MM
    outside: float = 15 * MM
    top: float = 17.5 * MM
    size: float = 10.75
    lh: float = 13.5
    lines: int = 33

    @property
    def text_w(self) -> float:
        return self.trim_w - self.inside - self.outside

    @property
    def text_h(self) -> float:
        return self.lines * self.size + (self.lines - 1) * (self.lh - self.size)

    def left(self, page: int) -> float:
        return self.inside if page % 2 else self.outside


G = Geometry()


# ---- Reading pages back ------------------------------------------------------

@dataclass
class Line:
    x0: float
    y0: float
    x1: float
    y1: float
    text: str
    words: list[tuple[float, float, str]] = field(default_factory=list)


@dataclass
class Page:
    number: int
    lines: list[Line]
    head: list[Line] = field(default_factory=list)
    foot: list[Line] = field(default_factory=list)
    body: list[Line] = field(default_factory=list)


def read_pages(pdf: Path) -> list[Page]:
    out = subprocess.run(
        ["pdftotext", "-bbox-layout", str(pdf), "-"], check=True, capture_output=True, text=True
    ).stdout
    pages = []
    for n, pg in enumerate(re.findall(r"<page .*?</page>", out, re.S), 1):
        lines = []
        for lm in re.finditer(
            r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', pg, re.S
        ):
            words = [
                (float(a), float(b), html.unescape(t))
                for a, b, t in re.findall(
                    r'<word xMin="([\d.]+)" yMin="[\d.]+" xMax="([\d.]+)" yMax="[\d.]+">(.*?)</word>',
                    lm.group(5),
                )
            ]
            lines.append(Line(*(float(lm.group(i)) for i in range(1, 5)),
                              " ".join(w for _, _, w in words), words))
        p = Page(n, lines)
        for ln in lines:
            if ln.y1 < G.top:
                p.head.append(ln)
            elif ln.y0 > G.top + G.text_h:
                p.foot.append(ln)
            else:
                p.body.append(ln)
        pages.append(p)
    return pages


def rows(page: Page) -> list[str]:
    """Lines that share a baseline (e.g. a contents entry and its page number), joined."""
    out: list[tuple[float, list[Line]]] = []
    for ln in sorted(page.lines, key=lambda l: (round(l.y1), l.x0)):
        if out and abs(out[-1][0] - ln.y1) < 2:
            out[-1][1].append(ln)
        else:
            out.append((ln.y1, [ln]))
    return [" ".join(l.text for l in sorted(ls, key=lambda l: l.x0)) for _, ls in out]


def norm(s: str) -> str:
    return unicodedata.normalize("NFKC", s).replace("­", "")


# ---- File-level checks ----------------------------------------------------------

def check_sizes(pdf: Path, w: float, h: float, tol: float = 0.2) -> list[str]:
    bad = []
    for i, p in enumerate(PdfReader(str(pdf)).pages, 1):
        pw, ph = float(p.mediabox.width), float(p.mediabox.height)
        if abs(pw - w) > tol or abs(ph - h) > tol or (p.get("/Rotate") or 0):
            bad.append(f"page {i}: {pw / MM:.1f} x {ph / MM:.1f} mm, rotate {p.get('/Rotate') or 0}")
    return bad


def fonts(pdf: Path) -> list[dict]:
    out = subprocess.run(["pdffonts", str(pdf)], check=True, capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines()[2:]:
        parts = line.split()
        if len(parts) >= 7:
            # name type... emb sub uni object gen
            rows.append({"name": parts[0], "emb": parts[-5], "sub": parts[-4], "uni": parts[-3]})
    return rows


def font_cmap(path: Path) -> set[int]:
    """Code points in an OpenType font's cmap (formats 4 and 12)."""
    data = path.read_bytes()
    num = struct.unpack(">H", data[4:6])[0]
    tables = {data[12 + 16 * i: 16 + 16 * i].decode("latin-1"):
              struct.unpack(">II", data[20 + 16 * i: 28 + 16 * i]) for i in range(num)}
    off = tables["cmap"][0]
    n = struct.unpack(">H", data[off + 2: off + 4])[0]
    cps: set[int] = set()
    for i in range(n):
        _pid, _eid, sub = struct.unpack(">HHI", data[off + 4 + 8 * i: off + 12 + 8 * i])
        o = off + sub
        fmt = struct.unpack(">H", data[o: o + 2])[0]
        if fmt == 4:
            seg2 = struct.unpack(">H", data[o + 6: o + 8])[0]
            ends = struct.unpack(f">{seg2 // 2}H", data[o + 14: o + 14 + seg2])
            starts = struct.unpack(f">{seg2 // 2}H", data[o + 16 + seg2: o + 16 + 2 * seg2])
            for s, e in zip(starts, ends):
                if s != 0xFFFF:
                    cps.update(range(s, e + 1))
        elif fmt == 12:
            ngroups = struct.unpack(">I", data[o + 12: o + 16])[0]
            for g in range(ngroups):
                s, e, _ = struct.unpack(">III", data[o + 16 + 12 * g: o + 28 + 12 * g])
                cps.update(range(s, e + 1))
    return cps


def missing_glyphs(text: str, font_files: list[Path]) -> list[str]:
    have: set[int] = set()
    for f in font_files:
        have |= font_cmap(f)
    return sorted({c for c in text if not c.isspace() and ord(c) not in have})


# ---- Reading text against the manuscript ------------------------------------------

def extracted_words(pages: list[Page], first: int, vocab: set[str]) -> list[str]:
    """Words on the page bodies from `first` on, line-end hyphens resolved."""
    words: list[str] = []
    pending = None  # (word ending in hyphen)
    for p in pages[first - 1:]:
        for ln in p.body + [l for l in p.foot if not re.fullmatch(r"[0-9ivxlc]+", l.text)]:
            # A break at a discretionary hyphen can come back as a soft hyphen.
            text = ln.text[:-1] + "-" if ln.text.endswith("\u00ad") else ln.text
            toks = norm(text).split()
            if not toks:
                continue
            if pending is not None:
                # A break at a real hyphen keeps it; a break inside a word drops it.
                joined, kept = pending[:-1] + toks[0], pending + toks[0]
                toks[0] = joined if joined in vocab and kept not in vocab else kept
                pending = None
            if toks[-1].endswith(("-", "‐")) and len(toks[-1]) > 1:
                pending = toks.pop()
            words += toks
    if pending:
        words.append(pending)
    return words


def compare_words(expected: list[str], got: list[str]) -> list[str]:
    sm = difflib.SequenceMatcher(None, expected, got, autojunk=False)
    diffs = []
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op != "equal":
            ctx = " ".join(expected[max(0, a1 - 6): a1])
            diffs.append(
                f"{op}: manuscript «{' '.join(expected[a1:a2])[:120]}» vs PDF «{' '.join(got[b1:b2])[:120]}» after «…{ctx[-60:]}»"
            )
    return diffs


# ---- Page layout checks ----------------------------------------------------------

@dataclass
class LayoutReport:
    openings: list[int] = field(default_factory=list)
    blanks: list[int] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    widows: list[str] = field(default_factory=list)
    orphans: list[str] = field(default_factory=list)
    short_pages: list[str] = field(default_factory=list)
    long_pages: list[str] = field(default_factory=list)
    hyphen_lines: int = 0
    hyphen_ladders: list[str] = field(default_factory=list)
    loose_lines: list[str] = field(default_factory=list)
    body_lines: int = 0
    stub_endings: list[str] = field(default_factory=list)


def classify(ln: Line, page: int) -> str:
    left = G.left(page)
    right = left + G.text_w
    centre = left + G.text_w / 2
    if ln.x0 > left + 15 and abs((ln.x0 + ln.x1) / 2 - centre) < 4 and ln.x1 < right - 15:
        return "centred"
    indented = ln.x0 > left + 5
    full = ln.x1 > right - 6
    return ("indent" if indented else "flush") + ("-full" if full else "-short")


def find_main_start(pages: list[Page]) -> int:
    for p in pages:
        if p.body and p.body[0].text.startswith(("Prologue", "Chapter 1")) and not p.head:
            return p.number
    raise SystemExit("could not find the first page of the main text")


def opening_pages(pages: list[Page], main_start: int) -> set[int]:
    return {p.number for p in pages if p.number >= main_start and p.lines and not p.head}


def short_pages(pages: list[Page], main_start: int) -> dict[int, int]:
    """Pages whose text stops above the last grid line though the section goes on overleaf."""
    ops = opening_pages(pages, main_start)
    bottom_slot = G.top + G.text_h - G.lh
    out = {}
    for p in pages:
        if p.number < main_start or not p.body or p.number >= len(pages):
            continue
        nxt = pages[p.number]
        if nxt.body and nxt.number not in ops and p.body[-1].y0 < bottom_slot - G.lh / 2:
            out[p.number] = round((bottom_slot - p.body[-1].y0) / G.lh)
    return out


def layout(pages: list[Page], main_start: int, folio) -> LayoutReport:
    r = LayoutReport()
    for p in pages:
        if not p.lines:
            r.blanks.append(p.number)
            continue
        if not p.body and (p.head or p.foot):
            r.errors.append(f"page {p.number}: running head or folio on an otherwise empty page")
        if p.number < main_start:
            continue
        if not p.head:
            r.openings.append(p.number)
        if p.head and p.body and p.head[-1].y1 > p.body[0].y0 - 4:
            r.errors.append(f"page {p.number}: running head touches the text")
        if len(p.foot) > 1:
            r.errors.append(f"page {p.number}: more than one line below the text area")
        r.body_lines += len(p.body)

    pmap = {p.number: p for p in pages}
    short = short_pages(pages, main_start)

    def label(n: int) -> str:
        return f"p. {folio(n)} (PDF {n})"

    for p in pages:
        if p.number < main_start or not p.body or p.number in r.openings and not p.body:
            continue
        nxt = pmap.get(p.number + 1)
        kinds = [classify(l, p.number) for l in p.body]
        continues = nxt is not None and nxt.body and nxt.number not in r.openings
        if p.number in short:
            r.short_pages.append(f"{label(p.number)}: {short[p.number]} line(s) short")
        if p.body[-1].y1 > G.top + G.text_h + 1:
            r.long_pages.append(label(p.number))
        # A section whose last page holds very little.
        if not continues and p.number not in r.openings and len(p.body) <= 3:
            r.stub_endings.append(f"{label(p.number)}: {len(p.body)} line(s)")
        # Hyphenation and spacing.
        run = 0
        for i, (ln, k) in enumerate(zip(p.body, kinds)):
            if ln.text.endswith("-") and k.endswith("full"):
                r.hyphen_lines += 1
                run += 1
                if run == 3:
                    r.hyphen_ladders.append(f"{label(p.number)}: ending «{ln.text[-30:]}»")
            else:
                run = 0
            if k.endswith("full") and len(ln.words) > 3:
                gaps = [b[0] - a[1] for a, b in zip(ln.words, ln.words[1:])]
                mean = sum(gaps) / len(gaps)
                if mean > 0.5 * G.size:
                    r.loose_lines.append(f"{label(p.number)}: «{ln.text[:60]}» (word space {mean / G.size:.2f} em)")
    return r


def widows_orphans(marks: list[dict], pages: list[Page], folio) -> tuple[list[str], list[str]]:
    """From the paragraph position markers: a paragraph's last line alone at the
    top of a page (widow), or its first line alone at the foot (orphan)."""
    def line_no(y: float) -> int:  # markers sit on the baseline, 0.75 em below the line top
        return round((y - G.top - 0.75 * G.size) / G.lh)

    starts = {m["id"]: m for m in marks if not m["end"]}
    widows, orphans = [], []
    for e in marks:
        if not e["end"]:
            continue
        s = starts[e["id"]]
        if s["page"] == e["page"]:
            continue
        if line_no(e["y"]) == 0:
            widows.append(f"p. {folio(e['page'])} (PDF {e['page']}): «{pages[e['page'] - 1].body[0].text[:60]}»")
        if line_no(s["y"]) == G.lines - 1:
            orphans.append(f"p. {folio(s['page'])} (PDF {s['page']}): «{pages[s['page'] - 1].body[-1].text[:60]}»")
    return widows, orphans


# ---- Imposition checks -----------------------------------------------------------

def crop_text(pdf: Path, page: int, x: float, y: float, w: float, h: float) -> str:
    out = subprocess.run(
        ["pdftotext", "-f", str(page), "-l", str(page), "-x", str(int(x)), "-y", str(int(y)),
         "-W", str(int(w)), "-H", str(int(h)), str(pdf), "-"],
        check=True, capture_output=True, text=True,
    ).stdout
    return " ".join(norm(out).split())


def page_text(pdf: Path, page: int) -> str:
    out = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), str(pdf), "-"],
                         check=True, capture_output=True, text=True).stdout
    return " ".join(norm(out).split())


def check_signature(reading: Path, imposed: Path, sig: impose.Signature, total: int,
                    page_texts: dict[int, str]) -> list[str]:
    problems = []
    table = impose.sides(sig)
    # 1. The imposition formula agrees with an independent walk through the folded sheets.
    where = {}
    for i, (side, sheet, left, right) in enumerate(table):
        where[(sheet, side, "left")] = left
        where[(sheet, side, "right")] = right
    for idx, key in enumerate(impose.fold_order(sig)):
        if where[key] != sig.start + idx:
            problems.append(f"sig {sig.number}: fold walk expects page {sig.start + idx} at {key}, imposed {where[key]}")
    # 2. Versos on the left, rectos on the right.
    for side, sheet, left, right in table:
        if left % 2 or not right % 2:
            problems.append(f"sig {sig.number} sheet {sheet} {side}: verso/recto on the wrong half")
    # 3. Sheet size and orientation.
    for msg in check_sizes(imposed, impose.SHEET_W, impose.SHEET_H):
        problems.append(f"sig {sig.number}: {msg}")
    # 4. What is printed in each half is that reading page, at 100 %, spine to the fold.
    pw, ph = G.trim_w, G.trim_h
    for i, (side, sheet, left, right) in enumerate(table, 1):
        for half, p in (("left", left), ("right", right)):
            x, _ = impose.cell_origin(half, pw, ph)
            y = (impose.SHEET_H - ph) / 2  # from the top, same as from the bottom
            got = crop_text(imposed, i, x + 1, y + 1, pw - 2, ph - 2)
            want = page_texts.get(p, "") if p <= total else ""
            # Letterspaced small caps extract with arbitrary spaces; compare the characters.
            if "".join(got.split()) != "".join(want.split()):
                problems.append(
                    f"sig {sig.number} sheet {sheet} {side} {half}: expected PDF page {p} "
                    f"«{want[:50]}», found «{got[:50]}»"
                )
    return problems


# ---- Possible source problems (reported, never fixed) -----------------------------

SOURCE_PATTERNS = [
    ("doubled word", re.compile(r"\b(\w+)\s+\1\b", re.I)),
    ("double space", re.compile(r"\S  +\S")),
    ("space before punctuation", re.compile(r"\s[,.;:!?](?!\.\.)")),
    ("straight quote", re.compile(r"[\"']")),
    ("hyphen used as dash", re.compile(r"\s-\s|--")),
    ("unmatched asterisk", re.compile(r"\*")),
]

ALLOWED_DOUBLES = {"had had", "that that"}


def source_concerns(data: dict) -> list[str]:
    from content import plain

    out = []
    for sec in data["sections"]:
        where = sec.get("label", sec["title"])
        for b in sec["blocks"]:
            t = plain(b["runs"])
            for name, rx in SOURCE_PATTERNS:
                for m in rx.finditer(t):
                    if name == "doubled word" and m.group(0).lower() in ALLOWED_DOUBLES:
                        continue
                    s = max(0, m.start() - 40)
                    out.append(f"{where}: {name}: «…{t[s:m.end() + 30]}…»")
            if t.count("“") != t.count("”"):
                # Multi-paragraph speech legitimately leaves a quote open.
                opened = t.count("“") > t.count("”")
                out.append(
                    f"{where}: quotes unbalanced in paragraph ({t.count('“')} open, {t.count('”')} close"
                    f"{'; may be speech running on into the next paragraph' if opened else ''}): «{t[:70]}…»"
                )
    return out

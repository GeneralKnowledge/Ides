#!/usr/bin/env python3
"""Export Book 1 chapter drafts to reading DOCX (metadata stripped).

    python tools/export_book1_docx.py           # write exports/
    python tools/export_book1_docx.py --check   # verify the tracked full copy

The full copy is stamped with the manuscript commit (last commit touching
drafts/book1), its date, the generation date and a digest of the chapter
sources. --check rebuilds the reading text from the working tree and fails
unless the DOCX matches it paragraph for paragraph. See
writing/FINAL_READINESS_GATE.md.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
DRAFTS = ROOT / "drafts" / "book1"
EXPORTS = ROOT / "exports"
FULL_PATH = EXPORTS / "Ides_Book1_FULL_Ch01-36.docx"
CHAPTER_COUNT = 36
# Optional prologue before Chapter 1, header "# Prologue: Title"; parsed as number 0.
# Inserted chapters (ch36a_*.md, "# Chapter 36a: Title") sit after their base
# chapter until the next renumbering pass; at most one letter per insert.
# The 2026-10-24 pass folded 25a and 27a into Ch 26 and Ch 29.
PROLOGUE = DRAFTS / "prologue_utica.md"
# Back matter in the full copy, after the last chapter. map_brief.md is for the cartographer.
BACK_MATTER = [DRAFTS / "back_matter" / "historical_note.md", DRAFTS / "back_matter" / "cast_list.md"]

ACTS = [
    (1, "Act 1: Foundations"),
    (7, "Act 2: Conspiracy"),
    (14, "Act 3: The Ides"),
    (21, "Act 4: Aftermath & Name-War"),
    (30, "Act 5: Mutina to Philippi"),
]

# Chapter / scene title separators after author-voice em-dash purge (colon),
# plus legacy dash forms if any remain in older notes.
# Allow optional spaces: "Chapter 1: Title" and "Chapter 1 — Title".
_TITLE_SEP = r"\s*[:—–-]\s*"

META_PREFIXES = (
    "POV:",
    "Date / place:",
    "Canon refs:",
    "Info ENTER:",
    "Info EXIT:",
    "Overhear risk:",
    "Canon:",
    "Soft date:",
    "Dates:",
    "Place:",
    "Continues:",
    "Set-piece:",
    "Note:",
    "Chronology:",
)

# Trailing lock tags on scene titles, e.g. "Wax Against the Ribs (NOTE-1)".
TITLE_TAG = re.compile(r"\s*\((?:[A-Z]+-\d+\w*[,/ ]*)+\)$")

# Bold-labelled craft lines: **G1:** …, **Opening prose pass:** …, whole-line **tags**
CRAFT_BOLD_LINE = re.compile(r"^\*\*")


# Inline *italic* (the manuscript uses single asterisks only).
ITALIC = re.compile(r"\*([^*\n]+?)\*")

# Anything that should never reach a reader: markup, scene ids, card fields,
# canon/lock tags, editor notes.
LEAK = re.compile(
    r"\*|^#|^//|TODO|\bSC-\d|\bPOV:|Canon refs|Info (?:ENTER|EXIT)|"
    r"Overhear risk|Continuity notes|End matter|\b(?:AMB|NOTE|SIDE|EXIT|CLEO|"
    r"OMEN|HOUSE|VOICE|TONE|HUMOR|CHOREO|SERIES|NAMES|PERS)-\d|\bFS\d\d|"
    r"\bFT\d|\bG[12]:|\bA\d{1,2}\b(?! ?BC)|\ufffd"
)


def git(*args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", *args], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return ""


def source_digest(files: list[Path]) -> str:
    """SHA-256 over chapter file names and bytes, in chapter order."""
    h = hashlib.sha256()
    for p in files:
        h.update(p.name.encode() + b"\0" + p.read_bytes() + b"\0")
    return h.hexdigest()[:16]


def source_stamp(files: list[Path]) -> dict[str, str]:
    dirty = bool(git("status", "--porcelain", "--", "drafts/book1"))
    return {
        "manuscript": git("log", "-1", "--format=%h", "--", "drafts/book1") or "unknown",
        "manuscript_date": git("log", "-1", "--format=%cs", "--", "drafts/book1") or "unknown",
        "head": git("rev-parse", "--short", "HEAD") or "unknown",
        "branch": git("branch", "--show-current") or "detached",
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "digest": source_digest(files),
        "dirty": "yes" if dirty else "no",
    }


class ChapNum(int):
    """Chapter number with an optional insert letter: 36a sorts after 36."""

    def __new__(cls, n: int, suffix: str = "") -> "ChapNum":
        obj = super().__new__(cls, n)
        obj.suffix = suffix
        return obj

    def key(self) -> tuple[int, str]:
        return (int(self), self.suffix)

    def __eq__(self, other: object) -> bool:
        return self.key() == (other.key() if isinstance(other, ChapNum) else (other, ""))

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self.key()) if self.suffix else int.__hash__(self)

    def __str__(self) -> str:
        return f"{int(self)}{self.suffix}"

    __format__ = lambda self, spec: format(str(self), spec)


def chapter_files() -> list[tuple[ChapNum, Path]]:
    """Chapter files sorted by chapter number, inserts after their base."""
    out = []
    for p in DRAFTS.glob("ch*.md"):
        m = re.match(r"ch(\d+)([a-z]?)_", p.name)
        if m:
            out.append((ChapNum(int(m.group(1)), m.group(2)), p))
    return sorted(out, key=lambda t: t[0].key())


def expected_heads(nums: list[ChapNum]) -> list[str]:
    """Chapter headings in reading order: 1..CHAPTER_COUNT plus any inserts."""
    return [str(n) for n in nums]


def parse_chapter(path: Path) -> tuple[int, str, list[tuple[str, str]]]:
    """Return (num, title, blocks) where blocks are ('scene'|'body', text)."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    m = re.match(
        rf"#\s+Chapter\s+(\d+)([a-z]?){_TITLE_SEP}(.+)", lines[0].strip()
    )
    pm = re.match(rf"#\s+Prologue{_TITLE_SEP}(.+)", lines[0].strip())
    if m:
        num, title = ChapNum(int(m.group(1)), m.group(2)), m.group(3).strip()
    elif pm:
        num, title = 0, pm.group(1).strip()
    else:
        raise ValueError(f"Bad chapter header in {path}")

    blocks: list[tuple[str, str]] = []
    i = 1
    skip_continuity = False
    in_end_matter = False

    while i < len(lines):
        raw = lines[i]
        line = raw.strip()
        i += 1

        if in_end_matter:
            continue

        if re.match(rf"#\s+Chapter\s+\d+{_TITLE_SEP}End matter", line):
            in_end_matter = True
            continue

        if line.startswith("## Continuity"):
            skip_continuity = True
            continue

        if skip_continuity:
            # Resume at next scene or chapter end-matter
            if line.startswith("# SC-") or line.startswith("### Beat") or re.match(
                rf"#\s+Chapter\s+\d+{_TITLE_SEP}End matter", line
            ):
                skip_continuity = False
                # fall through to handle this line
            else:
                continue

        if not line or line == "---":
            continue

        # All leading-** lines in this manuscript are craft/header metadata, not fiction.
        if CRAFT_BOLD_LINE.match(line):
            continue
        if any(line.startswith(p) for p in META_PREFIXES):
            continue
        if line.startswith("//"):
            continue
        # Continuity bullets that escaped a ## Continuity block
        if line.startswith("- **") or line.startswith("* **"):
            continue

        sc = re.match(rf"#\s+SC-\S+{_TITLE_SEP}(.+)", line)
        if sc:
            blocks.append(("scene", TITLE_TAG.sub("", sc.group(1).strip())))
            continue

        beat = re.match(rf"###\s+(Beat{_TITLE_SEP}.+)", line)
        if beat:
            blocks.append(("scene", beat.group(1).strip()))
            continue

        if line.startswith("#"):
            # Other headings (rare): treat as scene title without hashes
            blocks.append(("scene", re.sub(r"^#+\s*", "", line)))
            continue

        blocks.append(("body", line))

    return num, title, blocks


Runs = list[tuple[str, bool]]  # (text, italic)

# Book layout: 6 x 9 in trim, Georgia, indented justified prose, each act and
# chapter on a fresh page. Paragraph text is what --check compares; layout is not.
FONT = "Georgia"
INK = RGBColor(0x22, 0x22, 0x22)


def setup_document(doc: Document) -> None:
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(6), Inches(9)
    sec.top_margin = sec.bottom_margin = Inches(0.8)
    sec.left_margin = sec.right_margin = Inches(0.75)

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = INK
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    pf = normal.paragraph_format
    pf.space_before = pf.space_after = Pt(0)
    pf.line_spacing = 1.2
    pf.widow_control = True

    # Headings keep Word's navigation pane useful: acts and back matter at
    # level 1, chapter titles at level 2.
    for name, size in (("Heading 1", 16), ("Heading 2", 15), ("Heading 3", 12)):
        st = doc.styles[name]
        st.font.name, st.font.size, st.font.bold = FONT, Pt(size), False
        st.font.color.rgb = INK
        for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
            st.element.rPr.rFonts.attrib.pop(qn(attr), None)
        st.paragraph_format.space_before = st.paragraph_format.space_after = Pt(0)
        st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        st.paragraph_format.keep_with_next = True

    # Let Word hyphenate so justified lines don't gape.
    hyph = OxmlElement("w:autoHyphenation")
    hyph.set(qn("w:val"), "true")
    doc.settings.element.append(hyph)


def to_runs(text: str) -> Runs:
    runs: Runs = []
    pos = 0
    for m in ITALIC.finditer(text):
        if m.start() > pos:
            runs.append((text[pos : m.start()], False))
        runs.append((m.group(1), True))
        pos = m.end()
    if pos < len(text):
        runs.append((text[pos:], False))
    return runs


def add_para(doc: Document, text: str, *, style: str | None = None, small_caps_words: int = 0):
    """Paragraph from markdown text; optionally set the opening words in small caps."""
    p = doc.add_paragraph(style=style)
    for i, (chunk, italic) in enumerate(to_runs(text)):
        if i == 0 and small_caps_words and not italic:
            words = chunk.split(" ")
            lead = " ".join(words[:small_caps_words])
            rest = chunk[len(lead):]
            p.add_run(lead).font.small_caps = True
            if rest:
                p.add_run(rest)
            continue
        p.add_run(chunk).italic = italic or None
    return p


def page_number_footer(section) -> None:
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.font.size = Pt(9)
    for tag, text in (("begin", None), (None, "PAGE"), ("end", None)):
        if tag:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), tag)
        else:
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = text
        run._r.append(el)
    num = OxmlElement("w:pgNumType")
    num.set(qn("w:start"), "1")
    section._sectPr.append(num)


def front_line(doc: Document, text: str, *, size: float = 10.5, before: float = 0,
               after: float = 0, italic: bool = False, caps: bool = False, spacing: int = 0):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before, p.paragraph_format.space_after = Pt(before), Pt(after)
    run = p.add_run(text)
    run.font.size, run.italic, run.font.all_caps = Pt(size), italic or None, caps or None
    if spacing:
        sp = OxmlElement("w:spacing")
        sp.set(qn("w:val"), str(spacing))
        run._r.get_or_add_rPr().append(sp)
    return p


def page_break(doc: Document) -> None:
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def parse_back_matter(path: Path) -> list[tuple[str, str]]:
    """A back-matter page as (text, role): headings, bullets, prose; bold dropped."""
    out: list[tuple[str, str]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip().replace("**", "")
        if not line:
            continue
        if line.startswith("# "):
            out.append((line[2:].strip(), "back_head"))
        elif line.startswith("## "):
            out.append((line[3:].strip(), "back_sub"))
        elif line.startswith("- "):
            out.append(("• " + line[2:].strip(), "back_item"))
        else:
            out.append((line, "body"))
    return out


def reading_paragraphs(
    chapters: list[tuple[int, str, list[tuple[str, str]]]],
    end_line: str,
    back: list[tuple[str, str]] = [],
) -> list[tuple[str, str]]:
    """Everything after the front matter, as (markdown text, role)."""
    out: list[tuple[str, str]] = []
    act_by_start = {n: label for n, label in ACTS}
    for num, title, blocks in chapters:
        if num in act_by_start:
            out.append((act_by_start[num], "act"))
        out.append(("Prologue" if num == 0 else f"Chapter {num}", "chapter"))
        out.append((title, "title"))
        out.extend((text, kind) for kind, text in blocks)
    out.extend(back)
    out.append((end_line, "end"))
    return out


def render_reading(doc: Document, paras: list[tuple[str, str]]) -> None:
    prev = "start"
    for text, role in paras:
        fresh_page = prev != "start" and role in ("act", "chapter", "back_head")
        if role == "act":
            p = add_para(doc, text, style="Heading 1")
            p.paragraph_format.space_before = Pt(170)
        elif role == "chapter":
            p = add_para(doc, text)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(90)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            for r in p.runs:
                r.font.all_caps, r.font.size = True, Pt(9.5)
                letter = OxmlElement("w:spacing")
                letter.set(qn("w:val"), "40")
                r._r.get_or_add_rPr().append(letter)
        elif role == "title":
            p = add_para(doc, text, style="Heading 2")
            p.paragraph_format.space_after = Pt(42)
        elif role == "scene":
            p = add_para(doc, text)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0 if prev == "title" else 22)
            p.paragraph_format.space_after = Pt(10)
            p.paragraph_format.keep_with_next = True
            for r in p.runs:  # italics are reading text, so mark scenes with small caps
                r.font.small_caps, r.font.size = True, Pt(10)
        elif role == "back_head":
            p = add_para(doc, text, style="Heading 1")
            p.paragraph_format.space_before = Pt(60)
            p.paragraph_format.space_after = Pt(24)
        elif role == "back_sub":
            p = add_para(doc, text, style="Heading 3")
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
        elif role == "back_item":
            p = add_para(doc, text)
            p.paragraph_format.left_indent = Inches(0.2)
            p.paragraph_format.first_line_indent = Inches(-0.2)
            p.paragraph_format.space_after = Pt(2)
        elif role == "end":
            p = add_para(doc, text)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(36)
            for r in p.runs:
                r.font.small_caps, r.font.size = True, Pt(9)
        else:  # body prose: first paragraph of a run flush, opening words in small caps
            opening = prev in ("title", "scene", "back_head", "back_sub", "back_item")
            p = add_para(doc, text, small_caps_words=3 if prev == "title" else 0)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            if not opening:
                p.paragraph_format.first_line_indent = Inches(0.25)
        if fresh_page:
            p.paragraph_format.page_break_before = True
        prev = role


def build_doc(
    chapters: list[tuple[int, str, list[tuple[str, str]]]],
    *,
    subtitle: str,
    banner: str,
    blurb: str,
    source_note: str,
    end_line: str,
    stamp: dict[str, str],
    back: list[tuple[str, str]] = [],
) -> Document:
    doc = Document()
    setup_document(doc)
    paras = reading_paragraphs(chapters, end_line, back)

    # Title page
    front_line(doc, "The Ides of March", size=26, before=150, caps=True, spacing=30)
    front_line(doc, "Book 1", size=13, before=18, italic=True)
    front_line(doc, "Reuben Dennison", size=11, before=150, caps=True, spacing=20)
    page_break(doc)

    # About this copy
    front_line(doc, subtitle, size=11, before=40, after=14)
    for line in (banner, *blurb.split("\n"), source_note,
                 "Not a publication text. Continuity notes and canon tags omitted."):
        front_line(doc, line, size=8.5, after=8, italic=True)
    page_break(doc)

    # Contents (entries never equal a reading paragraph, so --check can find the start)
    front_line(doc, "Contents", size=13, before=20, after=18, caps=True, spacing=30)
    for i, (text, role) in enumerate(paras):
        if role == "act":
            front_line(doc, text, size=9, before=10, after=3, caps=True, spacing=15)
        elif role == "chapter":
            title = re.sub(r"\*", "", paras[i + 1][0])
            label = "Prologue: " if text == "Prologue" else text.replace("Chapter ", "") + ".  "
            front_line(doc, label + title, size=9.5)
        elif role == "back_head":
            front_line(doc, text, size=9.5, before=8)

    body = doc.add_section(WD_SECTION.NEW_PAGE)
    doc.sections[0].footer.is_linked_to_previous = True
    page_number_footer(body)
    render_reading(doc, paras)

    cp = doc.core_properties
    cp.title = "The Ides of March: " + subtitle
    cp.author = "Reuben Dennison"
    cp.last_modified_by = "tools/export_book1_docx.py"
    cp.version = stamp["manuscript"]
    cp.identifier = stamp["digest"]
    cp.comments = stamp_line(stamp)
    cp.created = cp.modified = datetime.now(timezone.utc).replace(tzinfo=None)
    return doc


def stamp_line(stamp: dict[str, str]) -> str:
    line = (
        f"Manuscript {stamp['manuscript']} ({stamp['manuscript_date']}) · "
        f"generated {stamp['generated']} from {stamp['branch']} @ {stamp['head']} · "
        f"source digest {stamp['digest']}"
    )
    if stamp["dirty"] == "yes":
        line += " · UNCOMMITTED MANUSCRIPT CHANGES"
    return line


def assert_reading_clean(chapters: list[tuple[int, str, list[tuple[str, str]]]]) -> None:
    """Fail loud if craft tags leak into reading body text."""
    bad = re.compile(
        r"^\*\*|\bG[12]:\b|MUST_EXPRESS|Law-sweep|Anti-formula|Opening prose pass|"
        r"Dinner-first|Mid-tier pass|M5 polish|Phase 1[A-G]|Final integrated|"
        r"Act5 ordeal|S-A\d|Gold dwell|Expansion D\d",
        re.I,
    )
    # Planning codes used as scene headings: "F2: Seius", "Movement A: Antony", "(False)"
    bad_heading = re.compile(r"^F\d:|^Movement [A-Z]\b|\((?:True|False)\)")
    leaks: list[str] = []
    for num, _title, blocks in chapters:
        for kind, text in blocks:
            if bad.search(text) or (kind == "scene" and bad_heading.search(text)):
                leaks.append(f"ch{num}: {text[:100]}")
    if leaks:
        raise SystemExit("Craft metadata leaked into export body:\n  " + "\n  ".join(leaks[:20]))


def full_back() -> list[tuple[str, str]]:
    return [b for path in BACK_MATTER if path.exists() for b in parse_back_matter(path)]


def load_chapters() -> tuple[list[Path], list[tuple[int, str, list[tuple[str, str]]]]]:
    files = chapter_files()
    nums = [n for n, _ in files]
    base = [int(n) for n in nums if not n.suffix]
    if base != list(range(1, CHAPTER_COUNT + 1)) or len(set(nums)) != len(nums):
        raise SystemExit(
            f"Expected chapter files 1–{CHAPTER_COUNT} once each, got {[str(n) for n in nums]}"
        )
    chapters = [parse_chapter(p) for _, p in files]
    for (n, p), (num, _, _) in zip(files, chapters):
        if n != num:
            raise SystemExit(f"{p.name}: filename says Ch {n}, header says Ch {num}")
        if num.suffix and ChapNum(int(num)) not in nums:
            raise SystemExit(f"{p.name}: insert Ch {num} has no base Ch {int(num)}")
    if PROLOGUE.exists():
        pro = parse_chapter(PROLOGUE)
        if pro[0] != 0:
            raise SystemExit(f"{PROLOGUE.name}: header must be '# Prologue: Title'")
        files.insert(0, (0, PROLOGUE))
        chapters.insert(0, pro)
    assert_reading_clean(chapters)
    # The digest covers the back matter too, so editing it marks the copy stale.
    return [p for _, p in files] + [p for p in BACK_MATTER if p.exists()], chapters


def docx_paragraphs(path: Path) -> list[Runs]:
    """Paragraphs as runs, adjacent runs with the same italic state merged."""
    out: list[Runs] = []
    for para in Document(str(path)).paragraphs:
        runs: Runs = []
        for r in para.runs:
            if not r.text:
                continue
            it = bool(r.italic)
            if runs and runs[-1][1] == it:
                runs[-1] = (runs[-1][0] + r.text, it)
            else:
                runs.append((r.text, it))
        out.append(runs)
    return out


def plain(runs: Runs) -> str:
    return "".join(t for t, _ in runs)


def check(path: Path) -> int:
    """Integrity check of a full export against the working-tree manuscript."""
    files, chapters = load_chapters()
    problems: list[str] = []
    if not path.exists():
        print(f"FAIL: {path} missing")
        return 1

    cp = Document(str(path)).core_properties
    digest = source_digest(files)
    if cp.identifier != digest:
        problems.append(
            f"stale: export digest {cp.identifier or 'none'} != manuscript digest {digest} "
            "(regenerate with tools/export_book1_docx.py)"
        )
    if "UNCOMMITTED" in (cp.comments or ""):
        problems.append("export was generated from uncommitted manuscript changes")

    expected = [to_runs(t) for t, _ in reading_paragraphs(chapters, FULL_END_LINE, full_back())]
    got = docx_paragraphs(path)
    lead = [plain(r) for r in expected[:3]]
    start = next((i for i in range(len(got)) if [plain(r) for r in got[i : i + 3]] == lead), 0)
    front, body = got[:start], got[start:]

    if not any(digest in plain(r) for r in front):
        problems.append("title page does not carry the source digest")

    # Chapters appear once each, in order.
    heads = [m.group(1) for r in got if (m := re.fullmatch(r"Chapter (\d+[a-z]?)", plain(r)))]
    if heads != expected_heads([c[0] for c in chapters if c[0] != 0]):
        problems.append(f"chapter headings out of order or repeated: {heads}")

    # Nothing omitted or duplicated (multiset), then exact sequence and italics.
    want = Counter(plain(r) for r in expected)
    have = Counter(plain(r) for r in body)
    for text, n in (want - have).items():
        problems.append(f"omitted x{n}: {text[:90]}")
    for text, n in (have - want).items():
        problems.append(f"extra/duplicated x{n}: {text[:90]}")
    if len(body) != len(expected):
        problems.append(f"paragraph count {len(body)} != expected {len(expected)}")
    for i, (e, g) in enumerate(zip(expected, body)):
        if e != g:
            kind = "italics differ" if plain(e) == plain(g) else "text differs"
            problems.append(f"first mismatch at reading paragraph {i} ({kind}): {plain(g)[:90]}")
            break

    # No metadata or markup anywhere in the reading text.
    for r in body:
        t = plain(r)
        if LEAK.search(t):
            problems.append(f"metadata/markup leak: {t[:90]}")

    if problems:
        print(f"FAIL: {path.name}")
        for p in problems[:40]:
            print("  " + p)
        return 1
    extra = [str(c[0]) for c in chapters if getattr(c[0], "suffix", "")]
    inserts = f" (+ inserts {', '.join(extra)})" if extra else ""
    print(
        f"OK: {path.name} · {CHAPTER_COUNT} chapters once{inserts}, in order · "
        f"{len(body)} reading paragraphs match the manuscript · no leaks\n"
        f"    {cp.comments}"
    )
    return 0


FULL_END_LINE = "End of Book 1 full review export"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="verify the tracked full export")
    ap.add_argument(
        "--allow-dirty",
        action="store_true",
        help="export even with uncommitted manuscript changes (stamped as such)",
    )
    args = ap.parse_args()
    if args.check:
        sys.exit(check(FULL_PATH))

    EXPORTS.mkdir(exist_ok=True)
    files, all_ch = load_chapters()
    stamp = source_stamp(files)
    if stamp["dirty"] == "yes" and not args.allow_dirty:
        raise SystemExit(
            "drafts/book1 has uncommitted changes; commit first so the export "
            "traces to a revision (or pass --allow-dirty for a scratch copy)"
        )

    label = (
        "Book 1 reading export · Utica prologue, then Ch 1 dinner · ends at Philippi · "
        "author-voice (no em dash)"
    )
    source = stamp_line(stamp)

    full = build_doc(
        all_ch,
        subtitle="Book 1: FULL Review Draft (Chapters 1–36)",
        banner="THIS FILE CONTAINS THE PROLOGUE AND ALL 36 CHAPTERS · OPENS WITH THE PROLOGUE",
        blurb="Prose export for reading · metadata stripped\n" + label,
        source_note=f"Source: {source} · prologue, chapters 1–36, historical note and cast",
        end_line=FULL_END_LINE,
        stamp=stamp,
        back=full_back(),
    )
    full.save(FULL_PATH)
    # Alias used by earlier review packets
    full.save(EXPORTS / "Ides_Book1_Review.docx")

    golden_ch = [c for c in all_ch if 14 <= c[0] <= 19]
    golden = build_doc(
        golden_ch,
        subtitle="Book 1: Golden Sample ONLY (Chapters 14–19)",
        banner="SAMPLE ONLY · STARTS AT CHAPTER 14 · NOT THE FULL BOOK",
        blurb="Stand-alone sample · Ides through funeral\n" + label,
        source_note=f"Source: {source} · chapters 14–19 only",
        end_line="End of golden chapters sample",
        stamp=stamp,
    )
    golden_path = EXPORTS / "Ides_Book1_Golden_Chapters.docx"
    golden.save(golden_path)
    golden.save(EXPORTS / "Ides_Book1_Golden_ONLY_Ch14-19.docx")

    print(f"Wrote {FULL_PATH}")
    print(f"Wrote {golden_path}")
    print(source)
    sys.exit(check(FULL_PATH))


if __name__ == "__main__":
    main()

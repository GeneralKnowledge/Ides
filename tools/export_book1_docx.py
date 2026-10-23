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
from docx.shared import Pt
from docx.enum.text import WD_LINE_SPACING

ROOT = Path(__file__).resolve().parents[1]
DRAFTS = ROOT / "drafts" / "book1"
EXPORTS = ROOT / "exports"
FULL_PATH = EXPORTS / "Ides_Book1_FULL_Ch01-34.docx"
CHAPTER_COUNT = 34
# Optional prologue before Chapter 1, header "# Prologue: Title"; parsed as number 0.
PROLOGUE = DRAFTS / "prologue_utica.md"

ACTS = [
    (1, "Act 1: Foundations"),
    (7, "Act 2: Conspiracy"),
    (14, "Act 3: The Ides"),
    (21, "Act 4: Aftermath & Name-War"),
    (28, "Act 5: Mutina to Philippi"),
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


def chapter_files() -> list[tuple[int, Path]]:
    """Chapter files sorted by chapter number."""
    out = []
    for p in sorted(DRAFTS.glob("ch*.md")):
        m = re.match(r"ch(\d+)_", p.name)
        if m:
            out.append((int(m.group(1)), p))
    return sorted(out)


def parse_chapter(path: Path) -> tuple[int, str, list[tuple[str, str]]]:
    """Return (num, title, blocks) where blocks are ('scene'|'body', text)."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    m = re.match(
        rf"#\s+Chapter\s+(\d+){_TITLE_SEP}(.+)", lines[0].strip()
    )
    pm = re.match(rf"#\s+Prologue{_TITLE_SEP}(.+)", lines[0].strip())
    if m:
        num, title = int(m.group(1)), m.group(2).strip()
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


def set_normal_style(doc: Document) -> None:
    style = doc.styles["Normal"]
    style.font.name = "Georgia"
    style.font.size = Pt(11)
    pf = style.paragraph_format
    pf.space_after = Pt(8)
    pf.line_spacing_rule = WD_LINE_SPACING.SINGLE


Runs = list[tuple[str, bool]]  # (text, italic)


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


def add_para(doc: Document, text: str, *, space_before: int = 0) -> None:
    p = doc.add_paragraph()
    for chunk, italic in to_runs(text):
        p.add_run(chunk).italic = italic or None
    if space_before:
        p.paragraph_format.space_before = Pt(space_before)


def reading_paragraphs(
    chapters: list[tuple[int, str, list[tuple[str, str]]]], end_line: str
) -> list[tuple[str, int]]:
    """Everything after the title page, as (markdown text, space_before)."""
    out: list[tuple[str, int]] = []
    act_by_start = {n: label for n, label in ACTS}
    for num, title, blocks in chapters:
        if num in act_by_start:
            out.append((act_by_start[num], 18))
        out.append(("Prologue" if num == 0 else f"Chapter {num}", 14))
        out.append((title, 0))
        for kind, text in blocks:
            out.append((text, 10 if kind == "scene" else 0))
    out.append((end_line, 18))
    return out


def build_doc(
    chapters: list[tuple[int, str, list[tuple[str, str]]]],
    *,
    subtitle: str,
    banner: str,
    blurb: str,
    source_note: str,
    end_line: str,
    stamp: dict[str, str],
) -> Document:
    doc = Document()
    set_normal_style(doc)

    add_para(doc, "The Ides of March")
    add_para(doc, subtitle)
    add_para(doc, banner)
    add_para(doc, blurb + "\n" + source_note)
    add_para(
        doc,
        "Not a publication text. Continuity notes and canon tags omitted.",
    )
    doc.add_paragraph("")

    for text, space_before in reading_paragraphs(chapters, end_line):
        add_para(doc, text, space_before=space_before)

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
    leaks: list[str] = []
    for num, _title, blocks in chapters:
        for kind, text in blocks:
            if bad.search(text):
                leaks.append(f"ch{num}: {text[:100]}")
    if leaks:
        raise SystemExit("Craft metadata leaked into export body:\n  " + "\n  ".join(leaks[:20]))


def load_chapters() -> tuple[list[Path], list[tuple[int, str, list[tuple[str, str]]]]]:
    files = chapter_files()
    nums = [n for n, _ in files]
    if nums != list(range(1, CHAPTER_COUNT + 1)):
        raise SystemExit(f"Expected chapter files 1–{CHAPTER_COUNT} once each, got {nums}")
    chapters = [parse_chapter(p) for _, p in files]
    for (n, p), (num, _, _) in zip(files, chapters):
        if n != num:
            raise SystemExit(f"{p.name}: filename says Ch {n}, header says Ch {num}")
    if PROLOGUE.exists():
        pro = parse_chapter(PROLOGUE)
        if pro[0] != 0:
            raise SystemExit(f"{PROLOGUE.name}: header must be '# Prologue: Title'")
        files.insert(0, (0, PROLOGUE))
        chapters.insert(0, pro)
    assert_reading_clean(chapters)
    return [p for _, p in files], chapters


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

    expected = [to_runs(t) for t, _ in reading_paragraphs(chapters, FULL_END_LINE)]
    got = docx_paragraphs(path)
    first = plain(expected[0])
    start = next((i for i, r in enumerate(got) if plain(r) == first), 0)
    front, body = got[:start], got[start:]

    if not any(digest in plain(r) for r in front):
        problems.append("title page does not carry the source digest")

    # Chapters appear once each, in order.
    heads = [int(m.group(1)) for r in got if (m := re.fullmatch(r"Chapter (\d+)", plain(r)))]
    if heads != list(range(1, CHAPTER_COUNT + 1)):
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
    print(
        f"OK: {path.name} · {CHAPTER_COUNT} chapters once, in order · "
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
        subtitle="Book 1: FULL Review Draft (Chapters 1–34)",
        banner="THIS FILE CONTAINS THE PROLOGUE AND ALL 34 CHAPTERS · OPENS WITH THE PROLOGUE",
        blurb="Prose export for reading · metadata stripped\n" + label,
        source_note=f"Source: {source} · prologue and chapters 1–34",
        end_line=FULL_END_LINE,
        stamp=stamp,
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

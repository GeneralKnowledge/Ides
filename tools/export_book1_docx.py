#!/usr/bin/env python3
"""Export Book 1 chapter drafts to reading DOCX (metadata stripped)."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_LINE_SPACING

ROOT = Path(__file__).resolve().parents[1]
DRAFTS = ROOT / "drafts" / "book1"
EXPORTS = ROOT / "exports"

ACTS = [
    (1, "Act 1 — Foundations"),
    (7, "Act 2 — Conspiracy"),
    (14, "Act 3 — The Ides"),
    (21, "Act 4 — Aftermath & Name-War"),
    (28, "Act 5 — Mutina to Philippi"),
]

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
)


def git_short() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except Exception:
        return "unknown"


def chapter_files() -> list[tuple[int, Path]]:
    out = []
    for p in sorted(DRAFTS.glob("ch*.md")):
        m = re.match(r"ch(\d+)_", p.name)
        if m:
            out.append((int(m.group(1)), p))
    return out


def parse_chapter(path: Path) -> tuple[int, str, list[tuple[str, str]]]:
    """Return (num, title, blocks) where blocks are ('scene'|'body', text)."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    m = re.match(r"#\s+Chapter\s+(\d+)\s+[—-]\s+(.+)", lines[0].strip())
    if not m:
        raise ValueError(f"Bad chapter header in {path}")
    num, title = int(m.group(1)), m.group(2).strip()

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

        if re.match(r"#\s+Chapter\s+\d+\s+[—-]\s+End matter", line):
            in_end_matter = True
            continue

        if line.startswith("## Continuity"):
            skip_continuity = True
            continue

        if skip_continuity:
            # Resume at next scene or chapter end-matter
            if line.startswith("# SC-") or line.startswith("### Beat") or re.match(
                r"#\s+Chapter\s+\d+\s+[—-]\s+End matter", line
            ):
                skip_continuity = False
                # fall through to handle this line
            else:
                continue

        if not line or line == "---":
            continue

        if line.startswith("**") and line.endswith("**"):
            continue
        if line.startswith("**") and "·" in line:
            continue
        if any(line.startswith(p) for p in META_PREFIXES):
            continue
        if line.startswith("//"):
            continue

        sc = re.match(r"#\s+SC-\S+\s+[—-]\s+(.+)", line)
        if sc:
            blocks.append(("scene", sc.group(1).strip()))
            continue

        beat = re.match(r"###\s+(Beat\s+[—-].+)", line)
        if beat:
            blocks.append(("scene", beat.group(1).strip()))
            continue

        if line.startswith("#"):
            # Other headings (rare) — treat as scene title without hashes
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


def add_para(doc: Document, text: str, *, space_before: int = 0) -> None:
    p = doc.add_paragraph(text)
    if space_before:
        p.paragraph_format.space_before = Pt(space_before)


def build_doc(
    chapters: list[tuple[int, str, list[tuple[str, str]]]],
    *,
    subtitle: str,
    banner: str,
    blurb: str,
    source_note: str,
    end_line: str,
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

    act_by_start = {n: label for n, label in ACTS}
    for num, title, blocks in chapters:
        if num in act_by_start:
            add_para(doc, act_by_start[num], space_before=18)
        add_para(doc, f"Chapter {num}", space_before=14)
        add_para(doc, title)
        for kind, text in blocks:
            if kind == "scene":
                add_para(doc, text, space_before=10)
            else:
                add_para(doc, text)

    add_para(doc, end_line, space_before=18)
    return doc


def main() -> None:
    EXPORTS.mkdir(exist_ok=True)
    sha = git_short()
    all_ch = [parse_chapter(p) for _, p in chapter_files()]
    assert [n for n, _, _ in all_ch] == list(range(1, 35)), "Expected chapters 1–34"

    label = (
        "DECISION COLD-READ · Story-first + Act5 + gold dwell + anti-formula + tissue/soft-joint densify · "
        "Not finished-line (gravity/play/humour still residual)"
    )

    full = build_doc(
        all_ch,
        subtitle="Book 1 — FULL Review Draft (Chapters 1–34)",
        banner="THIS FILE CONTAINS ALL 34 CHAPTERS · OPENS WITH CHAPTER 1",
        blurb="Prose export for reading · metadata stripped\n" + label,
        source_note=f"Source: main @ {sha} · chapters 1–34",
        end_line="— End of Book 1 full review export —",
    )
    full_path = EXPORTS / "Ides_Book1_FULL_Ch01-34.docx"
    full.save(full_path)
    # Alias used by earlier review packets
    full.save(EXPORTS / "Ides_Book1_Review.docx")

    golden_ch = [c for c in all_ch if 14 <= c[0] <= 19]
    golden = build_doc(
        golden_ch,
        subtitle="Book 1 — Golden Sample ONLY (Chapters 14–19)",
        banner="SAMPLE ONLY · STARTS AT CHAPTER 14 · NOT THE FULL BOOK",
        blurb="Stand-alone sample · Ides through funeral\n" + label,
        source_note=f"Source: main @ {sha} · chapters 14–19 only",
        end_line="— End of golden chapters sample —",
    )
    golden_path = EXPORTS / "Ides_Book1_Golden_Chapters.docx"
    golden.save(golden_path)
    golden.save(EXPORTS / "Ides_Book1_Golden_ONLY_Ch14-19.docx")

    print(f"Wrote {full_path}")
    print(f"Wrote {golden_path}")
    print(f"Source SHA {sha}; chapters {len(all_ch)}")


if __name__ == "__main__":
    main()

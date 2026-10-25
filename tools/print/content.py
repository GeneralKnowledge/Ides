"""Book 1 reading text as structured data for the print interior.

Chapters are parsed by tools/export_book1_docx.py, so the print interior and
the tracked DOCX reading copy strip the same metadata and keep the same
paragraphs. Back matter keeps its bold labels (set in small caps in print).

Runs are [text, style] with style "" (roman), "i" (italic) or "sc" (small caps).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import export_book1_docx as ex  # noqa: E402

LIST_ITEM = re.compile(r"^\d+\.\s")
INLINE = re.compile(r"\*\*(.+?)\*\*|\*([^*\n]+?)\*")


def runs(text: str) -> list[list[str]]:
    out: list[list[str]] = []
    pos = 0
    for m in INLINE.finditer(text):
        if m.start() > pos:
            out.append([text[pos : m.start()], ""])
        if m.group(1) is not None:
            # Bold label; may itself hold italics.
            for t, s in runs(m.group(1)):
                out.append([t, "i" if s == "i" else "sc"])
        else:
            out.append([m.group(2), "i"])
        pos = m.end()
    if pos < len(text):
        out.append([text[pos:], ""])
    return out


def plain(rs: list[list[str]]) -> str:
    return "".join(t for t, _ in rs)


def parse_back(path: Path) -> dict:
    title = None
    blocks: list[dict] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# "):
            if title is not None:
                raise SystemExit(f"{path.name}: more than one top-level heading")
            title = line[2:].strip()
        elif line.startswith("## "):
            blocks.append({"t": "sub", "runs": runs(line[3:].strip())})
        elif line.startswith("- "):
            blocks.append({"t": "bullet", "runs": runs(line[2:].strip())})
        else:
            blocks.append({"t": "p", "runs": runs(line)})
    if not title:
        raise SystemExit(f"{path.name}: no '# Title' heading")
    return {"kind": "back", "title": title, "running": title, "blocks": blocks}


def build() -> tuple[list[Path], dict]:
    files, chapters = ex.load_chapters()
    acts = dict(ex.ACTS)
    sections: list[dict] = []
    for num, title, blocks in chapters:
        sec: dict = {
            "kind": "chapter",
            "number": str(num),
            "label": "Prologue" if num == 0 else f"Chapter {num}",
            "title": title,
            "running": "Prologue" if num == 0 else title,
            "blocks": [],
        }
        if num in acts:
            label, _, name = acts[num].partition(": ")
            sec["act"] = {"label": label, "title": name}
        for kind, text in blocks:
            if kind == "scene":
                t = "scene"
            elif LIST_ITEM.match(text):
                t = "item"
            else:
                t = "p"
            sec["blocks"].append({"t": t, "runs": runs(text)})
        if not any(b["t"] == "p" for b in sec["blocks"]):
            raise SystemExit(f"{sec['label']}: no prose paragraphs parsed")
        sections.append(sec)
    for path in ex.BACK_MATTER:
        if not path.exists():
            raise SystemExit(f"missing back matter: {path.relative_to(ex.ROOT)}")
        sections.append(parse_back(path))
    return files, {"sections": sections}


def reading_words(data: dict) -> list[str]:
    """Every word a reader should find after the front matter, in order."""
    words: list[str] = []
    for sec in data["sections"]:
        if "act" in sec:
            words += f"{sec['act']['label']} {sec['act']['title']}".split()
        if sec["kind"] == "chapter":
            words += sec["label"].split() + sec["title"].split()
        else:
            words += sec["title"].split()
        for b in sec["blocks"]:
            words += plain(b["runs"]).split()
    return words

#!/usr/bin/env python3
"""Build a stamped reading copy of Punic War experiment from experiments/punic_war/draft/.

Scenes are taken in storyboard order (experiments/punic_war/storyboard/scenes.tsv); only scenes
that exist as experiments/punic_war/draft/act*/<ID>.md are included. Chapter numbers are
assigned here, in that order, and nowhere else. The title page carries a stamp
(git commit and a digest of the scene files) so a reader's copy can be
identified later.

Usage: python3 tools/export_punic_docx.py [--acts I,II] [--out PATH]
"""
import argparse
import csv
import hashlib
import re
import subprocess
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.shared import Pt, Cm

ROOT = Path(__file__).resolve().parent.parent
B2 = ROOT / "experiments" / "punic_war"
ACT_TITLES = {"I": "The Crossing", "II": "Cannae", "III": "Italy Chooses", "IV": "The Brother"}


def scene_files(acts):
    rows = list(csv.DictReader(open(B2 / "storyboard" / "scenes.tsv", encoding="utf-8"), delimiter="\t"))
    out = []
    for r in rows:
        if acts and r["act"] not in acts:
            continue
        f = B2 / "draft" / f"act{['I','II','III','IV'].index(r['act']) + 1}" / f"{r['id']}.md"
        if f.exists():
            out.append((r, f))
    return out


def parse(f):
    text = f.read_text(encoding="utf-8")
    title = text.splitlines()[0].lstrip("# ").strip()
    body = text.split("\n---\n", 1)[1].strip()
    return title, [p.strip() for p in body.split("\n\n") if p.strip()]


def add_runs(par, text):
    # *italic* only
    for i, chunk in enumerate(re.split(r"\*([^*]+)\*", text)):
        run = par.add_run(chunk)
        run.italic = bool(i % 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--acts", default="")
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    acts = [a for a in args.acts.split(",") if a]
    scenes = scene_files(acts)
    digest = hashlib.sha256(b"".join(f.read_bytes() for _, f in scenes)).hexdigest()[:12]
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()

    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = "Georgia"
    st.font.size = Pt(11.5)
    for s in doc.sections:
        s.page_width, s.page_height = Cm(21), Cm(29.7)
        s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Cm(2.5)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Punic War experiment")
    r.font.size = Pt(28)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run("The Second Punic War, 218–207 BC").italic = True
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    label = ", ".join(f"Act {a}" for a in (acts or ["I", "II", "III", "IV"]))
    p.add_run(f"Reading copy: {label}")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sr = p.add_run(f"Stamp {commit}-{digest}")
    sr.font.size = Pt(9)

    chapter, current_act, words = 0, None, 0
    for row, f in scenes:
        title, paras = parse(f)
        if row["act"] != current_act:
            current_act = row["act"]
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
            h = doc.add_paragraph()
            h.alignment = WD_ALIGN_PARAGRAPH.CENTER
            hr = h.add_run(f"Act {current_act}\n{ACT_TITLES[current_act]}")
            hr.font.size = Pt(20)
        chapter += 1
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        h = doc.add_paragraph()
        h.alignment = WD_ALIGN_PARAGRAPH.CENTER
        hr = h.add_run(f"{chapter}\n{title}")
        hr.font.size = Pt(16)
        for i, text in enumerate(paras):
            par = doc.add_paragraph()
            par.paragraph_format.space_after = Pt(0)
            par.paragraph_format.line_spacing = 1.35
            if i:
                par.paragraph_format.first_line_indent = Cm(0.7)
            add_runs(par, text)
            words += len(text.split())

    out = Path(args.out) if args.out else ROOT / "exports" / f"PunicWar_{'Act' + '-'.join(acts) if acts else 'FULL'}.docx"
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out)
    print(f"{out}  chapters={chapter}  words={words:,}  stamp={commit}-{digest}")


if __name__ == "__main__":
    main()

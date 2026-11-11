#!/usr/bin/env python3
"""Consistency check for the Punic War experiment canon pack (experiments/punic_war/canon/).

Checks:
  1. Every POV character sheet has the required sections.
  2. Every chronology row has a source and a check mark.
  3. Every handle in names.md is used for one person only.
  4. Reports how many lines are still marked "to check".

Exit status 1 if any structural check fails. Lines marked "to check" are
reported but do not fail the check until --strict is given (the storyboard
gate runs with --strict).
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "experiments" / "punic_war" / "canon"
REQUIRED = [
    "## Facts",
    "## Where",
    "## What he knows and when",
    "## How he talks",
    "## Invention zone",
    "## Open questions",
]
NON_SHEETS = {"README.md", "major_figures.md"}
CHECK_OK = re.compile(r"^(text|to check|partly text|outside the book)( \([^)]*\))?(, (flag [A-Z]|to check))*(, flag [A-Z])?$")


def table_rows(text):
    for line in text.splitlines():
        if line.startswith("|") and not re.match(r"^\|[-| ]+\|$", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            yield cells


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="fail on any 'to check' line")
    args = ap.parse_args()
    errors, to_check = [], 0

    for sheet in sorted((ROOT / "characters").glob("*.md")):
        if sheet.name in NON_SHEETS:
            continue
        text = sheet.read_text(encoding="utf-8")
        for sec in REQUIRED:
            if sec == "## Where":
                ok = "## Where he is" in text or "## The record he must follow" in text
            else:
                ok = sec in text
            if not ok:
                errors.append(f"{sheet.name}: missing section '{sec}'")
        to_check += len(re.findall(r"\bto check\b", text))

    chron = (ROOT / "chronology.md").read_text(encoding="utf-8")
    for cells in table_rows(chron):
        if cells[0] in ("When",) or len(cells) != 4:
            continue
        when, event, source, check = cells
        if not source:
            errors.append(f"chronology: no source for '{event[:50]}'")
        if not CHECK_OK.match(check):
            errors.append(f"chronology: bad check mark '{check}' for '{event[:50]}'")
        if "to check" in check:
            to_check += 1

    names = (ROOT / "names.md").read_text(encoding="utf-8")
    seen = {}
    for cells in table_rows(names):
        if len(cells) < 3 or cells[0] == "Name in the sources":
            continue
        for handle in re.findall(r"\*\*(.+?)\*\*", cells[2]):
            if handle in seen:
                errors.append(f"names: handle '{handle}' used for '{seen[handle]}' and '{cells[1][:40]}'")
            seen[handle] = cells[1][:40]

    for e in errors:
        print("FAIL", e)
    print(f"{len(errors)} failures; {to_check} items still marked 'to check'")
    if errors or (args.strict and to_check):
        sys.exit(1)


if __name__ == "__main__":
    main()

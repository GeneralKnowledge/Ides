#!/usr/bin/env python3
"""Check book2/canon/names.md: every handle appears once across both books.

Reads the first column of every table row in names.md. Fails if a handle is
listed twice (case-insensitive), or if a handle is also on the dead or
retired lists. Usage: python3 tools/book2_names_check.py
"""
import re
import sys
from pathlib import Path

NAMES = Path(__file__).resolve().parent.parent / "book2" / "canon" / "names.md"


def main() -> int:
    text = NAMES.read_text(encoding="utf-8")
    handles = {}
    failures = 0
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Handle"):
            continue
        cell = line.split("|")[1].strip()
        for h in [c.strip() for c in cell.split(",")]:
            key = h.lower()
            if key in handles:
                print(f"DUPLICATE handle: {h!r} (also {handles[key]!r})")
                failures += 1
            handles[key] = h
    for label in ("Dead before Book 2 opens", "Retired invented names"):
        m = re.search(label + r"[^:]*:\s*(.+?)\.", text)
        if not m:
            continue
        for h in [x.strip() for x in m.group(1).split(",")]:
            h = re.sub(r"\s*\(.*\)", "", h)
            if h.lower() in handles:
                print(f"REUSED handle {h!r}: on the '{label}' list and in a table")
                failures += 1
    print(f"{len(handles)} handles, {failures} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

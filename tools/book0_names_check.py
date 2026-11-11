#!/usr/bin/env python3
"""Check book0/canon/names.md against itself and against book2/canon/names.md.

A Book 0 handle may appear once in Book 0's tables and must not already be a
handle in Book 2's list (which carries Book 1's cast). The section headed
"Already in Books 1 and 2" is not read as new handles.
Usage: python3 tools/book0_names_check.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def handles(path, stop=None):
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if stop and line.startswith("## ") and stop in line:
            break
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Handle"):
            continue
        for h in line.split("|")[1].split(","):
            if h.strip():
                out.append(h.strip())
    return out


def main() -> int:
    new = handles(ROOT / "book0" / "canon" / "names.md", stop="Already in Books 1 and 2")
    old = {h.lower() for h in handles(ROOT / "book2" / "canon" / "names.md")}
    seen, failures = set(), 0
    for h in new:
        if h.lower() in seen:
            print(f"DUPLICATE in Book 0: {h!r}")
            failures += 1
        if h.lower() in old:
            print(f"ALREADY a Book 1/2 handle: {h!r}")
            failures += 1
        seen.add(h.lower())
    print(f"{len(new)} new handles, {failures} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

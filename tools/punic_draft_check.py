#!/usr/bin/env python3
"""Mechanical checks on Punic War experiment draft scenes (experiments/punic_war/draft/act*/<ID>.md).

For each scene: words of prose (after the header's '---' line) against the
storyboard budget, em dashes, one-word sentences in narration, banned words,
straight quotes. Exit 1 on em dashes, banned words or straight quotes.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "experiments" / "punic_war"
BANNED = [r"\bfiled\b", r"little did", r"\bMonday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday\b", r"\bokay\b"]


def prose(text):
    parts = text.split("\n---\n", 1)
    return parts[1] if len(parts) > 1 else text


def narration_only(body):
    # drop quoted speech so one-word replies in dialogue are allowed
    return re.sub(r"“[^”]*”", "", body)


def main():
    board = {r["id"]: r for r in csv.DictReader(open(ROOT / "storyboard" / "scenes.tsv", encoding="utf-8"), delimiter="\t")}
    errors, total, rows = [], 0, []
    files = sorted(ROOT.glob("draft/act*/*.md"))
    for f in files:
        sid = f.stem
        body = prose(f.read_text(encoding="utf-8"))
        words = len(body.split())
        total += words
        budget = int(board[sid]["words"]) if sid in board else 0
        flag = ""
        if budget and words > budget * 1.2:
            flag = "over"
        if budget and words < budget * 0.7:
            flag = "short"
        if "—" in body:
            errors.append(f"{sid}: em dash")
        for pat in BANNED:
            if re.search(pat, body, re.I):
                errors.append(f"{sid}: banned /{pat}/")
        if re.search(r"[A-Za-z]'[A-Za-z]|\"", body):
            errors.append(f"{sid}: straight quote or apostrophe")
        one = re.findall(r"(?:^|[.!?]\s+)([A-Z][a-z]+[.!?])(?=\s|$)", narration_only(body), re.M)
        rows.append((sid, words, budget, flag, len(one), one))
        if sid not in board:
            errors.append(f"{sid}: not in storyboard")
    for sid, w, b, flag, n, one in rows:
        extra = f"  one-word: {', '.join(one)}" if n else ""
        print(f"{sid:7} {w:>6,} / {b:>6,} {flag:5}{extra}")
    print(f"\n{len(rows)} scenes, {total:,} words")
    for e in errors:
        print("FAIL", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

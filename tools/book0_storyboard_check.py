#!/usr/bin/env python3
"""Checks for the Book 0 storyboard (book0/storyboard/scenes.tsv).

Flags:
  - date rewinds (a scene dated before the one it follows, beyond a season)
  - POV absences longer than --gap words (default 15,000)
  - scenes where nothing changes (empty what_changes)
  - dependencies that point forward or to unknown scenes
  - act and book word totals against the contract
  - where the hinge falls (first scene dated 48-08-09, Pharsalus)
  - empty pov_lens (what the POV notices, misreads, hides)
Prints a report; exit 1 on rewinds, bad dependencies or static scenes.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "book0"
ACT_BUDGET = {"I": 20000, "II": 20000, "III": 22000, "IV": 22000}
SEASON = {"spring": 4, "summer": 7, "autumn": 10, "winter": 12}


def date_key(d):
    """'41-11', '41-12-31', '40-spring', '40' -> sortable tuple (BC years count down)."""
    parts = d.split("-")
    year = int(parts[0])
    month = 6
    day = 15
    if len(parts) > 1:
        month = SEASON.get(parts[1], None) or int(parts[1])
    if len(parts) > 2:
        day = int(parts[2])
    return (-year, month, day)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gap", type=int, default=15000)
    args = ap.parse_args()
    rows = list(csv.DictReader(open(ROOT / "storyboard" / "scenes.tsv", encoding="utf-8"), delimiter="\t"))
    errors, warnings = [], []
    ids = [r["id"] for r in rows]
    pos = {r["id"]: i for i, r in enumerate(rows)}
    total = sum(int(r["words"]) for r in rows)

    # rewinds: allow a scene undated within a year ('40') to sit anywhere in that year
    for prev, cur in zip(rows, rows[1:]):
        if len(cur["date"].split("-")) == 1 or len(prev["date"].split("-")) == 1:
            if int(cur["date"].split("-")[0]) > int(prev["date"].split("-")[0]):
                errors.append(f"rewind: {cur['id']} ({cur['date']}) after {prev['id']} ({prev['date']})")
            continue
        if date_key(cur["date"]) < date_key(prev["date"]):
            errors.append(f"rewind: {cur['id']} ({cur['date']}) after {prev['id']} ({prev['date']})")

    for r in rows:
        if r["pov"] != "TBD" and not r["pov_lens"].strip():
            warnings.append(f"lens: {r['id']} has no pov_lens")
        if r["pov"] == "TBD":
            warnings.append(f"open: {r['id']} is not yet chosen")
            continue
        if not r["what_changes"].strip():
            errors.append(f"static: {r['id']} has no change")
        for dep in filter(None, re.split(r"[ ,]+", r["depends_on"])):
            if dep not in pos:
                errors.append(f"dependency: {r['id']} depends on unknown {dep}")
            elif pos[dep] >= pos[r["id"]]:
                errors.append(f"dependency: {r['id']} depends on later scene {dep}")

    # POV absences, measured in words between the end of one scene and the start of the next
    run = 0
    starts = []
    for r in rows:
        starts.append(run)
        run += int(r["words"])
    by_pov = {}
    for r, s in zip(rows, starts):
        by_pov.setdefault(r["pov"], []).append((s, s + int(r["words"]), r["id"]))
    gaps = []
    for pov, spans in sorted((k, v) for k, v in by_pov.items() if k != "TBD"):
        last_end, last_id = spans[0][1], spans[0][2]
        if spans[0][0] > args.gap:
            gaps.append((spans[0][0], pov, "start", spans[0][2]))
        for s, e, sid in spans[1:]:
            if s - last_end > args.gap:
                gaps.append((s - last_end, pov, last_id, sid))
            last_end, last_id = e, sid
        if total - last_end > args.gap:
            gaps.append((total - last_end, pov, last_id, "end"))

    print(f"Scenes: {len(rows)}   Words: {total:,}")
    print("\nActs (planned / contract):")
    for act, budget in ACT_BUDGET.items():
        w = sum(int(r["words"]) for r in rows if r["act"] == act)
        flag = "" if abs(w - budget) <= budget * 0.1 else "   <-- outside 10%"
        print(f"  {act:>3}: {w:>6,} / {budget:,}{flag}")
    hinge = next((s for r, s in zip(rows, starts) if r["date"].startswith("48-08-09")), None)
    if hinge is not None:
        print(f"\nPharsalus starts at {hinge:,} words ({hinge / total:.0%} of the book)")
    print("\nPOV share (words, scenes):")
    for pov, spans in sorted(by_pov.items(), key=lambda kv: -sum(e - s for s, e, _ in kv[1])):
        w = sum(e - s for s, e, _ in spans)
        print(f"  {pov}: {w:>6,}  {len(spans):>2}")
    if gaps:
        print(f"\nPOV absences over {args.gap:,} words:")
        for g, pov, a, b in sorted(gaps, reverse=True):
            print(f"  {pov}: {g:,} words between {a} and {b}")
    for w in warnings:
        print("WARN", w)
    for e in errors:
        print("FAIL", e)
    print(f"\n{len(errors)} failures, {len(gaps)} long absences")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

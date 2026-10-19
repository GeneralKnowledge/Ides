#!/usr/bin/env python3
"""Regenerate em_dash_removal_log.{jsonl,md} from pre-purge git rev vs working tree.

Usage (repo root):
  python3 archive/reports/_regen_em_dash_removal_log.py
"""
from __future__ import annotations

import difflib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

EM = "\u2014"
ELL = "\u2026"
BEFORE_REV = "12f4591"  # tip before purge commit aa2d173
ROOT = Path(__file__).resolve().parents[2]
REPORTS = Path(__file__).resolve().parent


def git_show(rev: str, path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{rev}:{path}"], cwd=ROOT, text=True
    )


def main() -> None:
    paths = [
        f"drafts/book1/{p.name}"
        for p in sorted((ROOT / "drafts/book1").glob("ch*.md"))
    ]
    paths.append("drafts/README.md")

    line_records: list[dict] = []
    site_records: list[dict] = []

    for path in paths:
        before_text = git_show(BEFORE_REV, path)
        after_text = (ROOT / path).read_text(encoding="utf-8")
        blines = before_text.splitlines()
        alines = after_text.splitlines()
        sm = difflib.SequenceMatcher(None, blines, alines, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                continue
            if tag == "replace" and (i2 - i1) == (j2 - j1):
                for bi, ai in zip(range(i1, i2), range(j1, j2)):
                    b, a = blines[bi], alines[ai]
                    if b == a or b.rstrip() == a.rstrip() and b != a:
                        if b.rstrip() == a.rstrip() and b != a:
                            continue
                        if b == a:
                            continue
                    n = b.count(EM)
                    if n == 0:
                        if b.rstrip() != a.rstrip():
                            line_records.append(
                                {
                                    "path": path,
                                    "before_line": bi + 1,
                                    "after_line": ai + 1,
                                    "em_count_removed": 0,
                                    "before": b,
                                    "after": a,
                                    "kind": "hand_polish",
                                    "flags": [],
                                }
                            )
                        continue

                    flags: set[str] = set()
                    if a.count("(") > b.count("("):
                        flags.add("paren_aside")
                    if ELL in a and ELL not in b:
                        flags.add("ellipsis_cutoff")
                    if b.lstrip().startswith("#") and EM in b:
                        flags.add("header_colon")
                    # Stacked punct, but allow abbrev + colon (*Visellius, A.: doubtful*)
                    if re.search(r"\.,|,\.|,;|;,|::|\.\.", a) or re.search(
                        r"(?<![A-Za-z])[,.:;]{2,}", a
                    ):
                        flags.add("double_punct")
                    elif re.search(r"[,:;]{2,}", a):
                        flags.add("double_punct")

                    for m in re.finditer(EM, b):
                        i = m.start()
                        j = i - 1
                        while j >= 0 and b[j] == " ":
                            j -= 1
                        k = i + 1
                        while k < len(b) and b[k] == " ":
                            k += 1
                        prev = b[j] if j >= 0 else ""
                        nxt = b[k] if k < len(b) else ""
                        ctx_before = b[max(0, i - 40) : i]
                        ctx_after = b[i + 1 : i + 41]

                        if nxt in "\"'”’" or prev in "\"'“‘":
                            repl_kind = "ellipsis"
                        elif prev.isdigit() or (
                            b.lstrip().startswith("#") and i < 40
                        ):
                            repl_kind = "colon"
                        elif prev.islower() and nxt.isupper():
                            rw = re.match(r"\S+", b[k:] or "")
                            word = rw.group(0) if rw else ""
                            if word and f", {word}" in a:
                                repl_kind = "comma"
                            elif word and f". {word}" in a:
                                repl_kind = "period"
                                flags.add("period_from_lowercase_em")
                            elif word and (
                                f" ({word}" in a or f"({word}" in a
                            ):
                                repl_kind = "paren"
                            else:
                                repl_kind = "unknown_cap"
                        elif prev.islower() and nxt.islower():
                            repl_kind = "comma_or_paren"
                        else:
                            repl_kind = "other"

                        site_records.append(
                            {
                                "path": path,
                                "before_line": bi + 1,
                                "after_line": ai + 1,
                                "em_index_in_line": i,
                                "prev_char": prev,
                                "next_char": nxt,
                                "repl_kind": repl_kind,
                                "context": f"{ctx_before}⟦—⟧{ctx_after}",
                                "before_line_text": b,
                                "after_line_text": a,
                            }
                        )

                    line_records.append(
                        {
                            "path": path,
                            "before_line": bi + 1,
                            "after_line": ai + 1,
                            "em_count_removed": n,
                            "before": b,
                            "after": a,
                            "kind": "em_replace",
                            "flags": sorted(flags),
                        }
                    )
            else:
                for bi in range(i1, i2):
                    b = blines[bi]
                    if EM in b:
                        line_records.append(
                            {
                                "path": path,
                                "before_line": bi + 1,
                                "after_line": None,
                                "em_count_removed": b.count(EM),
                                "before": b,
                                "after": None,
                                "kind": f"complex_{tag}",
                                "flags": ["alignment_complex"],
                            }
                        )

    missing = 0
    for path in paths:
        before_text = git_show(BEFORE_REV, path)
        for i, line in enumerate(before_text.splitlines(), 1):
            if EM not in line:
                continue
            hits = [
                r
                for r in line_records
                if r["path"] == path
                and r["before_line"] == i
                and r["em_count_removed"] > 0
            ]
            if not hits:
                hits = [
                    r
                    for r in line_records
                    if r["path"] == path and r.get("before") == line
                ]
            if not hits:
                missing += 1

    em_chars = sum(r["em_count_removed"] for r in line_records)
    by_ch = Counter()
    for r in line_records:
        by_ch[r["path"]] += r["em_count_removed"]

    period_suspects = [
        r
        for r in line_records
        if "period_from_lowercase_em" in r.get("flags", [])
    ]
    double = [
        r for r in line_records if "double_punct" in r.get("flags", [])
    ]
    hands = [r for r in line_records if r["kind"] == "hand_polish"]

    jsonl = REPORTS / "em_dash_removal_log.jsonl"
    with jsonl.open("w", encoding="utf-8") as f:
        for s in site_records:
            f.write(json.dumps({"type": "site", **s}, ensure_ascii=False) + "\n")
        for r in line_records:
            f.write(json.dumps({"type": "line", **r}, ensure_ascii=False) + "\n")

    md = f"""# Em-dash removal log

**Purpose:** Record every place U+2014 was removed from drafts, and sanity-check the replacements.

**Compared:** `{BEFORE_REV}` (pre-purge) → current working tree (purge `aa2d173` + hand polish).

| Artifact | Role |
|----------|------|
| [`em_dash_removal_log.jsonl`](em_dash_removal_log.jsonl) | Machine log: one `site` record per removed em dash + one `line` record per changed line |
| [`_regen_em_dash_removal_log.py`](_regen_em_dash_removal_log.py) | Regenerator |
| [`em_dash_author_voice.md`](em_dash_author_voice.md) | Policy |

## Totals

| Metric | Count |
|--------|------:|
| Em-dash characters removed | **{em_chars}** |
| Site records (one per dash) | {len(site_records)} |
| Lines that had ≥1 em dash | {sum(1 for r in line_records if r['em_count_removed']>0)} |
| Completeness gaps (pre-purge lines with EM not logged) | {missing} |
| Hand-polish lines (no EM on before-line) | {len(hands)} |

### Replacement kinds (heuristic per site)

| Kind | Count |
|------|------:|
"""
    for k, n in Counter(s["repl_kind"] for s in site_records).most_common():
        md += f"| `{k}` | {n} |\n"

    md += "\n### By file\n\n| File | Em dashes removed |\n|------|------------------:|\n"
    for path, n in sorted(by_ch.items()):
        md += f"| `{path}` | {n} |\n"

    md += f"""
## Sanity check

Not automatic defects. Highest-priority review:

### 1. Double punctuation ({len(double)})

"""
    for r in double:
        md += f"- `{r['path']}` L{r['before_line']}\n  - BEFORE: {r['before'][:220]}\n  - AFTER:  {r['after'][:220]}\n\n"

    if not double:
        md += "_None._\n\n"

    md += f"""### 2. Period that may have replaced an em dash after a lowercase letter ({len(period_suspects)})

Risk: false sentence break where an apposition should be a comma or parenthesis.

Known acceptable after hand review:
- `drafts/book1/ch13_go.md` GO list: `thickened. Ligarius’s pride…` (new sentence inside Cassius’s speech; keep).

"""
    for r in period_suspects[:50]:
        note = ""
        if r["path"].endswith("ch13_go.md") and r["before_line"] == 107:
            note = " **(reviewed: keep)**"
        md += f"- `{r['path']}` L{r['before_line']}{note}\n  - BEFORE: {r['before'][:220]}\n  - AFTER:  {r['after'][:220]}\n\n"
    if not period_suspects:
        md += "_None._\n\n"
    elif len(period_suspects) > 50:
        md += f"*…{len(period_suspects)-50} more; filter JSONL sites with `repl_kind` = `period`.*\n\n"

    md += f"""### 3. Hand polish after automated purge ({len(hands)})

"""
    if not hands:
        md += "_None as separate line records (hand fixes may sit on the same lines as em-replacements)._\n"
    else:
        for r in hands:
            md += f"- `{r['path']}` L{r['before_line']}→L{r['after_line']}\n"

    md += """
## How to read the JSONL

- `type: site` — one removed em dash: `path`, `before_line`, `context` (with `⟦—⟧` marker), `repl_kind`, full before/after line texts.
- `type: line` — whole-line before/after for grep-friendly review.

```bash
python3 archive/reports/_regen_em_dash_removal_log.py
# or
git diff 12f4591 -- drafts/book1 drafts/README.md
```

## Policy

Do not restore U+2014. If a replacement feels wrong, fix with comma / period / colon / parentheses / ellipsis only.
"""
    # Keep a visible marker in the human log without using U+2014 in repo prose habit:
    md = md.replace(EM, "[EM]")
    (REPORTS / "em_dash_removal_log.md").write_text(md, encoding="utf-8")
    print(
        f"wrote {jsonl.name} + em_dash_removal_log.md "
        f"(em={em_chars} sites={len(site_records)} missing={missing} "
        f"double={len(double)} period_suspects={len(period_suspects)})"
    )


if __name__ == "__main__":
    main()

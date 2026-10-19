# Em-dash policy: author voice (supersedes the 666 joke)

**Status:** Active. Supersedes the earlier “lock 666” joke.  
**Author:** has never used the em dash (U+2014) in their own writing; treats it as foreign / LLM residue.

---

## Decision

**Radical remove from manuscript drafts.** The em dash is not house style.

| Do | Do not |
|----|--------|
| Keep `drafts/book1` free of U+2014 | Restore em dashes for “rhythm” or LLM pause fashion |
| Prefer commas, periods, colons, parentheses, or ellipsis (`…`) for cutoffs | Invent a new decorative dash dialect |
| Fix any awkward replacement when a read flags it | Run a second poetic dash pass |

## What was done

Book-wide purge of U+2014 across `drafts/book1/ch*.md` (prose, headers, continuity blocks in those files).

Typical substitutions:

- Dialogue cutoffs → `…`
- Paired asides → `(…)`
- Clause / title breaks → `,` / `.` / `:`
- Markdown `---` rules left untouched (ASCII hyphens)

Live check after purge: **0** U+2014 in `drafts/book1/ch*.md`.

## Removal record + sanity

| File | Role |
|------|------|
| [`em_dash_removal_log.md`](em_dash_removal_log.md) | Human summary + sanity flags |
| [`em_dash_removal_log.jsonl`](em_dash_removal_log.jsonl) | One `site` record per removed dash (929) |
| [`_regen_em_dash_removal_log.py`](_regen_em_dash_removal_log.py) | Regenerator vs pre-purge `12f4591` |

Sanity after purge: one ledger `A., doubtful` fixed to `A.: doubtful`; one intentional period at Ch 13 GO (`thickened. Ligarius’s…`). Completeness gaps: 0.

## Reading note

Tomorrow’s full read will see the purged punctuation. If a sentence feels flattened or wrongly stopped, note the chapter/moment; do not put the em dash back as a default fix.

## Non-goals

No Philippi expand. No plot changes. No Ch 1–3 polish war beyond punctuation substitution. No requirement that continuity reports outside `drafts/book1` be scrubbed in the same pass.

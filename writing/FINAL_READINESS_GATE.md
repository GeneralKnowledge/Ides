# Final readiness gate — Book 1

**Status:** Standing rule from 2026-10-22.  
**Purpose:** Decide whether the manuscript is ready to leave the repository, with evidence rather than another read-through by people who already know what every passage is meant to do.  
**Not:** A new editing campaign. The gates find defects; they do not license polishing.

How the manuscript may be *changed* is governed elsewhere: evidence before edit, voice survival and the stopping rule live in [`HUMAN_VOICE_RULES.md`](HUMAN_VOICE_RULES.md); historical verification and change-impact review live in [`LLM_WRITING_BRIEF.md`](LLM_WRITING_BRIEF.md) §12. This file covers only whether the result can go out.

Passing every gate does not mean the book is perfect. It means the project has a defensible process for finding real defects, fixing them without collateral damage, and knowing when to stop.

---

## Gate 1: Reading-copy integrity

The tracked DOCX must be a faithful rendering of the current manuscript, not merely a file that generated without errors.

**Evidence:** `python tools/export_book1_docx.py --check` prints `OK`. The check rebuilds the reading text from `drafts/book1/` and fails unless:

- all 34 chapter headings appear once, in order;
- every reading paragraph is present exactly once, in sequence, with italics intact (nothing omitted, duplicated or reordered);
- no card fields, scene ids, lock tags, editor notes or stray markdown reach the reader;
- the copy's source digest matches the manuscript, so it is not stale;
- the title page and document properties name the manuscript commit, its date, the generation date and the digest, and say if it was built from uncommitted changes.

The digest is the authoritative link to the source text. The commit is the last one that touched `drafts/book1/`; after a squash merge of a PR that changed the manuscript, it may name a branch commit, and the digest still verifies the copy.

**Rule:** regenerate and commit `exports/Ides_Book1_FULL_Ch01-34.docx` (`git add -f`) in the same PR as any manuscript change. CI runs the check on every PR that touches the manuscript, the exporter or the copy.

**Not covered by the script:** how headings, dialogue, paragraph spacing and special characters *look* in Word. Open the copy once after any exporter change and page through a dialogue scene, a letter, Chapter 16 and the last page.

## Gate 2: Mechanical copyedit

**Evidence:** one complete pass over the reading copy for spelling, grammar, punctuation, quotation marks (straight vs curly, nesting), typos, inconsistent spellings of names and Latin, formatting and accidental repetition. Use automated tools to *locate* candidates; a human decides each fix.

**Pass when:** every candidate is fixed, rejected as deliberate (dialect, character voice, Latin convention) or logged as open. Name spellings check against [`NAMES_MINOR_CAST.md`](NAMES_MINOR_CAST.md) and [`STYLE_GLOSSARY.md`](STYLE_GLOSSARY.md).

## Gate 3: Independent-reader validation

The one gate the author's rereads cannot replace.

**Evidence:** written feedback from readers who have not seen earlier drafts and do not know the intended solutions: ideally one who reads historical fiction and one general fiction reader who will respond to the story rather than the research, optionally a professional editor. Ask about comprehension (who is this, why does this matter, what just happened), pacing (where did you skim or stop), investment (whom did you care about, when) and confusion (what did you have to reread). Do not ask whether they agree with the design.

**Triage** every point before touching the manuscript:

| Class | Means | Action |
|-------|-------|--------|
| **Defect** | A factual, continuity, clarity or story problem you can demonstrate in the text | Fix, under the evidence-before-edit rule |
| **Reader response** | A real reaction (confused here, bored there, moved by this) that may or may not need a change | Weigh in context: does the passage fail, or is the reaction the one intended? |
| **Preference** | A suggestion that would make the book different, not necessarily better | Reject when it conflicts with the novel’s intent; note it either way |

Then make **one** correction round and check only the changed passages and their dependencies (`LLM_WRITING_BRIEF.md` §12b), not every chapter from scratch.

**Pass when:** every point is classified, every defect is fixed or deferred, and every confusion that stays is kept on purpose with a reason (a mystery meant to stay open, for example).

---

## Record

Keep one line per gate here. A gate re-opens only when the manuscript changes in a way its evidence no longer covers.

| Gate | State | Evidence |
|------|-------|----------|
| 1. Reading-copy integrity | Passing | `--check` OK, manuscript `f0bb9be` (2026-10-22) |
| 2. Mechanical copyedit | Not started | |
| 3. Independent reader | Not started | |

*End final readiness gate.*

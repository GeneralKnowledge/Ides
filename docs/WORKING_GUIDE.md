# Working guide

How the manuscript, canon and tools fit together. This was the repository's front page until 2026-11-07, when the root `README.md` became an introduction to the novel for readers. Nothing here changed in the move except link paths.

Historical fiction — Book 1 of a late-Republic novel (Rome ~46–42 BC), ending at Philippi.

## Source of truth (read in this order)

1. **Manuscript** — [`drafts/book1/`](../drafts/book1/) (Utica prologue + 38 chapters). Authoritative for what is presently written.
2. **Canon & anchors** — [`continuity/canon.md`](../continuity/canon.md), [`story/historical_anchors.md`](../story/historical_anchors.md), [`continuity/contradictions.md`](../continuity/contradictions.md).
3. **Story architecture** — [`story/`](../story/) (master timeline, POV lock, mysteries, consequences) + [`continuity/character_profiles/`](../continuity/character_profiles/) + [`continuity/expansion/subplot_tracks.md`](../continuity/expansion/subplot_tracks.md) (tracks, planned and landed) and [`beat_deposit_map.md`](../continuity/expansion/beat_deposit_map.md) (logged deposits).
4. **Writing guidance** — [`writing/LLM_WRITING_BRIEF.md`](../writing/LLM_WRITING_BRIEF.md), [`writing/CHAPTER_MAP.md`](../writing/CHAPTER_MAP.md), [`writing/`](../writing/).
5. **Research** — [`research/`](../research/) when a historical question arises.
6. **Archive** — [`archive/`](../archive/) completed plans, pass logs, and editorial history.

**Which file is current for what**

| Question | File |
|----------|------|
| What happens, and in which chapter | [`writing/CHAPTER_MAP.md`](../writing/CHAPTER_MAP.md) |
| What must stay true | [`continuity/canon.md`](../continuity/canon.md) |
| Which history we follow, and when | [`story/historical_anchors.md`](../story/historical_anchors.md), [`story/master_timeline.md`](../story/master_timeline.md) |
| Who a character is | [`continuity/character_profiles/`](../continuity/character_profiles/) |
| What is being built next | [`continuity/expansion/subplot_tracks.md`](../continuity/expansion/subplot_tracks.md) |
| How to write and revise | [`writing/HUMAN_VOICE_RULES.md`](../writing/HUMAN_VOICE_RULES.md), [`writing/LLM_WRITING_BRIEF.md`](../writing/LLM_WRITING_BRIEF.md), [`writing/STYLE_GLOSSARY.md`](../writing/STYLE_GLOSSARY.md) |
| What to send an outside reader | [`reader_feedback/SECOND_READER_QUESTIONNAIRE.md`](../reader_feedback/SECOND_READER_QUESTIONNAIRE.md) with the reading copy |
| Is it ready | [`writing/FINAL_READINESS_GATE.md`](../writing/FINAL_READINESS_GATE.md) |

Pre-draft beat sheets, scene cards and finished-phase records are in [`archive/planning/`](../archive/planning/) (moved 2026-10-23).

Open questions: [`continuity/unresolved_questions.md`](../continuity/unresolved_questions.md).  
Navigation by need: [`docs/INDEX.md`](INDEX.md).  
Project overview: [`docs/README.md`](README.md).

## Current state

Book 1 draft (Utica prologue + Ch 1–38) is in place; the Ch 1 dinner follows the prologue (2026-10-23). Mid-tier expansion and later development phases are **complete** (records in [`archive/`](../archive/)). Resume work from the manuscript and canon — not from completed phase plans.

**Book 1 ends at Philippi.** Actium / Principate are series hooks only, not this volume’s plot.

## Tools

DOCX export (metadata stripped): `python tools/export_book1_docx.py` → writes under `exports/`. It also writes an untracked A4 copy, `exports/Ides_Book1_FULL_Ch01-38_A4.docx`, for printing or reading on A4 paper (the 6 x 9 in book layout sits small in one corner of an A4 sheet). Only `exports/Ides_Book1_FULL_Ch01-38.docx` is tracked; it is stamped with its manuscript commit and source digest. `python tools/export_book1_docx.py --check` verifies it against the manuscript (also run in CI). See [`writing/FINAL_READINESS_GATE.md`](../writing/FINAL_READINESS_GATE.md).

Ebook (EPUB 3, for Kindle via Send to Kindle, Apple Books, Kobo): `python tools/export_book1_epub.py` → `exports/Ides_Book1_Ch01-38.epub` (untracked). Same reading text and order as the DOCX, reflowable, with a typographic cover; `--check` compares every paragraph with the manuscript and runs epubcheck if installed (`pip install epubcheck`, needs Java).

Print interior for a hand-sewn hardcover (129 × 198 mm, imposed in 16-page A4 signatures): `python tools/print/build_book1_print.py` → writes under `build/print/` (not tracked). See [`tools/print/README.md`](../tools/print/README.md).

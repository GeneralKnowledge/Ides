# Ides of March

Historical fiction — Book 1 of a late-Republic novel (Rome ~46–42 BC), ending at Philippi.

## Source of truth (read in this order)

1. **Manuscript** — [`drafts/book1/`](drafts/book1/) (34 chapters). Authoritative for what is presently written.
2. **Canon & anchors** — [`continuity/canon.md`](continuity/canon.md), [`story/historical_anchors.md`](story/historical_anchors.md), [`continuity/contradictions.md`](continuity/contradictions.md).
3. **Story architecture** — [`story/`](story/) (timeline, POV, scene cards, mysteries, consequences) + [`continuity/expansion/`](continuity/expansion/) + [`continuity/character_profiles/`](continuity/character_profiles/).
4. **Writing guidance** — [`writing/LLM_WRITING_BRIEF.md`](writing/LLM_WRITING_BRIEF.md), [`writing/CHAPTER_MAP.md`](writing/CHAPTER_MAP.md), [`writing/`](writing/).
5. **Research** — [`research/`](research/) when a historical question arises.
6. **Archive** — [`archive/`](archive/) completed plans, pass logs, and editorial history.

Open questions: [`continuity/unresolved_questions.md`](continuity/unresolved_questions.md).  
Navigation by need: [`docs/INDEX.md`](docs/INDEX.md).  
Project overview: [`docs/README.md`](docs/README.md).

## Current state

Book 1 draft (Utica prologue + Ch 1–34) is in place; the Ch 1 dinner follows the prologue (2026-10-23). Mid-tier expansion and later development phases are **complete** (records in [`archive/`](archive/)). Resume work from the manuscript and canon — not from completed phase plans.

**Book 1 ends at Philippi.** Actium / Principate are series hooks only, not this volume’s plot.

## Tools

DOCX export (metadata stripped): `python tools/export_book1_docx.py` → writes under `exports/`. Only `exports/Ides_Book1_FULL_Ch01-34.docx` is tracked; it is stamped with its manuscript commit and source digest. `python tools/export_book1_docx.py --check` verifies it against the manuscript (also run in CI). See [`writing/FINAL_READINESS_GATE.md`](writing/FINAL_READINESS_GATE.md).

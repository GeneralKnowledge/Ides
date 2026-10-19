# Reader DOCX export (post em-dash purge)

**Date:** 2026-10-19 (regenerated 07:19 UTC)  
**Branch:** `main`  
**Source:** `main` @ `61052b5` (after #56 em-dash purge + #57 exporter fix)  
**Exporter:** `tools/export_book1_docx.py`  
**Artifacts:** `exports/` (gitignored) and `/opt/cursor/artifacts/docx/`

---

## What shipped

| File | Contents |
|------|----------|
| `Ides_Book1_FULL_Ch01-34.docx` | Chapters 1–34, metadata stripped |
| `Ides_Book1_Review.docx` | Alias of FULL |
| `Ides_Book1_Golden_Chapters.docx` | Chapters 14–19 only |
| `Ides_Book1_Golden_ONLY_Ch14-19.docx` | Alias of Golden |

**Banner label:**  
`Book 1 reading export · dinner-first opening · ends at Philippi · author-voice (no em dash) · main @ 188631b`

## Exporter fix

Chapter/SC headers are now `Chapter N: Title` / `SC-…: Title` (no U+2014). The exporter regex was updated to accept colon (and legacy dash) separators with optional spaces. Act labels and DOCX chrome no longer use em dashes.

## Sanity

| Check | Result |
|-------|--------|
| Chapters in FULL | 1–34 (34) |
| Chapters in Golden | 14–19 (6) |
| U+2014 in export prose | **0** |
| Craft/metadata leaks (`POV:`, `G1:`, etc.) | **0** |

## Use

Tomorrow’s full read: prefer **FULL**. Golden remains the Ides sample only.

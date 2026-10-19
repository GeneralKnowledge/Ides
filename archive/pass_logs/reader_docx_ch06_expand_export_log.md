# Reader DOCX export (through Ch 6 expanded)

**Date:** 2026-10-19  
**Branch:** `cursor/reader-docx-ch06-expand-cb1d`  
**Commit:** `80d1cff` (main tip with Ch 1–6 expansions)  
**Source:** Expanded Ch 1–6 on `main` (PRs #104–#111) + prior human-voice tip Ch 7–34  
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
| `SHA256SUMS.txt` | Checksums under artifacts |

## Sanity

| Check | Result |
|------|--------|
| Chapters in FULL | 1–34 (34) |
| Chapters in Golden | 14–19 (6) |
| U+2014 in export prose | **0** |
| Craft/metadata leaks (`POV:`, etc.) | **0** |
| Ch 6 *perpetuo* gloss (“six months”) | present |

## Use

Prefer **FULL** for the cold read including expanded Ch 1–6. Golden remains the Ides sample only.

*End DOCX regen.*

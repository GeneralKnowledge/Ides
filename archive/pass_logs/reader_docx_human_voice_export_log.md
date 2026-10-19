# Reader DOCX export (human-voice tip Ch 12–34)

**Date:** 2026-10-19  
**Branch:** `cursor/reader-docx-human-voice-cb1d`  
**Source:** Assembled Ch 12–34 feel-passes (PRs #80–#102) on top of `main` (Ch 1–11 already merged)  
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

## Use

Prefer **FULL** for the cold read of the human-voice tip. Golden remains the Ides sample only.

*End DOCX regen.*

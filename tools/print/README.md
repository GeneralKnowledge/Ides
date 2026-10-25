# Book 1 print interior (hand-sewn hardcover)

Typesets Book 1 as a literary-novel interior at 129 × 198 mm and imposes it
two-up on A4 for duplex printing, folding into 16-page signatures and sewing.

```
pip install typst==0.15.0 pypdf python-docx     # Python 3.10+
sudo apt install poppler-utils                   # pdftotext, pdffonts, pdftoppm
python tools/print/build_book1_print.py          # writes build/print/ (about 2–3 minutes)
```

Options: `--out DIR`, `--signature 12` (pages per signature, multiple of 4),
`--no-fit` (skip copyfitting; faster, some pages run a line short),
`--no-collation-marks`.

The build reads `drafts/book1/` (through the chapter parser in
`tools/export_book1_docx.py`, so the print text and the DOCX reading copy strip
the same metadata) and never writes to it. It stops, writing nothing, if a
font, the manuscript or a tool is missing, or if any check that guards the text
fails: the words read back out of the PDF must equal the manuscript's, in
order; every character must have a glyph; fonts must be embedded; every page
must be the right size; and every half of every imposed A4 side must carry the
text of the reading page it should.

## What it writes (`build/print/`, not tracked)

| Path | What |
|------|------|
| `README.txt` | Map of the package |
| `Ides_Book1_interior_reading-order_129x198mm.pdf` | Master proof, reading order, trim size |
| `test/` | Duplex calibration sheet, a test signature (imposed) and the same pages in reading order: print these first |
| `signatures/sigNN_pdf-pages_AAA-BBB.pdf` | One imposed A4 PDF per signature |
| `Ides_Book1_imposed_A4_all-signatures.pdf` | All signatures, one file |
| `Ides_Book1_printing-and-binding-instructions.pdf` | Printer settings, folding, sewing, trimming |
| `Ides_Book1_sewing-jig_A4.pdf` | Punching jig: kettle and tape stations for sewing on three tapes |
| `Ides_Book1_specification.pdf`, `spec.json` | Trim, pages, signatures, type, margins, thickness and board estimates |
| `Ides_Book1_proofing-report.pdf` | Checks run, concerns, missing metadata, decisions, limitations |
| `source/` | The exact Typst source compiled: template, parsed manuscript (`content.json`), metadata, copyfitting (`adjust.json`) |

## Files here

| File | Role |
|------|------|
| `build_book1_print.py` | The one command: parse, typeset, fit, check, impose, document |
| `book1.typ` | Interior design: page, type, openings, running heads, folios, front matter |
| `meta.json` | Title, author and the bibliographic fields still to be supplied (null = left off the page) |
| `content.py` | Manuscript to structured runs (italic, small caps) |
| `fit.py` | Copyfitting: fills pages left short by widow/orphan control by setting one paragraph a hair tighter or looser |
| `impose.py` | Signature plan and A4 imposition |
| `jig.typ` | Sewing jig (station positions) |
| `marks.typ` | Trim, fold and collation marks and sheet labels (all in the trimmed-off strips); calibration sheet |
| `qa.py` | Read-back checks |
| `docs.py` | Specification, instructions and proofing report |
| `fonts/` | EB Garamond Regular and Italic (OTF) with `OFL.txt` |

## Fonts and licences

EB Garamond (Octavio Pardo, after Georg Duffner) is under the SIL Open Font
License 1.1 (`fonts/OFL.txt`), which allows embedding in PDFs and
redistribution with the licence. The build checks the font files against
recorded SHA-256 digests and uses no system fonts.

## Imposition in one paragraph

Each A4 sheet, printed landscape on both sides and folded once across its
width, carries four book pages; four sheets nest into a 16-page signature.
Each book page sits with its spine edge on the fold, centred head to tail;
19.5 mm at the fore-edge and 6 mm at head and tail are trimmed after sewing.
For sheet *k* (0 = outside) of an *n*-page signature: front = *n − 2k* | *2k + 1*,
back = *2k + 2* | *n − 2k − 1*. Print duplex, flip on short edge, 100 %.

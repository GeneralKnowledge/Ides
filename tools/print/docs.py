"""Specification sheet, printing and binding instructions, and proofing report.

Each is written as Typst markup and compiled to an A4 PDF. Values that come
from the manuscript or the build go in through `t()`, as Typst strings, so no
manuscript text is ever read as markup.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import impose
import qa

# Physical assumptions for estimates. Calipers are typical for uncoated office
# and book papers; measure your own stack before cutting boards.
CALIPER = {80: 0.100, 90: 0.115}  # mm per leaf
THREAD_SWELL = (0.15, 0.25)  # mm added at the spine per signature by the sewing thread
ENDPAPER_LEAVES = 4  # one folded sheet at each end
ENDPAPER_CALIPER = 0.15  # mm per leaf, ~120 gsm
BOARD = 2.0  # mm greyboard
SQUARE = 3.0  # mm board overhang at head, tail and fore-edge
JOINT = 6.0  # mm gap between spine stiffener and board (about 2 x board + 2)
TURN_IN = 18.0  # mm cover material turned over the board edges


def t(s: object) -> str:
    """A Typst string literal in markup: never interpreted as markup."""
    return "#{" + json.dumps(str(s), ensure_ascii=False) + "}"


def roman(n: int) -> str:
    vals = [(10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out


@dataclass
class Info:
    meta: dict
    stamp: dict
    total: int
    padded: int
    sigs: list
    main_start: int
    test: object
    layout: qa.LayoutReport
    checks: list
    words: int
    signature: int
    concerns: list
    folio: Callable[[int], str]
    collation: bool
    reading_name: str
    fitted: object = None


PREAMBLE = r"""
#set page(paper: "a4", margin: (x: 22mm, top: 20mm, bottom: 22mm),
  footer: context align(center, text(size: 8.5pt, counter(page).display())))
#set text(font: "EB Garamond", size: 10.5pt, lang: "en", region: "GB", number-type: "lining")
#set par(justify: false, leading: 0.55em, spacing: 0.9em)
#set heading(numbering: none)
#show heading.where(level: 1): it => block(below: 1em, text(size: 17pt, weight: "regular", it.body))
#show heading.where(level: 2): it => block(above: 1.4em, below: 0.7em, text(size: 12.5pt, weight: "regular", smallcaps(all: true, it.body)))
#show heading.where(level: 3): it => block(above: 1em, below: 0.5em, text(size: 10.5pt, style: "italic", weight: "regular", it.body))
#set table(stroke: 0.4pt + luma(70%), inset: (x: 5pt, y: 4pt))
#show table: set par(justify: false)
#show table: set text(size: 9.5pt)
"""


def table(rows: list[list[str]], cols: str = "(auto, 1fr)", header: bool = False) -> str:
    cells = []
    for i, r in enumerate(rows):
        for c in r:
            cells.append(f"[*{c}*]" if header and i == 0 else f"[{c}]")
    return f"#table(columns: {cols}, " + ", ".join(cells) + ")\n"


def bullets(items: list[str]) -> str:
    return "".join(f"- {i}\n" for i in items) + "\n"


def stamp_line(i: Info) -> str:
    s = i.stamp
    dirty = " · UNCOMMITTED MANUSCRIPT CHANGES" if s["dirty"] == "yes" else ""
    return t(f"Manuscript revision {s['manuscript']} ({s['manuscript_date']}) · source digest {s['digest']} · "
             f"built {s['generated']}{dirty}")


def thickness(i: Info) -> dict:
    leaves = i.padded // 2
    n = len(i.sigs)
    end = ENDPAPER_LEAVES * ENDPAPER_CALIPER
    out = {"leaves": leaves, "signatures": n, "endpapers": end}
    for gsm, c in CALIPER.items():
        paper = leaves * c
        out[gsm] = {
            "paper": paper,
            "fore_edge": paper + end,
            "spine": (paper + end + n * THREAD_SWELL[0], paper + end + n * THREAD_SWELL[1]),
        }
    return out


def sig_table(i: Info) -> list[list[str]]:
    rows = [["Signature", "Sheets", "PDF pages", "Printed folios", "File"]]
    for s in i.sigs:
        last = min(s.end, i.total)
        fol = f"{i.folio(s.start)}–{i.folio(last)}"
        blanks = s.end - i.total
        pages = f"{s.start}–{s.end}" + (f" ({blanks} blank pad page{'s' if blanks > 1 else ''})" if blanks > 0 else "")
        rows.append([str(s.number), str(s.sheets), t(pages), t(fol),
                     t(f"sig{s.number:02d}_pdf-pages_{s.start:03d}-{s.end:03d}.pdf")])
    return rows


def sig_plan_sentence(i: Info) -> str:
    sizes = [s.pages for s in i.sigs]
    full = sizes.count(i.signature)
    rest = [x for x in sizes if x != i.signature]
    s = f"{len(sizes)} signatures: {full} of {i.signature} pages"
    if rest:
        s += " and " + " + ".join(f"{x}" for x in rest) + " pages at the end"
    return s


# ---- Specification sheet ----------------------------------------------------------

def spec(i: Info) -> str:
    th = thickness(i)
    g = qa.G
    lo80, hi80 = th[80]["spine"]
    lo90, hi90 = th[90]["spine"]
    spine_lo, spine_hi = lo80, hi90
    stiff = (spine_lo + 2 * BOARD, spine_hi + 2 * BOARD)
    board_w = 129 + SQUARE - JOINT
    board_h = 198 + 2 * SQUARE
    cover_w = (2 * board_w + 2 * JOINT + stiff[0] + 2 * TURN_IN, 2 * board_w + 2 * JOINT + stiff[1] + 2 * TURN_IN)
    m = i.meta
    rows = [
        ["Title", t(f"{m['title']}, {m['volume']}")],
        ["Author", t(m["author"])],
        ["Source", stamp_line(i)],
        ["Finished trim size", "129 × 198 mm (portrait)"],
        ["Total interior pages", t(f"{i.total} typeset pages ({roman(i.main_start - 1)} front-matter pages + "
                                   f"{i.total - i.main_start + 1} main pages), padded to {i.padded} for printing")],
        ["Leaves", t(f"{th['leaves']} leaves (one leaf = two pages)")],
        ["Signatures", t(sig_plan_sentence(i))],
        ["Pages per signature", t(f"{i.signature} (4 A4 sheets, folded once and nested); see the signature table")],
        ["Printing", "A4 landscape, two book pages per side, duplex, flip on short edge, 100 % scale"],
        ["Paper (assumed)", "80–90 gsm uncoated, white or natural; short grain preferred (grain parallel to the 210 mm edge, so it runs along the spine)"],
        ["Words", t(f"{i.words:,} in the reading text")],
    ]
    type_rows = [
        ["Typeface", "EB Garamond (Octavio Pardo / Georg Duffner), SIL Open Font License 1.1; Regular and Italic, embedded as subsets"],
        ["Body", t(f"{g.size} pt on {g.lh} pt baseline grid, {g.lines} lines per full page, justified, "
                   "old-style figures, English hyphenation, hanging punctuation")],
        ["Measure", t(f"{g.text_w / qa.MM:.1f} mm (about 62–66 characters per line)")],
        ["Paragraphs", "1 em first-line indent; first paragraph of a chapter or scene flush, no space between paragraphs"],
        ["Chapter openings", "Recto; sunk 9 grid lines; “Chapter N” in letterspaced small caps, title 16 pt, first three words in small caps"],
        ["Scene breaks", "The scene titles from the manuscript, in letterspaced small caps, one blank grid line above and below"],
        ["Part pages", "Five act pages, recto, blank verso; no running head or folio"],
        ["Running heads", "Centred, 8.25 pt letterspaced small caps: book title on versos, chapter title on rectos; none on openings or blanks"],
        ["Folios", "Centred at the foot, 9.5 pt; roman in front matter (contents only), arabic from the Prologue (page 1); none on blanks, part pages, half-title, title and copyright pages"],
        ["Widows and orphans", "None: prevented by the typesetter and checked from the paragraph positions"],
        ["Copyfitting", "Where widow control left a page a line short, one paragraph on that page is set a hair tighter or looser (at most ±0.018 em letterspacing) so the page fills; see the proofing report"],
    ]
    margin_rows = [
        ["Inner (gutter)", "19.0 mm from the spine fold to the text"],
        ["Outer (fore-edge)", "15.0 mm after trimming"],
        ["Top", "17.5 mm to the top of the text (running head sits 6.5 mm above it)"],
        ["Bottom", t(f"{(198 - 17.5 - g.text_h / qa.MM):.1f} mm below the last line (folio inside it)")],
        ["Text block on the page", t(f"{g.text_w / qa.MM:.1f} × {g.text_h / qa.MM:.1f} mm")],
        ["On the A4 sheet", "Spine edge of each page on the sheet’s centre fold; 19.5 mm fore-edge and 6 mm head and tail strips are trimmed off after sewing"],
    ]
    est_rows = [
        ["Basis", t(f"{th['leaves']} leaves; caliper 0.100 mm/leaf (80 gsm) or 0.115 mm/leaf (90 gsm); "
                    f"endpapers {ENDPAPER_LEAVES} leaves × {ENDPAPER_CALIPER} mm; sewing swell "
                    f"{THREAD_SWELL[0]}–{THREAD_SWELL[1]} mm per signature × {th['signatures']} signatures")],
        ["Text block at fore-edge", t(f"≈ {th[80]['fore_edge']:.1f} mm (80 gsm) / ≈ {th[90]['fore_edge']:.1f} mm (90 gsm)")],
        ["Text block at spine, pressed", t(f"≈ {lo80:.1f}–{hi80:.1f} mm (80 gsm) / ≈ {lo90:.1f}–{hi90:.1f} mm (90 gsm)")],
        ["Spine width (spine stiffener, flat back)", t(f"≈ {stiff[0]:.0f}–{stiff[1]:.0f} mm = text block at spine + 2 × board thickness ({BOARD} mm)")],
        ["Rounded and backed spine", "Measure the rounded spine with a paper strip after backing; cut the stiffener to that arc length"],
        ["Cover boards (2 mm greyboard)", t(f"{board_h:.0f} mm high (198 + 2 × {SQUARE:.0f} mm squares) × {board_w:.0f} mm wide (129 + {SQUARE:.0f} mm square − {JOINT:.0f} mm joint allowance)")],
        ["Joint gap", t(f"≈ {JOINT:.0f} mm each side between stiffener and board (about 2 × board thickness + 2 mm)")],
        ["Cover material", t(f"≈ {cover_w[0]:.0f}–{cover_w[1]:.0f} × {board_h + 2 * TURN_IN:.0f} mm including {TURN_IN:.0f} mm turn-ins")],
        ["Endpapers", "Each a folded sheet 258 × 198 mm (two leaves of 129 × 198), grain parallel to the fold; cut from A4 or larger"],
    ]
    return PREAMBLE + f"""
= Book specification
{t(f"{i.meta['title']}, {i.meta['volume']}")} · hand-sewn hardcover interior

== The book
{table(rows)}
== Typography
{table(type_rows)}
== Margins
{table(margin_rows)}
== Signatures
{table(sig_table(i), "(auto, auto, auto, auto, 1fr)", header=True)}
Blank pad pages (if any) are added at the very end of the last signature; they sit after the cast list as the conventional blank leaves before the rear endpaper.

== Estimates: not final
#block(fill: luma(94%), inset: 8pt, radius: 2pt, width: 100%)[*These are estimates.* Paper caliper varies by brand and humidity, and sewing, gluing and pressing change the spine. Measure the actual sewn, glued and pressed text block before cutting boards or the spine stiffener; recompute with the formulas below.]

{table(est_rows)}
"""


# ---- Printing, folding and sewing --------------------------------------------------

def instructions(i: Info) -> str:
    last = i.sigs[-1]
    tail = [s for s in i.sigs if s.pages != i.signature]
    tail_text = (
        "All signatures are " + str(i.signature) + " pages."
        if not tail else
        "The last " + ("signature is" if len(tail) == 1 else f"{len(tail)} signatures are")
        + " shorter: " + ", ".join(f"signature {s.number} has {s.pages} pages ({s.sheets} sheets)" for s in tail)
        + f". This avoids a single-sheet signature, which sews poorly."
    )
    blanks = last.end - i.total
    return PREAMBLE + f"""
= Printing, folding and sewing
{t(f"{i.meta['title']}, {i.meta['volume']}")} · {stamp_line(i)}

#block(fill: luma(94%), inset: 8pt, radius: 2pt, width: 100%)[*Nothing here has been physically printed.* The files were checked programmatically and by rendering them, but paper handling, duplex registration, fold accuracy and the opening of the sewn block are untested. Print the calibration sheet and the test signature first, and check them against the list in step 3.]

== What is in the package
{table([
    ["File", "Use"],
    [t(i.reading_name), "Master proof in reading order at the finished size. Read and check typography here. Do not print this for binding."],
    [t(f"test/TEST_duplex-calibration-sheet_A4.pdf"), "One sheet. Print first to confirm 100 % scale, duplex flip and front/back registration."],
    [t(f"test/TEST_signature-{i.test.number:02d}_imposed_A4_print-me-first.pdf"), t(f"Signature {i.test.number} of the book (PDF pages {i.test.start}–{i.test.end}), imposed. If it passes it goes into the book; it holds a chapter opening, scene breaks, dialogue and italics.")],
    [t(f"test/TEST_reading-order_pdf-pages_{i.test.start:03d}-{i.test.end:03d}.pdf"), "The same 16 pages in reading order, to compare with the folded test signature."],
    [t("signatures/sigNN_pdf-pages_AAA-BBB.pdf"), t(f"One file per signature, {len(i.sigs)} files. Print one at a time.")],
    [t("Ides_Book1_imposed_A4_all-signatures.pdf"), "All signatures in one file, in order, for printing in a single run if your printer is reliable."],
    [t("single-sided/sigNN_…_side-A_fronts.pdf and …_side-B_backs.pdf"), "For printers without two-sided printing: print side A, put the sheets back in, print side B. See section 2a."],
    ["Spec, report and these instructions", "Book specification (sizes, estimates), proofing report (checks and open questions)."],
], "(auto, 1fr)", header=True)}
"PDF pages" means page numbers in the reading-order PDF, counting the half-title as 1. The printed folios differ: the Prologue is printed page 1, which is PDF page {i.main_start}.

== 1. Paper
- A4, 80–90 gsm, uncoated. Use one ream for the whole book so caliper and colour match.
- *Grain.* The fold should run with the grain. Each sheet is folded across its width, so the grain should run parallel to the 210 mm edge ("short grain"). Most office A4 is long grain: it still works, but the folds are stiffer and the pages turn less freely. Test: bend a sheet both ways without creasing; it bends more easily along the grain.
- Fan the paper and print in a dry room; let printed sheets rest flat for an hour before folding.

== 2. Printer settings
- *Scale: Actual size / 100 %.* Turn off “Fit to page”, “Shrink oversized pages” and any booklet mode. The files are already imposed.
- *Orientation: Landscape* (or Auto-rotate). Each PDF page is A4 landscape, 297 × 210 mm.
- *Two-sided: flip on short edge.* (Some drivers call it “short-edge binding” or “Tablet”.)
- Black or greyscale, plain paper, normal or best quality. Disable “toner save”.
- Each signature PDF has 2 pages per A4 sheet: sheet 1 front, sheet 1 back, sheet 2 front, and so on. Print the whole file duplex.

== 2a. Printing without duplex
The `single-sided/` folder splits each signature into two files: *side A* (the fronts of sheets 1, 2, 3, 4) and *side B* (their backs, in the same order). They hold exactly the pages you get by printing a signature file’s odd pages, then its even pages.
+ Print side A, one-sided, at 100 %, landscape.
+ Take the printed sheets and put them back in the tray so the blank side will be printed and the sheets keep the same orientation as a short-edge flip: turn the stack over from left to right, so the printed side faces the opposite way and the same short edge leads. Mark a test sheet with a pencil arrow first to learn your printer’s habit.
+ Make sure sheet 1 will be printed first. If your printer delivers the A sheets in reverse order, either reverse the stack or tick “Reverse order” in the print dialog for side B.
+ Print side B. Check the label in the margin strip of each sheet: the signature and sheet number on the front and back must match, and BACK must read the right way up behind FRONT.

== 3. Calibration and test signature
+ Print `TEST_duplex-calibration-sheet_A4.pdf` duplex.
  - Measure the grey bar: it must be exactly 100 mm. If it is shorter, scaling is on.
  - Turn the sheet over left to right: “BACK” should read the right way up. If it is upside down, change the flip setting.
  - Hold it to a window: the crosses on both sides should coincide. Note any offset; under about 1 mm is fine. A consistent offset can be corrected in the printer’s duplex alignment settings.
+ Print the test signature duplex, then fold and nest it as in step 4.
+ Check, with the reading-order test PDF beside you:
  - The page numbers run in order through the folded signature, with no page upside down or missing.
  - The spine-side margins look equal on facing pages and the text is square to the fold.
  - Running heads: the book title on left-hand pages, the chapter title on right-hand pages; none on the chapter opening.
  - Trim marks: the short lines in the outer strips mark the head and tail trim; the 129 mm page width runs from the fold to the fore-edge trim line.
  - Open the nested signature flat: the gutter (19 mm from fold to text) should feel generous. The sewn book will lose a few millimetres of it.
  - Type size and darkness are comfortable on your paper.
+ Only when these pass, print the rest of the book.

== 4. Folding and nesting
- Each sheet’s outer strip carries a small label: signature, sheet, FRONT or BACK, and the pages on it. These strips are trimmed off later.
- Fold each sheet in half across its width, *FRONT side outside*, aligning the corners exactly and creasing with a bone folder. The FRONT side of sheet 1 shows the signature’s first page on the right and its last page on the left.
- Nest the folded sheets: sheet 2 inside sheet 1, sheet 3 inside sheet 2, sheet 4 innermost. The centre spread is the innermost sheet’s BACK side.
- Check the page order, then press the signature under boards and weight overnight.
- {t(tail_text)}{t(f" The last {blanks} page(s) of signature {last.number} are deliberately blank." if blanks else "")}
- {"Collation marks: the outer sheet of each signature carries a small black bar on the fold, one step lower per signature. Gathered in order, the bars form a diagonal staircase on the spine; a break in the staircase shows a missing or misplaced signature. The bar is 1.6 mm wide, so a sliver of up to 0.8 mm sits at the very gutter of each signature’s first and last page, inside the sewn fold. Rebuild with `--no-collation-marks` if you would rather not have it." if i.collation else "Collation marks are switched off; number the signatures in pencil on the spine fold before gathering."}

== 5. Sewing
- Gather the signatures in order (signature 1 on top when the book lies face up) and knock them square at the spine and head.
- Print `Ides_Book1_sewing-jig_A4.pdf` at 100 % and glue it to card: it marks the kettle stations 21 mm from head and tail (15 mm inside the trim lines, so trimming never cuts the thread) and three 12 mm tapes at 63, 105 and 147 mm, with a hole just outside each tape edge.
- Pierce each signature through the fold from the inside, using the jig.
- Sew all along (linen thread, e.g. 18/3 or 25/3, waxed), on tapes or cords if you are using them, with kettle stitches at head and tail. Keep tension even so the spine does not swell more than needed.
- Add the endpapers (tipped on, or sewn on as the first and last signatures).

== 6. Gluing, trimming and casing
- Knock up the spine, clamp, and glue with PVA or bookbinding adhesive; work it between the signatures. Let it dry.
- *Trim* to 129 × 198 mm: 19.5 mm off the fore-edge and 6 mm off head and tail. The marks on the sheets show the lines; measure 129 mm from the spine fold for the fore-edge. A plough, guillotine or a very sharp knife with a steel straightedge and many light passes all work. Check the trimmed size against the specification.
- If you decide not to trim, the text block will be about 148.5 × 210 mm with a wide, uneven fore-edge margin; the typesetting assumes trimming.
- Round and back if you wish, then line: mull (super), headbands, kraft paper.
- Measure the pressed spine before cutting boards and the spine stiffener. The specification gives estimates and formulas.
- Make the case, case in, and press overnight with boards at the joints.

== 7. If you rebuild
`python tools/print/build_book1_print.py` regenerates everything from the manuscript; see `tools/print/README.md`. Signature boundaries move if the page count changes, so reprint whole signatures, never single sheets from an older build.
"""


# ---- Proofing report ---------------------------------------------------------------

def fit_text(i: Info) -> str:
    f = i.fitted
    if f is None:
        return "Copyfitting was switched off for this build (--no-fit)."
    levels = {}
    for v in f.adjust.values():
        levels[v] = levels.get(v, 0) + 1
    desc = {-2: "tighter (−0.015 em letterspacing, 90 % word space)",
            -1: "slightly tighter (−0.008 em, 95 %)",
            1: "slightly looser (+0.010 em, 108 %)",
            2: "looser (+0.018 em, 115 %)"}
    parts = "; ".join(f"{n} {desc[k]}" for k, n in sorted(levels.items()))
    return t(f"As a compositor would, the build filled such pages by setting one paragraph on the page a fraction "
             f"tighter or looser, keeping a change only if the page then filled: {len(f.adjust)} of the book’s "
             f"paragraphs are adjusted ({parts}). Only letter and word spacing change, never the words; the list is in "
             f"source/adjust.json, by section and paragraph number.")


def report(i: Info) -> str:
    lay = i.layout
    m = i.meta
    missing = [k for k in ("copyright_line", "rights_statement", "publisher", "edition_statement", "isbn")
               if not m.get(k)]
    labels = {
        "copyright_line": "Copyright line (e.g. holder and year) for the copyright page",
        "rights_statement": "Rights statement (e.g. “All rights reserved”), if wanted",
        "publisher": "Publisher or imprint name for the title page, if any",
        "edition_statement": "Edition or printing statement (e.g. “First edition, privately printed, 2026”), if wanted",
        "isbn": "ISBN (none needed for a private, unsold copy)",
    }

    def listing(items: list[str], none: str, cap: int = 60) -> str:
        if not items:
            return none + "\n\n"
        more = f"- {t(f'… and {len(items) - cap} more')}\n" if len(items) > cap else ""
        return bullets([t(x) for x in items[:cap]]) + more + "\n"

    confirmed: list[str] = []
    return PREAMBLE + f"""
= Proofing report
{t(f"{m['title']}, {m['volume']}")} · {stamp_line(i)}

== Summary
The full manuscript (Utica prologue, Chapters 1–36, historical note and cast list) is typeset in {t(i.total)} pages at 129 × 198 mm and imposed as {t(sig_plan_sentence(i))}. Every check that guards the text passed: the words extracted from the PDF match the manuscript exactly, in order. The interior has *not* been printed, folded or sewn; physical checks are listed at the end.

== Checks performed
{table([["Check", "Result"]] + [[t(c), t(r)] for c, r in i.checks], "(1fr, auto)", header=True)}
Also checked: no typesetting warnings; font files match their recorded checksums; every running head clears the text; no line falls below the text area; versos carry the book title and rectos the chapter title; the imposition was checked against an independent walk through the folded, nested sheets; and each half of every A4 side was read back and compared with its reading-order page.

== Confirmed errors
{listing(confirmed, "None found. The build stops on any text difference, missing glyph, unembedded font, wrong page size, misplaced page furniture or imposition mismatch, so a delivered package has none of these.")}
== Possible concerns: layout
=== Widows and orphans
{listing(lay.widows + lay.orphans, "None detected (lines read back from the PDF: no paragraph’s last line alone at the top of a page, no first line alone at the foot).")}
=== Short pages and copyfitting
Keeping widows and orphans off the page means moving a line over, which leaves the page above it a line short of the 33-line grid. {fit_text(i)} {t(f"{len(lay.short_pages)} of {i.total - i.main_start + 1} main pages still run short")}, where no paragraph on the page could gain or lose a line within those limits. Look at a few in the proof; the remedy for any that bother you is a manual adjustment, never a change to the text.

{listing(lay.short_pages, "None.", cap=80)}
=== Chapter endings with three lines or fewer on the last page
{listing(lay.stub_endings, "None.")}
=== Hyphenation and spacing
{t(f"{lay.hyphen_lines} lines end in a hyphen ({lay.hyphen_lines / max(lay.body_lines, 1):.1%} of {lay.body_lines:,} text lines; this count includes lines broken at a real hyphen).")} Three or more consecutive hyphenated lines:

{listing(lay.hyphen_ladders, "None.")}
Loose lines (average word space above 0.5 em):

{listing(lay.loose_lines, "None.")}
== Possible concerns: source text
Reported only; nothing was changed. Patterns searched: doubled words, double spaces, space before punctuation, straight quotes, hyphens used as dashes, stray asterisks, and paragraphs whose opening and closing quotation marks do not balance (often legitimate: speech that runs on into the next paragraph leaves its quote open).

{listing(i.concerns, "None found.")}
== Missing information for you to supply
Edit `tools/print/meta.json` and rebuild. Nothing below was invented; the pages simply leave it out.
{bullets([labels[k] for k in missing])}
- No dedication, epigraph or acknowledgements exist in the manuscript, so none are set. Add them in `meta.json` if you want them (`dedication`, `epigraph`).

== Decisions taken (all reversible)
- *Title page:* “The Ides of March”, “Book 1” and “Reuben Dennison”, as on the existing DOCX reading copy.
- *Copyright page:* carries only “Set in EB Garamond” and a line giving the manuscript revision the interior was set from, so a printed copy can be matched to the source. Set `show_revision_line` to false in `meta.json` to drop it.
- *Contents:* included; the book has five acts and 36 titled chapters, which a reader of a book this long will use.
- *Scene titles:* the manuscript titles every scene, and the DOCX reading copy shows them, so they are kept, set small and quiet. If you would prefer unnamed breaks (an ornament or a line space), that is a one-line change in `book1.typ` and a decision for you, since it removes words the reader currently sees.
- *Act pages:* one recto per act, as in the DOCX reading copy.
- *Recto starts:* every chapter, act page and back-matter section starts on a right-hand page; this adds blank versos, typical for a hardcover.
- *Chapter 30’s three numbered lines* are set as a short indented list, exactly as written.
- *Back matter:* the historical note and cast list follow Chapter 36. Bold labels in them (names, sub-points) are set in small caps; list bullets become hanging indents. The map brief is for a cartographer and is not printed.
- *Excluded, as in the DOCX copy:* scene cards, POV/date/canon lines, continuity notes and other metadata; the DOCX’s “End of Book 1 full review export” line.
- *Trim size kept at 129 × 198 mm.* It fits a folded A4 sheet (148.5 × 210 mm) with a 19.5 mm fore-edge trim and 6 mm head and tail trims; the spine edge sits on the fold, so the full 19 mm gutter survives.

== Conversion notes
- Markdown `*italic*` became italic; nothing else in the chapter text carries markup. Curly quotes, apostrophes, ellipses and the dagger (†) come straight from the source and are all in the font.
- Smart-quote substitution is off for the text: the source already uses typographic quotes, and nothing is retyped.
- Line-end hyphenation is the only change to word shapes in the PDF; the text comparison rejoins hyphenated words before comparing.

== Limitations
- *Not physically tested.* Printing, duplex registration, folding accuracy, paper grain behaviour, sewing and the opening of the finished block have not been tested. Treat the test signature as the first real proof.
- *Creep is not compensated.* With four nested sheets of 80–90 gsm paper, the inner sheet’s fore-edge sits about 0.3 mm proud of the outer one; trimming removes it and the text shifts by under 0.3 mm, which is invisible. Thicker paper or larger signatures would need compensation.
- *Printer margins:* most printers cannot print within 3–5 mm of the sheet edge. Only trim and fold marks sit there; if they are clipped, measure instead (6 mm from head and tail, 129 mm from the fold).
- Visual inspection was done from rendered images, which cannot show the colour, weight or show-through of real paper.

== What you must check physically before printing the whole book
+ Calibration sheet: 100 mm bar measures 100 mm; back reads upright after a left-to-right turn; crosses coincide within about 1 mm.
+ Test signature folds to a correctly ordered 16-page section with consistent margins and no rotated pages.
+ The text block's position looks right after trimming a test signature (or after marking the trim lines on it).
+ Gutter clearance when the sewn signature is opened.
+ Show-through and type darkness on your paper.
+ After sewing and pressing: measure the actual spine thickness before cutting boards and the spine stiffener.
"""


def write_all(i: Info, src: Path, out: Path, compile_typst, stamp) -> None:
    docs = {
        "Ides_Book1_specification.pdf": spec(i),
        "Ides_Book1_printing-and-binding-instructions.pdf": instructions(i),
        "Ides_Book1_proofing-report.pdf": report(i),
    }
    for name, markup in docs.items():
        f = src / (Path(name).stem + ".typ")
        f.write_text(markup, encoding="utf-8")
        compile_typst(f, out / name, stamp)
    th = thickness(i)
    spec_json = {
        "title": i.meta["title"], "volume": i.meta["volume"], "author": i.meta["author"],
        "manuscript": i.stamp, "trim_mm": [129, 198], "pages": i.total, "padded_pages": i.padded,
        "front_matter_pages": i.main_start - 1,
        "signatures": [{"number": s.number, "pdf_pages": [s.start, s.end], "sheets": s.sheets} for s in i.sigs],
        "test_signature": i.test.number,
        "estimates_mm_not_final": {
            "text_block_spine_80gsm": th[80]["spine"], "text_block_spine_90gsm": th[90]["spine"],
        },
    }
    (out / "spec.json").write_text(json.dumps(spec_json, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "README.txt").write_text(
        f"""The Ides of March, Book 1 · print package
{i.stamp['manuscript']} ({i.stamp['manuscript_date']}), built {i.stamp['generated']}

Start here:
  Ides_Book1_printing-and-binding-instructions.pdf   how to print, fold and sew
  test/                                              print these first
Then:
  {i.reading_name}   master proof, reading order, 129 x 198 mm
  signatures/                                        one imposed A4 PDF per signature (duplex)
  single-sided/                                      side A (fronts) and side B (backs) per signature
  Ides_Book1_imposed_A4_all-signatures.pdf           all signatures in one file
  Ides_Book1_specification.pdf                       sizes, margins, estimates
  Ides_Book1_sewing-jig_A4.pdf                       punching jig for sewing on three tapes
  Ides_Book1_proofing-report.pdf                     checks and open questions
  source/                                            the Typst source this build compiled
  qa_previews/                                       low-resolution renders used in checking

Nothing here has been physically printed. Print at 100 %, duplex, flip on short edge.
""", encoding="utf-8")

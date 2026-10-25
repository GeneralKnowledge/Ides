#!/usr/bin/env python3
"""Build the Book 1 print package for a hand-sewn hardcover.

    pip install typst==0.15.0 pypdf python-docx    # plus poppler-utils
    python tools/print/build_book1_print.py         # writes build/print/
    python tools/print/build_book1_print.py --out DIR --signature 16

Produces the reading-order interior at trim size, a test signature, every
signature imposed two-up on A4 for duplex printing, a duplex calibration
sheet, and the specification sheet, printing instructions and proofing
report. Reads the manuscript (drafts/book1/) and never writes to it. Stops
with an error, and writes no package, if an input is missing or a check that
guards the text fails.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

FONT_DIR = HERE / "fonts"
FONTS = {
    "EBGaramond-Regular.otf": "8d618a6bc6e1f4444e1990c39770a62ccbc29394e57afcc58acd530c16489275",
    "EBGaramond-Italic.otf": "296feee09f6fa157f913cf3d75460b5e282b3c43dff4ddffbcc5c1a924f4fd14",
}
TYPST_VERSION = "0.15.0"
READING_NAME = "Ides_Book1_interior_reading-order_129x198mm.pdf"


def fail(msg: str) -> None:
    raise SystemExit(f"BUILD FAILED: {msg}")


def preflight() -> None:
    for mod in ("typst", "pypdf", "docx"):
        try:
            importlib.import_module(mod)
        except ImportError:
            fail(f"Python package '{mod}' missing (pip install typst=={TYPST_VERSION} pypdf python-docx)")
    import typst

    if typst.__version__ != TYPST_VERSION:
        print(f"warning: typst {typst.__version__} installed; built and checked with {TYPST_VERSION}")
    for tool in ("pdftotext", "pdffonts", "pdftoppm"):
        if not shutil.which(tool):
            fail(f"'{tool}' not found (install poppler-utils)")
    for name, digest in FONTS.items():
        f = FONT_DIR / name
        if not f.exists():
            fail(f"font missing: {f.relative_to(ROOT)}")
        if hashlib.sha256(f.read_bytes()).hexdigest() != digest:
            fail(f"font changed: {f.relative_to(ROOT)} does not match its recorded checksum")
    if not (FONT_DIR / "OFL.txt").exists():
        fail("fonts/OFL.txt (font licence) missing")


def compile_typst(src: Path, out: Path, stamp: datetime, inputs: dict | None = None) -> None:
    import typst

    _, warnings = typst.compile_with_warnings(
        str(src), output=str(out), root=str(src.parent), font_paths=[str(FONT_DIR)],
        ignore_system_fonts=True, timestamp=int(stamp.timestamp()), sys_inputs=inputs or {},
    )
    if warnings:
        fail(f"typst warnings compiling {src.name}: {warnings}")


def query_marks(src: Path) -> list[dict]:
    import typst

    return json.loads(typst.query(
        str(src), "<pmark>", field="value", root=str(src.parent), font_paths=[str(FONT_DIR)],
        ignore_system_fonts=True,
    ))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", type=Path, default=ROOT / "build" / "print")
    ap.add_argument("--signature", type=int, default=16, help="pages per signature (multiple of 4)")
    ap.add_argument("--no-fit", action="store_true",
                    help="skip copyfitting (pages may run a line short)")
    ap.add_argument("--no-collation-marks", action="store_true",
                    help="leave the stepped marks off the spine folds")
    args = ap.parse_args()

    preflight()
    import content
    import docs
    import impose
    import qa
    import export_book1_docx as ex
    from pypdf import PdfReader, PdfWriter

    files, data = content.build()
    meta = json.loads((HERE / "meta.json").read_text(encoding="utf-8"))
    stamp = ex.source_stamp(files)
    if stamp["dirty"] == "yes":
        print("warning: drafts/book1 has uncommitted changes; the package is stamped as such")
    stamp_date = datetime.strptime(stamp["manuscript_date"], "%Y-%m-%d").replace(tzinfo=timezone.utc) \
        if stamp["manuscript_date"] != "unknown" else datetime.now(timezone.utc)

    out = args.out
    work = Path(tempfile.mkdtemp(prefix="ides-print-"))
    src = work / "source"
    src.mkdir()
    for f in ("book1.typ", "marks.typ"):
        shutil.copy(HERE / f, src / f)
    (src / "content.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    (src / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    (src / "build.json").write_text(json.dumps(stamp, indent=2), encoding="utf-8")

    # ---- A. Reading-order interior -------------------------------------------------
    reading = work / READING_NAME
    (src / "adjust.json").write_text("{}")
    fitted = None
    if not args.no_fit:
        import fit

        print("Copyfitting short pages")
        fitted = fit.fit(src, reading, data, lambda: compile_typst(src / "book1.typ", reading, stamp_date),
                         lambda: query_marks(src / "book1.typ"))
    compile_typst(src / "book1.typ", reading, stamp_date)
    total = len(PdfReader(str(reading)).pages)
    print(f"Typeset {total} pages")

    hard: list[str] = []  # anything here stops the build
    checks: list[tuple[str, str]] = []  # (check, result) for the report

    bad = qa.check_sizes(reading, qa.G.trim_w, qa.G.trim_h)
    hard += [f"page size: {b}" for b in bad]
    checks.append(("Every page is 129 × 198 mm, unrotated", "pass" if not bad else f"FAIL ({len(bad)})"))

    font_rows = qa.fonts(reading)
    unembedded = [r["name"] for r in font_rows if r["emb"] != "yes"]
    foreign = [r["name"] for r in font_rows if "EBGaramond" not in r["name"]]
    hard += [f"font not embedded: {n}" for n in unembedded] + [f"unexpected font: {n}" for n in foreign]
    checks.append(("All fonts embedded (subset) and only EB Garamond used",
                   "pass: " + ", ".join(r["name"].split("+")[-1] for r in font_rows)
                   if not unembedded and not foreign else "FAIL"))

    all_text = json.dumps(data, ensure_ascii=False) + json.dumps(meta, ensure_ascii=False)
    missing = qa.missing_glyphs(all_text, [FONT_DIR / n for n in FONTS])
    hard += [f"glyph missing from EB Garamond: {c!r} U+{ord(c):04X}" for c in missing]
    checks.append(("Every character in the manuscript has a glyph in the font",
                   "pass" if not missing else f"FAIL: {missing}"))

    pages = qa.read_pages(reading)
    main_start = qa.find_main_start(pages)

    def folio(n: int) -> str:
        if n >= main_start:
            return str(n - main_start + 1)
        return docs.roman(n)

    expected = [qa.norm(w) for w in content.reading_words(data)]
    got = qa.extracted_words(pages, main_start, set(expected))
    diffs = qa.compare_words(expected, got)
    hard += [f"text: {d}" for d in diffs]
    checks.append((
        "Extracted reading text matches the manuscript word for word",
        f"pass: {len(got):,} words in the PDF, {len(expected):,} expected, 0 differences"
        if not diffs else f"FAIL: {len(diffs)} differences",
    ))

    lay = qa.layout(pages, main_start, folio)
    marks = query_marks(src / "book1.typ")
    lay.widows, lay.orphans = qa.widows_orphans(marks, pages, folio)
    ids = {m["id"] for m in marks}
    n_paras = sum(len(s["blocks"]) - sum(b["t"] in ("scene", "sub") for b in s["blocks"]) for s in data["sections"])
    if len(ids) != n_paras or len(marks) != 2 * n_paras:
        hard.append(f"paragraph markers: {len(ids)} paragraphs placed, {n_paras} expected")
    checks.append(("Every paragraph placed once (position markers at both ends)",
                   f"pass: {n_paras:,} paragraphs" if len(ids) == n_paras else "FAIL"))
    checks.append(("No widows or orphans (from paragraph positions)",
                   "pass" if not lay.widows and not lay.orphans
                   else f"{len(lay.widows)} widows, {len(lay.orphans)} orphans (see concerns)"))
    hard += lay.errors
    if lay.long_pages:
        hard.append(f"text runs below the text area on {lay.long_pages}")

    # Every section opens on a recto, and the contents page numbers agree.
    secs = data["sections"]
    heads = []
    for s in secs:
        if "act" in s:
            heads.append(("part", s["act"]["label"]))
        heads.append((s["kind"], s["label"] if s["kind"] == "chapter" else s["title"]))
    found = []
    for n in lay.openings:
        first = pages[n - 1].body[0].text
        found.append((n, first))
    if len(found) != len(heads):
        hard.append(f"expected {len(heads)} opening pages (parts, chapters, back matter), found {len(found)}")
    opening_page = {}
    for (kind, label), (n, first) in zip(heads, found):
        if not first.startswith(label):
            hard.append(f"opening order: expected «{label}» on PDF page {n}, found «{first[:40]}»")
        if n % 2 == 0:
            hard.append(f"«{label}» opens on a verso (PDF page {n})")
        opening_page[(kind, label)] = n
    checks.append(("Prologue, 5 part pages, 36 chapters and 2 back-matter sections each open on a recto, in order",
                   "pass" if len(found) == len(heads) else "FAIL"))

    contents_text = " | ".join(r for p in pages[: main_start - 1] for r in qa.rows(p))
    toc_bad = []
    for s in secs:
        key = ("chapter", s["label"]) if s["kind"] == "chapter" else ("back", s["title"])
        n = opening_page.get(key)
        title = s["title"] if s["kind"] == "back" or s["number"] != "0" else f"Prologue: {s['title']}"
        if n is None or f"{title} {folio(n)} |" not in contents_text + " |":
            toc_bad.append(title)
    hard += [f"contents entry wrong or missing: {t}" for t in toc_bad]
    checks.append(("Contents lists every section with its correct page number",
                   "pass" if not toc_bad else f"FAIL: {toc_bad}"))

    blank_ok = all(n == 2 or (n + 1) in lay.openings for n in lay.blanks)
    checks.append(("Blank pages carry no running head or folio, and each sits before a recto opening",
                   f"pass: {len(lay.blanks)} blank pages" if blank_ok and not lay.errors else "FAIL"))
    if not blank_ok:
        hard.append(f"unexpected blank pages: {[n for n in lay.blanks if n != 2 and n + 1 not in lay.openings]}")
    checks.append(("Opening pages carry no running head; folios only where intended",
                   "pass" if not lay.errors else "FAIL"))

    if hard:
        print("\n".join(hard[:60]))
        fail(f"{len(hard)} check(s) failed; nothing written to {out}")

    # ---- C. Signatures ---------------------------------------------------------------
    sigs = impose.plan(total, args.signature)
    padded = sigs[-1].end
    side_rows = []
    for sig in sigs:
        for side, sheet, left, right in impose.sides(sig):
            side_rows.append({
                "label": impose.side_label(sig, side, sheet, left, right, total),
                "collation": None if args.no_collation_marks or not (side == "front" and sheet == 1)
                else sig.number - 1,
            })
    (src / "sides.json").write_text(json.dumps(side_rows, ensure_ascii=False), encoding="utf-8")
    marks_pdf = work / "marks.pdf"
    compile_typst(src / "marks.typ", marks_pdf, stamp_date)
    calib = work / "calibration.pdf"
    compile_typst(src / "marks.typ", calib, stamp_date, {"mode": "calibration"})
    mark_pages = PdfReader(str(marks_pdf)).pages

    reader = PdfReader(str(reading))
    page_texts = {i: " ".join(qa.norm(t).split())
                  for i, t in enumerate(subprocess.run(["pdftotext", str(reading), "-"], check=True,
                                                       capture_output=True, text=True).stdout.split("\f"), 1)}
    sig_dir = work / "signatures"
    sig_dir.mkdir()
    combined = PdfWriter()
    sig_files = []
    imp_problems = []
    mi = 0
    for sig in sigs:
        n_sides = sig.sheets * 2
        w = impose.impose(reader, sig, total, mark_pages[mi: mi + n_sides])
        mi += n_sides
        name = f"sig{sig.number:02d}_pdf-pages_{sig.start:03d}-{sig.end:03d}.pdf"
        path = sig_dir / name
        with open(path, "wb") as fh:
            w.write(fh)
        sig_files.append(path)
        for pg in PdfReader(str(path)).pages:
            combined.add_page(pg)
        imp_problems += qa.check_signature(reading, path, sig, total, page_texts)
    all_sigs = work / "Ides_Book1_imposed_A4_all-signatures.pdf"
    with open(all_sigs, "wb") as fh:
        combined.write(fh)
    if imp_problems:
        print("\n".join(imp_problems[:40]))
        fail(f"{len(imp_problems)} imposition check(s) failed")
    checks.append((
        f"All {len(sigs)} signatures: fold walk, verso/recto halves, A4 landscape, and each half's text equals its reading page",
        "pass",
    ))
    font_bad = [p.name for p in sig_files + [all_sigs, calib]
                if any(r["emb"] != "yes" for r in qa.fonts(p))]
    checks.append(("Imposed and calibration PDFs embed all fonts", "pass" if not font_bad else f"FAIL {font_bad}"))
    if font_bad:
        fail(f"unembedded fonts in {font_bad}")

    # ---- Test signature: a real signature with a chapter opening, a scene break,
    # dialogue and italics, printable before committing to the whole book.
    def has_italic(n: int) -> bool:
        if n < main_start:
            return False
        res = reader.pages[n - 1].get("/Resources") or {}
        fonts_ = res.get("/Font") or {}
        return any("Italic" in str(f.get_object().get("/BaseFont")) for f in fonts_.values())

    def scene_break(n: int) -> bool:
        return (n >= main_start and n not in lay.openings and bool(pages[n - 1].head)
                and any(qa.classify(l, n) == "centred" for l in pages[n - 1].body))

    test = None
    for sig in sigs:
        rng = range(sig.start, min(sig.end, total) + 1)
        if (any(n in lay.openings and pages[n - 1].body[0].text.startswith("Chapter") for n in rng)
                and any(scene_break(n) for n in rng) and any(has_italic(n) for n in rng)
                and any("“" in page_texts[n] for n in rng) and sig.pages == args.signature):
            test = sig
            break
    if test is None:
        fail("no signature holds a chapter opening, scene break, dialogue and italics")
    test_dir = work / "test"
    test_dir.mkdir()
    test_reading = test_dir / f"TEST_reading-order_pdf-pages_{test.start:03d}-{test.end:03d}.pdf"
    tw = PdfWriter()
    for n in range(test.start, test.end + 1):
        tw.add_page(reader.pages[n - 1])
    with open(test_reading, "wb") as fh:
        tw.write(fh)
    test_imposed = test_dir / f"TEST_signature-{test.number:02d}_imposed_A4_print-me-first.pdf"
    shutil.copy(sig_files[test.number - 1], test_imposed)
    shutil.copy(calib, test_dir / "TEST_duplex-calibration-sheet_A4.pdf")

    # Previews for visual inspection.
    prev = work / "qa_previews"
    prev.mkdir()
    subprocess.run(["pdftoppm", "-r", "50", "-png", str(test_imposed), str(prev / "test_sig_side")], check=True)
    subprocess.run(["pdftoppm", "-r", "70", "-png", "-f", str(test.start), "-l", str(test.start + 3),
                    str(reading), str(prev / "test_reading")], check=True)

    # ---- D/E. Documents ----------------------------------------------------------------
    info = docs.Info(
        meta=meta, stamp=stamp, total=total, padded=padded, sigs=sigs, main_start=main_start,
        test=test, layout=lay, checks=checks, words=len(expected), signature=args.signature,
        concerns=qa.source_concerns(data), folio=folio, collation=not args.no_collation_marks,
        reading_name=READING_NAME, fitted=fitted,
    )
    docs.write_all(info, src, work, compile_typst, stamp_date)

    # ---- Publish -------------------------------------------------------------------------
    marks_pdf.unlink()
    calib.unlink()  # copied into test/
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(work, out)
    shutil.rmtree(work)
    print(f"OK: wrote {out}")
    for c, r in checks:
        print(f"  [{r.split(':')[0]}] {c}")


if __name__ == "__main__":
    main()

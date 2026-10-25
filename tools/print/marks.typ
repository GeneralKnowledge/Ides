// Printer's marks for imposed A4 sheets, and the duplex calibration sheet.
// Everything here sits outside the trimmed book page: in the fore-edge strips
// (19.5 mm each side) and the head and tail strips (6 mm), all cut away.
// sides.json is written by impose.py: one entry per printed side.

#let mode = sys.inputs.at("mode", default: "marks")
#let sheet-w = 297mm
#let sheet-h = 210mm
#let fold = sheet-w / 2
#let page-w = 129mm
#let page-h = 198mm
#let head = (sheet-h - page-h) / 2
#let fore = fold - page-w
#let hair = 0.3pt

#set page(width: sheet-w, height: sheet-h, margin: 0pt)
#set text(font: "EB Garamond", size: 7pt, number-type: "lining")

#let line-at(x1, y1, x2, y2) = place(top + left, line(start: (x1, y1), end: (x2, y2), stroke: hair))

#let trim-marks() = {
  // Fold: centre ticks in the head and tail strips.
  line-at(fold, 0.5mm, fold, head - 1.5mm)
  line-at(fold, sheet-h - head + 1.5mm, fold, sheet-h - 0.5mm)
  // Head and tail trim lines, drawn in the fore-edge strips.
  for y in (head, sheet-h - head) {
    line-at(3mm, y, fore - 2mm, y)
    line-at(sheet-w - fore + 2mm, y, sheet-w - 3mm, y)
  }
  // Fore-edge trim lines, drawn in the head and tail strips.
  for x in (fore, sheet-w - fore) {
    line-at(x, 0.5mm, x, head - 1.5mm)
    line-at(x, sheet-h - head + 1.5mm, x, sheet-h - 0.5mm)
  }
}

#let strip-label(body) = place(top + left, dx: fore / 2 - 1.2mm, dy: (sheet-h - 150mm) / 2,
  rotate(-90deg, reflow: true, origin: center, box(width: 150mm, align(center, body))))

#if mode == "marks" {
  let sides = json("sides.json")
  for (i, s) in sides.enumerate() {
    if i > 0 { pagebreak() }
    trim-marks()
    strip-label(text(tracking: 0.04em, s.label))
    if s.collation != none {
      // Stepped collation mark across the spine fold of the outer sheet.
      let step = calc.rem(s.collation, 24)
      place(top + left, dx: fold - 0.8mm, dy: 14mm + step * 7mm,
        rect(width: 1.6mm, height: 5mm, fill: black, stroke: none))
    }
  }
} else {
  // Duplex calibration sheet: front and back carry crosses at the same
  // physical positions, so held to the light they coincide when duplex
  // registration is right. Page outlines show where the book pages land.
  let crosses = ((fold, 22mm), (fold, 188mm), (50mm, 165mm), (sheet-w - 50mm, 165mm))
  for (side, name) in ((0, "FRONT"), (1, "BACK")) {
    if side == 1 { pagebreak() }
    trim-marks()
    for (x, y) in crosses {
      // The back is seen mirrored after a short-edge flip.
      let xx = if side == 1 { sheet-w - x } else { x }
      line-at(xx - 6mm, y, xx + 6mm, y)
      line-at(xx, y - 6mm, xx, y + 6mm)
      place(top + left, dx: xx - 2mm, dy: y - 2mm, circle(radius: 2mm, stroke: hair))
    }
    for x in (fore, fold) {
      place(top + left, dx: x, dy: head, rect(width: page-w, height: page-h, stroke: (paint: luma(60%), thickness: hair, dash: "dashed")))
    }
    let body = if side == 0 [
      #text(size: 20pt, tracking: 0.2em)[FRONT]
      #v(4mm)
      #text(size: 10pt)[Print at Actual size / 100 % · two-sided · flip on short edge]
      #v(5mm)
      #box(width: 100mm, height: 3mm, stroke: hair, fill: luma(85%))
      #v(1mm)
      #text(size: 9pt)[This bar should measure exactly 100 mm. If not, scaling is on.]
    ] else [
      #text(size: 20pt, tracking: 0.2em)[BACK]
      #v(4mm)
      #text(size: 10pt)[This side must read the right way up when the sheet is turned over left to right.]
      #v(2mm)
      #text(size: 10pt)[If it is upside down, switch between “flip on short edge” and “flip on long edge”.]
      #v(2mm)
      #text(size: 10pt)[Hold the sheet to a window: the crosses on both sides should coincide.]
      #v(2mm)
      #text(size: 10pt)[Measure any offset; under 1 mm is fine for this book.]
    ]
    // Centre the instructions inside the right-hand page outline.
    place(top + left, dx: fold + 8mm, dy: 45mm, box(width: page-w - 16mm, align(center, body)))
    place(top + left, dx: fore + 8mm, dy: 45mm, box(width: page-w - 16mm, align(center,
      text(size: 30pt, tracking: 0.2em, name))))
  }
}

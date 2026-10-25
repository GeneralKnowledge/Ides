// Punching jig for sewing on three tapes with kettle stitches.
// Positions are measured along the fold of the untrimmed sheet (210 mm),
// from the head edge. Print at 100 %, glue to card, crease along the
// centre line, and lay it in the fold of each signature to pierce.

#let fold-h = 210mm
#let trim = 6mm
#let kettle = 21mm          // 15 mm inside the trim line
#let tape-w = 12mm
#let tape-centres = (63mm, 105mm, 147mm)  // evenly between the kettles
#let gap = 1mm              // hole sits this far outside the tape edge
#let holes = (kettle,) + tape-centres.map(c => (c - tape-w / 2 - gap, c + tape-w / 2 + gap)).flatten() + (fold-h - kettle,)

#set page(paper: "a4", margin: 0pt)
#set text(font: "EB Garamond", size: 9pt, number-type: "lining")

#let x0 = 40mm   // strip's head edge, from the page's left
#let y0 = 70mm   // strip's top, from the page's top
#let strip-h = 50mm
#let hair = 0.4pt
#let at(x, y, body) = place(top + left, dx: x, dy: y, body)
#let vline(x, y1, y2, ..s) = at(0pt, 0pt, line(start: (x, y1), end: (x, y2), stroke: s.at(0, default: hair)))

// Rotate the page content so the 210 mm strip runs along the A4 long side.
#rotate(-90deg, reflow: true, block(width: 297mm, height: 210mm, {
  at(x0, 18mm, text(size: 16pt, tracking: 0.12em, smallcaps(all: true)[Sewing jig · three tapes, kettle stitch]))
  at(x0, 28mm, block(width: 220mm, text(size: 9.5pt)[
    Print at *Actual size / 100 %*, then check the 100 mm bar below. Glue the strip to thin card, cut it out on the
    outer line, and crease it along the dashed centre line so it sits in the fold of a signature. Butt the *HEAD*
    end against the signature’s head edge (untrimmed, 210 mm) and pierce through each dot from the inside of the fold.
    Use the same end, head to head, for every signature.
  ]))
  // Strip outline and centre (fold) line.
  at(x0, y0, rect(width: fold-h, height: strip-h, stroke: hair))
  at(x0, y0 + strip-h / 2, line(length: fold-h, stroke: (thickness: hair, dash: "dashed")))
  // Trim lines.
  for x in (trim, fold-h - trim) {
    vline(x0 + x, y0, y0 + strip-h, (thickness: hair, dash: "dotted"))
  }
  at(x0 + trim + 1mm, y0 + 2mm, text(size: 6.5pt)[trim])
  at(x0 + fold-h - trim - 7mm, y0 + 2mm, text(size: 6.5pt)[trim])
  // Tapes.
  for c in tape-centres {
    at(x0 + c - tape-w / 2, y0 + 6mm, rect(width: tape-w, height: strip-h - 12mm, fill: luma(90%), stroke: none))
    at(x0 + c - tape-w / 2, y0 + strip-h - 5mm, box(width: tape-w, align(center, text(size: 6.5pt)[tape])))
  }
  // Holes, with distances from the head.
  for (i, h) in holes.enumerate() {
    vline(x0 + h, y0 + strip-h / 2 - 5mm, y0 + strip-h / 2 + 5mm)
    at(x0 + h - 0.9mm, y0 + strip-h / 2 - 0.9mm, circle(radius: 0.9mm, fill: black))
    let kind = if i == 0 or i == holes.len() - 1 [kettle] else []
    at(x0 + h - 8mm, y0 + strip-h + 2mm, box(width: 16mm, align(center,
      text(size: 7pt)[#calc.round(h / 1mm, digits: 1) mm \ #kind])))
  }
  at(x0 - 13mm, y0 + strip-h / 2 - 2mm, text(size: 9pt, tracking: 0.1em)[HEAD])
  at(x0 + fold-h + 2mm, y0 + strip-h / 2 - 2mm, text(size: 8pt)[tail])
  // Scale check.
  at(x0, 150mm, rect(width: 100mm, height: 3mm, fill: luma(80%), stroke: hair))
  at(x0, 155mm, text(size: 8pt)[This bar must measure exactly 100 mm.])
  at(x0, 168mm, block(width: 220mm, text(size: 8.5pt)[
    Stations: kettle 21 mm from head and tail (15 mm inside the 6 mm trim lines); three 12 mm tapes centred at
    63, 105 and 147 mm, with a hole 1 mm outside each tape edge. Eight holes per signature.
  ]))
}))

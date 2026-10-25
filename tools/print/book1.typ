// Book 1 print interior: reading order, finished trim size.
// Built by tools/print/build_book1_print.py, which writes content.json (the
// manuscript, parsed), meta.json (bibliographic details) and build.json
// (manuscript revision) next to this file. Design values live here.

#let book = json("content.json")
#let meta = json("meta.json")
#let build = json("build.json")
// Copyfitting: paragraphs set a hair tighter or looser so a page fills its
// grid instead of running short (written by fit.py; ids are section.block).
#let adjust = json("adjust.json")
#let fit-levels = (
  "-2": (tracking: -0.015em, spacing: 90%),
  "-1": (tracking: -0.008em, spacing: 95%),
  "1": (tracking: 0.01em, spacing: 108%),
  "2": (tracking: 0.018em, spacing: 115%),
)

// Page and type. Every line of prose sits on a baseline grid of `lh`, so
// facing pages line up; headings occupy whole grid lines.
#let trim-w = 129mm
#let trim-h = 198mm
#let m-inside = 19mm
#let m-outside = 15mm
#let m-top = 17.5mm
#let size = 10.75pt
#let lh = 13.5pt
#let lead = lh - size
#let lines-per-page = 33
#let text-h = lines-per-page * size + (lines-per-page - 1) * lead
#let m-bottom = trim-h - m-top - text-h - 0.5pt

#set document(title: meta.title + ": " + meta.volume, author: meta.author)
#set text(
  font: "EB Garamond",
  size: size,
  lang: "en",
  region: "GB",
  hyphenate: true,
  number-type: "old-style",
  top-edge: 0.75em,
  bottom-edge: -0.25em,
  costs: (hyphenation: 150%, runt: 150%, widow: 100%, orphan: 100%),
)
#set par(
  justify: true,
  leading: lead,
  spacing: lead,
  first-line-indent: 0pt,
  justification-limits: (
    spacing: (min: 80%, max: 150%),
    tracking: (min: -0.01em, max: 0.015em),
  ),
)
#set block(spacing: lead)

// ---- Page furniture ---------------------------------------------------------

// Each page unit (front-matter page, part page, chapter, back-matter section)
// is bracketed by start/end markers. A page between an end and the next start
// is a deliberate blank: no running head, no folio.
#let unit-start(kind, running: none, folio: true) = [#metadata((
  kind: "start", unit: kind, running: running, folio: folio,
))<flow>]
#let unit-end = [#metadata((kind: "end"))<flow>]

#let page-info() = {
  let p = here().page()
  let marks = query(<flow>)
  let blank = false
  let opening = none
  let current = none
  let prev = none
  for m in marks {
    let mp = m.location().page()
    if m.value.kind == "start" {
      if mp == p { opening = m.value }
      if mp <= p { current = m.value }
      if prev != none and prev.value.kind == "end" {
        let ep = prev.location().page()
        if ep < p and p < mp { blank = true }
      }
    }
    prev = m
  }
  if prev != none and prev.value.kind == "end" and prev.location().page() < p {
    blank = true
  }
  (blank: blank, opening: opening, current: current)
}

#let main-start() = query(<main>).first().location().page()

#let folio-of(p) = {
  let m = main-start()
  if p >= m { str(p - m + 1) } else { numbering("i", p) }
}

#let head-style(body) = text(size: 8.25pt, tracking: 0.1em, smallcaps(all: true, body))

#set page(
  width: trim-w,
  height: trim-h,
  binding: left,
  margin: (inside: m-inside, outside: m-outside, top: m-top, bottom: m-bottom),
  header-ascent: 6.5mm,
  footer-descent: 9mm,
  header: context {
    let i = page-info()
    if i.blank or i.opening != none or i.current == none { return }
    if i.current.running == none { return }
    let verso = calc.even(here().page())
    align(center, head-style(if verso { meta.title } else { i.current.running }))
  },
  footer: context {
    let i = page-info()
    if i.blank or i.current == none { return }
    if i.opening != none and not i.opening.folio { return }
    if not i.current.folio { return }
    align(center, text(size: 9.5pt, folio-of(here().page())))
  },
)

// ---- Text ------------------------------------------------------------------

#let run(r) = {
  let (t, s) = r
  if s == "i" { emph(t) } else if s == "sc" { smallcaps(t) } else { t }
}
#let inline(runs) = runs.map(run).join()

// Opening words of a chapter in small caps.
#let lead-in(runs, n: 3) = {
  let (t, s) = runs.first()
  if s != "" { return inline(runs) }
  let words = t.split(" ")
  let head = words.slice(0, calc.min(n, words.len())).join(" ")
  let rest = t.slice(head.len())
  smallcaps(head) + rest + inline(runs.slice(1))
}

// A heading that occupies `n` whole grid lines with its text on line `at`.
#let grid-block(n, at, body, sticky: true) = block(
  width: 100%,
  height: n * lh - lead,
  sticky: sticky,
  breakable: false,
  place(top + center, dy: (at - 1) * lh, body),
)

#let scene-title(runs) = context {
  let t = text(tracking: 0.08em, smallcaps(all: true, inline(runs)))
  let w = measure(t).width
  // A title too long for one line gets a second grid line.
  if w > 0.95 * (trim-w - m-inside - m-outside) {
    grid-block(4, 2, box(width: 85%, align(center, par(justify: false, leading: lead, t))))
  } else {
    grid-block(3, 2, t)
  }
}

// Zero-width position markers at both ends of each paragraph, read back by
// fit.py and the build checks (`typst query <pmark>`).
#let pmark(id, end) = box(context [#metadata((
  id: id, end: end, page: here().page(),
  x: here().position().x.pt(), y: here().position().y.pt(),
))<pmark>])

#let fitted(id, body) = {
  let level = adjust.at(id, default: none)
  if level == none { body } else {
    text(..fit-levels.at((if level < 0 { "-" } else { "" }) + str(calc.abs(level))), body)
  }
}

#let para(runs, id, indent: true, opening: false) = {
  let body = par(
    first-line-indent: (amount: if indent { 1em } else { 0pt }, all: true),
    pmark(id, false) + (if opening { lead-in(runs) } else { inline(runs) }) + pmark(id, true),
  )
  fitted(id, body)
}

#let render-blocks(blocks, sid, opening-lead-in: true) = {
  let prev = "title"
  let first-para = true
  for (j, b) in blocks.enumerate() {
    let id = str(sid) + "." + str(j)
    let t = b.t
    if t == "scene" or t == "sub" {
      scene-title(b.runs)
    } else if t == "item" {
      pad(left: 1.5em, par(first-line-indent: 0pt, hanging-indent: 1em, justify: false,
        pmark(id, false) + inline(b.runs) + pmark(id, true)))
    } else if t == "bullet" {
      fitted(id, par(first-line-indent: 0pt, hanging-indent: 1em, justify: false,
        pmark(id, false) + inline(b.runs) + pmark(id, true)))
    } else {
      let fresh = prev in ("title", "scene", "sub", "bullet")
      para(b.runs, id, indent: not fresh, opening: opening-lead-in and first-para)
      first-para = false
    }
    prev = t
  }
}

// ---- Front matter ----------------------------------------------------------

#let present(key) = key in meta and meta.at(key) != none

#let half-title() = {
  unit-start("half-title", folio: false)
  v(6 * lh)
  align(center, text(size: 12pt, tracking: 0.14em, smallcaps(all: true, meta.title)))
  unit-end
}

#let title-page() = {
  pagebreak(to: "odd", weak: true)
  unit-start("title", folio: false)
  v(5 * lh)
  align(center, text(size: 22pt, tracking: 0.12em, smallcaps(all: true, meta.title)))
  v(1.2 * lh)
  align(center, text(size: 13pt, style: "italic", meta.volume))
  v(9 * lh)
  align(center, text(size: 12pt, tracking: 0.14em, smallcaps(all: true, meta.author)))
  if present("publisher") {
    place(bottom + center, text(size: 9.5pt, tracking: 0.1em, smallcaps(all: true, meta.publisher)))
  }
  unit-end
}

#let copyright-page() = {
  pagebreak()
  unit-start("copyright", folio: false)
  set par(justify: false, first-line-indent: 0pt)
  set text(size: 8.5pt)
  let lines = ()
  for key in ("copyright_line", "rights_statement", "edition_statement") {
    if present(key) { lines.push(meta.at(key)) }
  }
  if present("isbn") { lines.push("ISBN " + meta.isbn) }
  lines.push([Set in EB Garamond])
  if meta.at("show_revision_line", default: false) {
    lines.push([Interior set from manuscript revision #build.manuscript (#build.manuscript_date)])
  }
  place(bottom + left, block(width: 100%, lines.join(parbreak())))
  unit-end
}

#let single-page(kind, body) = {
  pagebreak(to: "odd", weak: true)
  unit-start(kind, folio: false)
  v(7 * lh)
  align(center, block(width: 80%, text(style: "italic", body)))
  unit-end
}

#let contents() = {
  pagebreak(to: "odd", weak: true)
  unit-start("contents", folio: true)
  grid-block(5, 2, text(size: 11pt, tracking: 0.14em, smallcaps(all: true)[Contents]), sticky: false)
  set par(justify: false, first-line-indent: 0pt)
  let row(num, title, i) = grid(
    columns: (1.8em, 1fr, auto),
    align: (right, left, right),
    column-gutter: 0.6em,
    num, title,
    context folio-of(query(label("sec-" + str(i))).first().location().page()),
  )
  for (i, sec) in book.sections.enumerate() {
    if "act" in sec {
      block(above: lh, below: lead, sticky: true, align(center,
        text(size: 8.5pt, tracking: 0.12em, smallcaps(all: true, sec.act.label + ": " + sec.act.title))))
    } else if sec.kind == "back" and book.sections.at(i - 1).kind != "back" {
      v(lh - lead)
    }
    if sec.kind == "chapter" and sec.number != "0" {
      row(sec.number, sec.title, i)
    } else {
      row([], if sec.kind == "chapter" { sec.label + ": " + sec.title } else { sec.title }, i)
    }
  }
  unit-end
}

// ---- Main matter -----------------------------------------------------------

#let part-page(act) = {
  pagebreak(to: "odd", weak: true)
  unit-start("part", folio: false)
  v(8 * lh)
  align(center, text(size: 9pt, tracking: 0.16em, smallcaps(all: true, act.label)))
  v(0.8 * lh)
  align(center, text(size: 16pt, act.title))
  unit-end
}

#let opening(label, title) = grid-block(9, 4, sticky: true, {
  if label != none {
    text(size: 9pt, tracking: 0.16em, smallcaps(all: true, label))
    v(1.6 * lh, weak: false)
  } else {
    v(2.6 * lh)
  }
  text(size: 16pt, title)
})

#let section(sec, i, first) = {
  if "act" in sec { part-page(sec.act) }
  pagebreak(to: "odd", weak: true)
  unit-start(sec.kind, running: sec.running, folio: true)
  [#metadata(i)#label("sec-" + str(i))]
  if first [#metadata("main")<main>]
  if sec.kind == "chapter" {
    opening(sec.label, sec.title)
  } else {
    opening(none, sec.title)
  }
  render-blocks(sec.blocks, i, opening-lead-in: sec.kind == "chapter")
  unit-end
}

// ---- The book --------------------------------------------------------------

#half-title()
#title-page()
#copyright-page()
#if present("dedication") { single-page("dedication", meta.dedication) }
#if present("epigraph") { single-page("epigraph", meta.epigraph) }
#contents()
#for (i, sec) in book.sections.enumerate() { section(sec, i, i == 0) }

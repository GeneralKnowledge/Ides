#!/usr/bin/env python3
"""Export Book 1 as an EPUB 3 ebook (Kindle via Send to Kindle, Apple Books, Kobo).

    python tools/export_book1_epub.py           # write exports/Ides_Book1_Ch01-37.epub
    python tools/export_book1_epub.py --check   # verify the written EPUB

The reading text comes from tools/export_book1_docx.py (same parser, same
order: cast list and offices, prologue, acts and chapters, historical note and
timeline), so the ebook and the DOCX never drift. Layout is reflowable and
left to the reader's device: no embedded fonts, no fixed sizes.

--check reopens the EPUB, compares every reading paragraph with the
manuscript, and runs epubcheck when it is on PATH (``pip install epubcheck``).
The EPUB lands in exports/, which git ignores; it is not tracked.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import uuid
import zipfile
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import export_book1_docx as dx  # noqa: E402

EPUB_PATH = dx.EXPORTS / f"Ides_Book1_Ch01-{dx.CHAPTER_COUNT:02d}.epub"
FONTS = dx.ROOT / "tools" / "print" / "fonts"
TITLE = "The Ides of March"
SUBTITLE = "Book 1"
AUTHOR = "Reuben Dennison"
END_LINE = "End of Book 1"
# Stable book id: Kindle and other readers key reading position on it, so a
# re-sent copy replaces the old one instead of sitting beside it.
BOOK_ID = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "https://github.com/GeneralKnowledge/Ides/book1"))

CSS = """\
body { margin: 0 4%; font-family: serif; line-height: 1.4; }
p { margin: 0; text-indent: 1.4em; text-align: justify; hyphens: auto; -webkit-hyphens: auto; }
p.first, p.break, p.item, p.end, p.center { text-indent: 0; }
p.break { text-align: center; margin: 1em 0; }
p.item { margin: 0.15em 0 0.15em 1.4em; text-indent: -1em; text-align: left; }
p.end { text-align: center; margin-top: 3em; font-variant: small-caps; }
.sc { font-variant: small-caps; letter-spacing: 0.03em; }
h1, h2, h3 { font-weight: normal; text-align: center; page-break-after: avoid; }
h1.act { margin-top: 30%; font-size: 1.5em; }
h1.back { margin: 2em 0 1.2em; font-size: 1.4em; }
h2.chapter { margin: 3em 0 0; }
h2.chapter .num { display: block; font-size: 0.7em; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 0.6em; }
h2.chapter .title { display: block; font-size: 1.25em; margin-bottom: 2em; }
h3 { font-size: 1.05em; margin: 1.2em 0 0.4em; }
div.titlepage { text-align: center; margin-top: 30%; }
div.titlepage h1 { font-size: 2em; letter-spacing: 0.12em; text-transform: uppercase; }
div.titlepage p { text-indent: 0; text-align: center; }
p.subtitle { font-style: italic; font-size: 1.2em; margin-top: 0.8em; }
p.author { margin-top: 4em; letter-spacing: 0.1em; text-transform: uppercase; }
p.colophon { text-indent: 0; text-align: center; font-size: 0.8em; margin-top: 2em; font-style: italic; }
nav ol { list-style: none; padding-left: 1em; }
img.cover { width: 100%; height: auto; }
"""


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def inline(text: str, sc_words: int = 0) -> str:
    """Markdown italics -> <em>, **bold** -> small caps, as in the DOCX."""
    out = []
    for j, part in enumerate(dx.BOLD.split(text)):
        chunk = []
        for k, (t, it) in enumerate(dx.to_runs(part)):
            if j == 0 and k == 0 and sc_words and not it:
                lead = " ".join(t.split(" ")[:sc_words])
                chunk.append(f'<span class="sc">{esc(lead)}</span>{esc(t[len(lead):])}')
            else:
                chunk.append(f"<em>{esc(t)}</em>" if it else esc(t))
        s = "".join(chunk)
        out.append(f'<span class="sc">{s}</span>' if j % 2 else s)
    return "".join(out)


def page(title: str, body: str, epub_type: str = "") -> str:
    et = f' epub:type="{epub_type}"' if epub_type else ""
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" '
        'xml:lang="en-GB" lang="en-GB">\n<head><meta charset="utf-8"/>'
        f"<title>{esc(title)}</title>"
        '<link rel="stylesheet" type="text/css" href="style.css"/></head>\n'
        f"<body{et}>\n{body}\n</body>\n</html>\n"
    )


def split_files(paras: list[tuple[str, str]]) -> list[dict]:
    """One XHTML file per act page, chapter, and back-matter page."""
    files: list[dict] = []
    i = 0
    while i < len(paras):
        text, role = paras[i]
        if role == "act":
            files.append(dict(kind="act", label=text, html=[f'<h1 class="act">{inline(text)}</h1>']))
            i += 1
            continue
        if role == "chapter":
            title = paras[i + 1][0]
            files.append(dict(
                kind="chapter", label=text, title=title,
                html=[f'<h2 class="chapter"><span class="num">{esc(text)}</span>'
                      f'<span class="title">{inline(title)}</span></h2>'],
            ))
            i += 2
            prev = "title"
        elif role == "back_head":
            files.append(dict(kind="back", label=text, html=[f'<h1 class="back">{inline(text)}</h1>']))
            i += 1
            prev = "back_head"
        else:
            raise SystemExit(f"Unexpected paragraph before any heading: {text[:60]}")
        # Body of this file
        while i < len(paras) and paras[i][1] not in ("act", "chapter", "back_head"):
            text, role = paras[i]
            h = files[-1]["html"]
            if role == "scene":
                h.append('<p class="break">·   ·   ·</p>')
            elif role == "back_sub":
                h.append(f"<h3>{inline(text)}</h3>")
            elif role in ("back_item",) or (role == "body" and dx.LIST_ITEM.match(text)):
                h.append(f'<p class="item">{inline(text)}</p>')
                role = "item"
            elif role == "end":
                h.append(f'<p class="end">{inline(text)}</p>')
            else:
                opening = prev in ("title", "scene", "back_head", "back_sub", "back_item", "item")
                cls = ' class="first"' if opening else ""
                h.append(f"<p{cls}>{inline(text, 3 if prev == 'title' else 0)}</p>")
            prev = role
            i += 1
    for n, f in enumerate(files, 1):
        f["name"] = f"part{n:03d}.xhtml"
    return files


def make_cover() -> bytes | None:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return None
    W, H = 1600, 2560
    img = Image.new("RGB", (W, H), (0x5a, 0x12, 0x12))
    d = ImageDraw.Draw(img)
    gold = (0xe6, 0xd3, 0xa3)

    def font(name: str, size: int):
        p = FONTS / name
        return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default(size)

    def centre(y: int, text: str, f, fill=gold, spacing: int = 0):
        if spacing:
            text = (" " * spacing).join(text)
        w = d.textlength(text, font=f)
        d.text(((W - w) / 2, y), text, font=f, fill=fill)

    d.rectangle([70, 70, W - 70, H - 70], outline=gold, width=4)
    d.rectangle([95, 95, W - 95, H - 95], outline=gold, width=2)
    centre(760, "THE IDES", font("EBGaramond-Regular.otf", 190))
    centre(980, "OF MARCH", font("EBGaramond-Regular.otf", 190))
    d.line([(W / 2 - 220, 1290), (W / 2 + 220, 1290)], fill=gold, width=3)
    centre(1360, "Book 1", font("EBGaramond-Italic.otf", 110))
    centre(2150, "REUBEN DENNISON", font("EBGaramond-Regular.otf", 80))
    buf = BytesIO()
    img.save(buf, "JPEG", quality=90)
    return buf.getvalue()


def nav_and_ncx(files: list[dict]) -> tuple[str, str]:
    """EPUB 3 nav (acts nest their chapters) plus an NCX for older readers."""
    items: list[tuple[int, str, str]] = []  # (depth, label, href)
    for f in files:
        if f["kind"] == "act":
            items.append((0, f["label"], f["name"]))
        elif f["kind"] == "chapter":
            in_act = any(x["kind"] == "act" for x in files[: files.index(f)]) and f["label"] != "Prologue"
            lead = "Prologue: " if f["label"] == "Prologue" else f["label"].replace("Chapter ", "") + ". "
            label = lead + re.sub(r"\*", "", f["title"])
            items.append((1 if in_act else 0, label, f["name"]))
        else:
            items.append((0, f["label"], f["name"]))

    def ol(start: int, depth: int) -> tuple[str, int]:
        out, i = ["<ol>"], start
        while i < len(items) and items[i][0] >= depth:
            d, label, href = items[i]
            li = f'<li><a href="{href}">{esc(label)}</a>'
            i += 1
            if i < len(items) and items[i][0] > depth:
                sub, i = ol(i, depth + 1)
                li += sub
            out.append(li + "</li>")
        return "".join(out) + "</ol>", i

    toc, _ = ol(0, 0)
    first_text = next(f["name"] for f in files if f["kind"] == "chapter")
    nav = page("Contents", (
        f'<nav epub:type="toc" id="toc"><h1 class="back">Contents</h1>{toc}</nav>\n'
        '<nav epub:type="landmarks" hidden="hidden"><ol>'
        '<li><a epub:type="cover" href="cover.xhtml">Cover</a></li>'
        '<li><a epub:type="toc" href="nav.xhtml">Contents</a></li>'
        f'<li><a epub:type="bodymatter" href="{first_text}">Start</a></li>'
        "</ol></nav>"
    ))

    points, n = [], 0
    stack: list[int] = []
    for d, label, href in items:
        while stack and stack[-1] >= d:
            points.append("</navPoint>")
            stack.pop()
        n += 1
        points.append(f'<navPoint id="np{n}" playOrder="{n}"><navLabel><text>{esc(label)}</text>'
                      f'</navLabel><content src="{href}"/>')
        stack.append(d)
    points.extend("</navPoint>" for _ in stack)
    ncx = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1"><head>'
        f'<meta name="dtb:uid" content="{BOOK_ID}"/><meta name="dtb:depth" content="2"/>'
        '<meta name="dtb:totalPageCount" content="0"/><meta name="dtb:maxPageNumber" content="0"/>'
        f"</head><docTitle><text>{esc(TITLE)}: {SUBTITLE}</text></docTitle>"
        f"<navMap>{''.join(points)}</navMap></ncx>\n"
    )
    return nav, ncx


def build(out: Path) -> dict[str, str]:
    files_src, chapters = dx.load_chapters()
    stamp = dx.source_stamp(files_src)
    paras = dx.reading_paragraphs(chapters, END_LINE, dx.full_back(), dx.full_front())
    parts = split_files(paras)
    cover = make_cover()
    nav, ncx = nav_and_ncx(parts)

    colophon = (
        f"Reading copy · manuscript {stamp['manuscript']} ({stamp['manuscript_date']}) · "
        f"source digest {stamp['digest']}"
    )
    title_page = page(TITLE, (
        f'<div class="titlepage"><h1>{esc(TITLE)}</h1><p class="subtitle">{SUBTITLE}</p>'
        f'<p class="author">{esc(AUTHOR)}</p></div>'
        f'<p class="colophon">{esc(colophon)}</p>'
    ), "frontmatter")

    docs: list[tuple[str, str, str]] = []  # (name, content, spine properties)
    if cover:
        docs.append(("cover.xhtml", page("Cover",
            f'<div><img class="cover" src="cover.jpg" alt="{esc(TITLE)}: {SUBTITLE}"/></div>', "cover"), ""))
    docs.append(("title.xhtml", title_page, ""))
    docs.append(("nav.xhtml", nav, ""))
    for p in parts:
        docs.append((p["name"], page(re.sub(r"\*", "", p.get("title", p["label"])), "\n".join(p["html"])), ""))

    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest = ['<item id="css" href="style.css" media-type="text/css"/>',
                '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>']
    if cover:
        manifest.append('<item id="cover-img" href="cover.jpg" media-type="image/jpeg" properties="cover-image"/>')
    spine = []
    for name, _, _ in docs:
        iid = name.split(".")[0]
        props = ' properties="nav"' if name == "nav.xhtml" else ""
        manifest.append(f'<item id="{iid}" href="{name}" media-type="application/xhtml+xml"{props}/>')
        spine.append(f'<itemref idref="{iid}"/>')
    opf = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="en-GB">'
        '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
        f'<dc:identifier id="bookid">{BOOK_ID}</dc:identifier>'
        f"<dc:title>{esc(TITLE)}: {SUBTITLE}</dc:title>"
        f"<dc:creator>{esc(AUTHOR)}</dc:creator><dc:language>en-GB</dc:language>"
        f"<dc:description>{esc(colophon)}</dc:description>"
        f'<meta property="dcterms:modified">{modified}</meta>'
        + ('<meta name="cover" content="cover-img"/>' if cover else "")
        + f'</metadata><manifest>{"".join(manifest)}</manifest>'
        f'<spine toc="ncx">{"".join(spine)}</spine></package>\n'
    )
    container = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
        '<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>'
        "</rootfiles></container>\n"
    )

    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/toc.ncx", ncx, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/style.css", CSS, compress_type=zipfile.ZIP_DEFLATED)
        if cover:
            z.writestr("OEBPS/cover.jpg", cover, compress_type=zipfile.ZIP_DEFLATED)
        for name, content, _ in docs:
            z.writestr(f"OEBPS/{name}", content, compress_type=zipfile.ZIP_DEFLATED)
    return stamp


def check(path: Path) -> int:
    """Reading paragraphs in the EPUB match the manuscript, in order; epubcheck passes."""
    _, chapters = dx.load_chapters()
    expected = [re.sub(r"\s+", " ", dx.plain(dx.to_runs(t))).strip()
                for t, _ in dx.reading_paragraphs(chapters, END_LINE, dx.full_back(), dx.full_front())]
    got: list[str] = []
    with zipfile.ZipFile(path) as z:
        names = sorted(n for n in z.namelist() if re.fullmatch(r"OEBPS/part\d+\.xhtml", n))
        for n in names:
            body = z.read(n).decode("utf-8").split("<body", 1)[1]
            for m in re.finditer(r"<(p|h1|h3)[^>]*>(.*?)</\1>|<span class=\"(?:num|title)\">(.*?)</span>", body):
                inner = m.group(2) if m.group(2) is not None else m.group(3)
                t = html.unescape(re.sub(r"<[^>]+>", "", inner)).replace(" ", " ")
                got.append(re.sub(r"\s+", " ", t).strip())
    problems = []
    if len(got) != len(expected):
        problems.append(f"paragraph count {len(got)} != expected {len(expected)}")
    for i, (e, g) in enumerate(zip(expected, got)):
        if e != g:
            problems.append(f"first mismatch at paragraph {i}: want {e[:70]!r} got {g[:70]!r}")
            break
    for g in got:
        if dx.LEAK.search(g):
            problems.append(f"metadata/markup leak: {g[:90]}")
    if problems:
        print(f"FAIL: {path.name}")
        for p in problems[:20]:
            print("  " + p)
        return 1
    print(f"OK: {path.name} · {len(got)} reading paragraphs match the manuscript · no leaks")
    try:
        from epubcheck import EpubCheck  # pip install epubcheck (needs Java)
    except ImportError:
        print("epubcheck not installed (pip install epubcheck); structural check skipped")
        return 0
    r = EpubCheck(str(path))
    for m in r.messages[:20]:
        print(f"  epubcheck {m.level} {m.id}: {m.location} {m.message}")
    print(f"epubcheck: {'valid' if r.valid else 'INVALID'} · {len(r.messages)} messages")
    return 0 if r.valid else 1


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="verify the written EPUB")
    ap.add_argument("--allow-dirty", action="store_true",
                    help="export even with uncommitted manuscript changes")
    args = ap.parse_args()
    if args.check:
        sys.exit(check(EPUB_PATH))
    if git_dirty() and not args.allow_dirty:
        raise SystemExit("drafts/book1 has uncommitted changes; commit first (or pass --allow-dirty)")
    stamp = build(EPUB_PATH)
    print(f"Wrote {EPUB_PATH}")
    print(dx.stamp_line(stamp))
    sys.exit(check(EPUB_PATH))


def git_dirty() -> bool:
    return bool(dx.git("status", "--porcelain", "--", "drafts/book1"))


if __name__ == "__main__":
    main()

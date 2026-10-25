"""Signature imposition: book pages two-up on A4 landscape, folded and nested.

Each A4 sheet is folded once across its width, so its two halves are
148.5 x 210 mm. A book page (129 x 198 mm) sits with its spine edge on the
fold and is centred head to tail; the 19.5 mm fore-edge and 6 mm head and tail
strips are trimmed off after sewing. Sheets nest: sheet 1 is the outside.

For a signature of n pages (1-based within the signature) and sheet k
(0-based, outside in), printed duplex with a short-edge flip:

    front: left = n - 2k        right = 2k + 1
    back:  left = 2k + 2        right = n - 2k - 1

Left halves always carry versos (even pages), right halves rectos, because
every signature holds a multiple of four pages and the book starts on a recto.
"""

from __future__ import annotations

from dataclasses import dataclass

from pypdf import PageObject, PdfReader, PdfWriter, Transformation

MM = 72 / 25.4
SHEET_W, SHEET_H = 297 * MM, 210 * MM
FOLD = SHEET_W / 2


@dataclass
class Signature:
    number: int
    start: int  # first book page (1-based, physical)
    pages: int  # pages in this signature, a multiple of 4

    @property
    def sheets(self) -> int:
        return self.pages // 4

    @property
    def end(self) -> int:
        return self.start + self.pages - 1


def plan(total: int, size: int = 16) -> list[Signature]:
    """Signatures of `size` pages; a short tail is evened out, never thinner than 8.

    The book is padded to a multiple of 4 with blank pages at the end. A
    remainder of 12 makes a 12-page last signature; 8 becomes 12 + 12 in
    place of the last 16 + 8; 4 becomes 12 + 8 in place of 16 + 4, so no
    signature is a single sheet (too thin to sew well).
    """
    if size % 4:
        raise ValueError("signature size must be a multiple of 4")
    padded = -(-total // 4) * 4
    full, rem = divmod(padded, size)
    sizes = [size] * full
    if rem:
        if size == 16 and rem in (4, 8) and full:
            sizes.pop()
            sizes += [12, 8] if rem == 4 else [12, 12]
        else:
            sizes.append(rem)
    sigs, start = [], 1
    for i, n in enumerate(sizes, 1):
        sigs.append(Signature(i, start, n))
        start += n
    return sigs


def sides(sig: Signature) -> list[tuple[str, int, int, int]]:
    """(side, sheet, left page, right page) per printed side, book page numbers."""
    out = []
    n, s0 = sig.pages, sig.start - 1
    for k in range(sig.sheets):
        out.append(("front", k + 1, s0 + n - 2 * k, s0 + 2 * k + 1))
        out.append(("back", k + 1, s0 + 2 * k + 2, s0 + n - 2 * k - 1))
    return out


def fold_order(sig: Signature) -> list[tuple[int, str, str]]:
    """Independent check: walk the folded, nested sheets and list which
    (sheet, side, half) each successive page lands on.

    Opening the folded signature from the front, the right half of each
    sheet's front comes first, outside in, with its verso on the back left;
    past the centre the back right and then the front left come back out.
    """
    order = []
    for k in range(1, sig.sheets + 1):
        order += [(k, "front", "right"), (k, "back", "left")]
    for k in range(sig.sheets, 0, -1):
        order += [(k, "back", "right"), (k, "front", "left")]
    return order


def cell_origin(half: str, page_w: float, page_h: float) -> tuple[float, float]:
    ty = (SHEET_H - page_h) / 2
    return (FOLD - page_w if half == "left" else FOLD, ty)


def impose(reader: PdfReader, sig: Signature, total: int, marks: list[PageObject] | None = None):
    """A PdfWriter with this signature's sides in print order (front, back, ...)."""
    w = PdfWriter()
    pw = float(reader.pages[0].mediabox.width)
    ph = float(reader.pages[0].mediabox.height)
    for i, (_side, _sheet, left, right) in enumerate(sides(sig)):
        sheet = PageObject.create_blank_page(width=SHEET_W, height=SHEET_H)
        for half, p in (("left", left), ("right", right)):
            if p <= total:
                tx, ty = cell_origin(half, pw, ph)
                sheet.merge_transformed_page(reader.pages[p - 1], Transformation().translate(tx, ty))
        if marks is not None:
            sheet.merge_page(marks[i])
        w.add_page(sheet)
    return w


def side_label(sig: Signature, side: str, sheet: int, left: int, right: int, total: int) -> str:
    def pg(p: int) -> str:
        return str(p) if p <= total else f"{p} (blank)"
    return (
        f"Signature {sig.number} · PDF pages {sig.start}–{sig.end} · "
        f"sheet {sheet} of {sig.sheets} · {side.upper()} · left {pg(left)} | right {pg(right)}"
    )

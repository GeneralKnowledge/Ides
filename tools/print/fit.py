"""Copyfitting: fill short pages by setting one paragraph a hair tighter or looser.

The typesetter keeps widows and orphans off the page by moving a line over,
which leaves the page above a line short. A compositor would instead take a
paragraph on that page and set it a fraction tighter (to save a line) or
looser (to make one), within limits a reader does not notice. This does the
same, page by page within each section: try the likeliest paragraphs, keep an
adjustment only if the page then fills, and otherwise leave the page short.
Sections start on fresh rectos, so they are fitted in parallel.

The words are never touched: an adjustment changes letter and word spacing
only (see `fit-levels` in book1.typ).
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import qa

MAX_TRIES = 9


@dataclass
class Para:
    id: str
    sid: int
    kind: str
    page: int
    end_page: int
    lines: int
    last_frac: float


@dataclass
class Target:
    offset: int  # page within the section, 0 = opening page
    candidates: list[tuple[str, int]]
    tries: int = 0
    pending: tuple[str, int] | None = None


@dataclass
class Result:
    adjust: dict[str, int] = field(default_factory=dict)
    iterations: int = 0
    fixed: int = 0
    left_short: list[tuple[int, int]] = field(default_factory=list)  # (sid, offset)


def paragraphs(marks: list[dict], data: dict) -> dict[str, Para]:
    starts = {m["id"]: m for m in marks if not m["end"]}
    out = {}
    for m in marks:
        if not m["end"]:
            continue
        s = starts[m["id"]]
        sid, j = (int(x) for x in m["id"].split("."))
        left = qa.G.left(m["page"])
        out[m["id"]] = Para(
            id=m["id"], sid=sid, kind=data["sections"][sid]["blocks"][j]["t"],
            page=s["page"], end_page=m["page"],
            lines=round((m["y"] - s["y"]) / qa.G.lh) + 1 if s["page"] == m["page"] else 0,
            last_frac=(m["x"] - left) / qa.G.text_w,
        )
    return out


def candidates(page: int, paras: dict[str, Para]) -> list[tuple[str, int]]:
    scored = []
    for p in paras.values():
        # A paragraph running over to the next page was usually split to keep
        # a widow off it: one line less, or one more, lets it fill this page.
        if p.kind in ("p", "bullet") and p.page == page and p.end_page == page + 1:
            scored.append((2 - abs(p.last_frac - 0.5), p.id, -1 if p.last_frac < 0.5 else 1))
            scored.append((1.5 - abs(p.last_frac - 0.5), p.id, 1 if p.last_frac < 0.5 else -1))
            continue
        if p.kind not in ("p", "bullet") or p.page != page or p.end_page != page:
            continue
        if p.lines >= 2 and p.last_frac < 0.4:
            scored.append((0.4 - p.last_frac + 0.03 * p.lines, p.id, -1))
        if p.last_frac > 0.55:
            scored.append((p.last_frac - 0.55 + 0.03 * p.lines, p.id, 1))
    scored.sort(reverse=True)
    first = [(pid, d) for _, pid, d in scored[:6]]
    second = [(pid, 2 * d) for _, pid, d in scored[:3]]
    return (first + second)[:MAX_TRIES]


def fit(src: Path, pdf: Path, data: dict, compile_reading, query_marks, max_iter: int = 80,
        log=print) -> Result:
    res = Result()
    targets: dict[int, Target] = {}
    settled: dict[int, int] = {}  # sid -> pages before this offset are done
    adjust_file = src / "adjust.json"
    for it in range(1, max_iter + 1):
        adjust_file.write_text(json.dumps(res.adjust, indent=0, sort_keys=True))
        compile_reading()
        paras = paragraphs(query_marks(), data)
        pages = qa.read_pages(pdf)
        main = qa.find_main_start(pages)
        short = qa.short_pages(pages, main)
        sec_start: dict[int, int] = {}
        page_sid: dict[int, int] = {}
        for p in paras.values():
            sec_start[p.sid] = min(sec_start.get(p.sid, p.page), p.page)
            for n in range(p.page, p.end_page + 1):
                page_sid.setdefault(n, p.sid)
        # Judge last round's attempts.
        for sid, t in list(targets.items()):
            if t.pending is None:
                continue
            page = sec_start[sid] + t.offset
            if page not in short:
                res.fixed += 1
                settled[sid] = t.offset + 1
                del targets[sid]
            else:
                del res.adjust[t.pending[0]]
                t.pending = None
        # Next attempt per section.
        busy = False
        short_by_sid: dict[int, list[int]] = {}
        for n in sorted(short):
            if n in page_sid:
                short_by_sid.setdefault(page_sid[n], []).append(n - sec_start[page_sid[n]])
        for sid, offsets in short_by_sid.items():
            todo = [o for o in offsets if o >= settled.get(sid, 0)]
            if not todo:
                continue
            t = targets.get(sid)
            if t is None or t.offset != todo[0]:
                page = sec_start[sid] + todo[0]
                t = targets[sid] = Target(todo[0], candidates(page, paras))
            while t.tries < len(t.candidates) and t.candidates[t.tries][0] in res.adjust:
                t.tries += 1
            if t.tries >= len(t.candidates):
                res.left_short.append((sid, t.offset))
                settled[sid] = t.offset + 1
                del targets[sid]
                busy = True  # look at this section's next short page next round
                continue
            t.pending = t.candidates[t.tries]
            t.tries += 1
            res.adjust[t.pending[0]] = t.pending[1]
            busy = True
        log(f"  fit round {it}: {len(short)} short pages, {len(res.adjust)} adjusted paragraphs")
        res.iterations = it
        if not busy:
            break
    else:
        raise SystemExit("copyfitting did not settle; rerun with --no-fit to inspect")
    adjust_file.write_text(json.dumps(res.adjust, indent=0, sort_keys=True))
    return res

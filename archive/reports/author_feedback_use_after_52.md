# How author feedback was used (after merge of #51 / #52)

**Status:** Process guidance for the next read — not a new edit commission.  
**Sources:** Author reading notes (#51); golden-read P0–P3 implementation (#52); author clarification on selective use.

---

## Core distinction

General comments shaped **editorial principles**. Implementation was **deliberately selective**.

It was not: copy four or five examples into the manuscript.  
It was not: systematically apply every observation across all 34 chapters.

Examples were treated as **evidence of possible underlying problems**, not as instructions to reproduce the same fix everywhere.

---

## How feedback was actually used

### 1. General comments → editorial principles

Recurring problems to investigate (not isolated typos):

- readers losing bearings
- characters talking rather than acting
- prose with AI-like corrective habits
- relationships lacking personal depth

### 2. Changes concentrated in selected scenes

| Concern | Where work landed |
|---------|-------------------|
| Place-first | Ch 5–7, 12–19 (selected doors) |
| Prose hygiene | Selected passages; not every antithesis/em dash book-wide (~711→666 in prose) |
| Character attitude | Specific moments in Ch 4, 8, 16–18, 21–24, 30 |

### 3. Some comments → decisions **not** to change

| Comment | Decision |
|---------|----------|
| No clear single protagonist | Opening cost of ensemble; **no** Octavian-centred rewrite |
| Dream / omens as through-beat | Plant → peak → aftermath; **no** certified precognition |
| Batiatus comparison | Strengthen Hordeonius; **no** new OC |

---

## Mapping: observation → what was implemented

| General observation | What was implemented |
|---------------------|----------------------|
| Everyone talking rather than driving | Specific action-first beats (Hordeonius, Nysa, Laberius) — not a book-wide action rewrite |
| Opinions / relationships need depth | Brutus↔Caesar closeness/guilt; Antony→Octavian — **not** every major dyad |
| Readers lose bearings | Place cues at selected openings — not scenery over every chapter |
| AI-like contrasts / em dashes | Selective cuts — not a full scrub |
| Dream/omens as thread | Contested packet structure; ambiguity held |
| No character carrying the whole story | Judged intentional ensemble cost — not grounds for single-hero retrofit |

---

## Assessment (author)

The process respected intention: examples → underlying problems, not universal paste of the flagged fix.

**Limitation:** Implementation notes show feedback became specific changes and decisions. They do **not** prove every instance of those problems was found or fixed.

Examples of the gap:

- “Clever rate-sheet voice” is broader than Hordeonius; targeted beats may help without resolving the wider voice habit.
- “Opinions underdeveloped” was not turned into a systematic review of every important relationship.

---

## Recommendation for next read

1. **Do not** launch another full-book pass yet.
2. **Do not** mistake merged #52 for proof that every general concern is resolved.
3. Guide the next read by whether the **underlying problems still feel present** — not by whether every original example has been edited.

**Aim:** improve the novel’s underlying behaviour, not only make the passages that happened to be flagged look better.

---

## Also lock (was under-specified)

### Scope of evidence

The notes + #52 rest on **Ch 1–6 + golden Ch 14–19** only. **Ch 7–13 and Act 4–5 were unread** in that pass.

- Silence about an unread chapter is **not** proof it is fine.
- Do **not** invent mid/late-book commissions from that silence.
- Prefer the next read to *feel* those zones (or an outside reader on a clean DOCX) before scheduling work there.

### Standing non-goals (unless a concrete later read forces reopen)

- No Ch 1–3 polish wars without a concrete reason
- No Philippi expand; no mid-book redesign; no new audit / test suite
- No blank-verse funeral; no Pharsalus prologue
- No certified psychic; no baker conspiracy / slang glossary pass
- No new Batiatus OC; no new mobile follow-OC
- No single-hero / Octavian-early / grain-quest retrofit
- Campbell/Vogler = diagnostic only

### Author clarifications override first phrasing

Example: funeral “too short” was withdrawn; the real issue was the **one-beat pyre→buildings cut**. Process must prefer the corrected framing, not the first wording.

### Soft risks left *inside* #52 (watch on re-read, don’t scrub yet)

- Hordeonius caption crumbs that explain the joke
- Dream plant line slightly meta (“rehearsed a dream before…”)
- Ch 20 dream-versions list a bit neat
- Mobile “transfer” labels a bit loud

These are over-clarity risks in the *fixes*, not unfinished examples from the notes.

### When to escalate beyond selective work

| If next read still feels… | Then consider… | Not… |
|---------------------------|----------------|------|
| Unmoored *after* recruitment / Ides / name (not only Ch 1–5) | Connective recoverability; whose ordeal is feelable | Single-hero rewrite |
| Talk/metaphor still dominates entertainment | More action-first / staged irony in existing carriers | Book-wide quip pass or new OC |
| Relationships still flat as functions | Spot-check 1–2 further dyads | Universal relationship essay |
| Rate-sheet cleverness everywhere | Voice hygiene beyond Hordeonius samples | Another full LLM scrub by default |

### Preferred shape of the next read

Not another edit pass. Prefer one of:

1. **Re-read touched zones** (Ch 1–6, 10–11, 14–24, 30) asking “do the underlying behaviours still jar?”
2. **Sample unread mid/late** (Ch 7–13 or Act 4–5) only to learn whether silence hid problems — still no commission from one chapter
3. **Outside-reader DOCX** (craft metadata already stripped in #50) for bearings / follow / entertainment without editorial memory

Stop and note; do not immediately implement mid-read.

### Dual engines stay the carriers

Ides incomplete-info and will/name/heir remain behavioural engines. Do not invent a third master throughline from reading notes (grain quest, seer arc, tour-guide servant).

---

## Pointers

- Notes archive: `archive/reports/author_reading_notes_post_merge.md`
- P3 decisions + diagnostics: `continuity/expansion/golden_read_p3_decisions.md`
- Export craft-strip (reading DOCX): PR #50 / `tools/export_book1_docx.py`

# Author reading notes — post-merge (Oct 2026)

**Status:** Historical reader observations while reading the live draft on `main` after PRs #48–#50.  
**Not** a phase plan, audit, or edit commission. Preserve so the notes are not lost to chat context.

**Context:** Housekeeping stopped; DOCX regenerated; author reading Book 1 as a reader.

---

## 1. Continuity-receipt voice at chapter doors

**Catch (Ch 2 opening):**

> Africa still hit the stalls like a price change with blood in it.

Chapter 1 *does* establish Africa (New-Africa, Thapsus, triumph dust), so the fact is not unearned. The problem is stance: “**still**” addresses a reader who has already filed Africa, rather than letting Hordeonius meet the day’s Forum weather cold. The scene title (“Africa Still Prices”) reinforces continuity-receipt voice. The next line (“Thapsus,” someone said, as if the name were fresh) is closer to the better way in.

**How widespread (spot-check, not full audit):**

- Not every “still” is this problem — many are ordinary sensory persistence (dirt still drying, toga that could still show holes).
- Sticky pattern: openings that treat a prior plant as already in the reader’s brief.
- Cousins of the Ch 2 catch include joins like Ch 7’s “festival was still sticky… the diadem’s ghost.”
- Worth a private list of openings that *address the briefed reader*; fix later only where it jars. Do **not** reopen Ch 1–3 wholesale mid-read without a concrete reason.

---

## 2. Export craft-metadata leaks (fixed)

Reading DOCX had been leaking craft lines such as:

> **G1:** Second POV — collides with F4’s unfinished question (closed Africa → what victory costs on the street / at the house)

**Cause:** Exporter only stripped fully-bold lines and middot banners; `**G1:** …` / `**Opening prose pass:** …` fell through as body.

**Fix:** PR #50 — strip all leading-`**` craft lines; fail loud if tags still appear. Regenerated FULL/Golden DOCX on `main`.

Scene titles from manuscript SC headers (e.g. “Africa Still Prices”) remain as section breaks — intentional, not the G1 tag class.

---

## 3. Seius — does he return?

Yes. Recurring F2 POV, not a one-chapter walk-on:

| Chapter | Role |
|---------|------|
| 3 | Atrium nod, soft debt, Seia Prima audit |
| 7 | Pale in Lupercalia crowd (Antony notices) |
| 10 | Almost-recruited at baths; flinches |
| 23 | Refuses petition signature; spends neighbour goodwill |
| 30 | Name off proscription lists; near-cognomen scare |

Ch 18 only uses “Seius’ type” as comparison. No further full turn after the lists in Book 1.

---

## 4. Dropped into rooms without place

**Reader feeling:** Often hard to know where we are.

**Verdict:** Real house habit, not imagination.

- Draft often opens on **who wants what**, not **where we are**. Place arrives via props a beat later (couch/cup/fish; atrium smell; exits/togae/statue) or stays thin.
- When place lands early (camp mud, vestibule smell, burned street), orientation is easy — those openings are the minority.
- **Export compounds it:** `Date / place:` lines in the `.md` files are stripped as metadata, so the reading DOCX removes an explicit “you are here” the source still has.

**Later (only if pursued):** Orientation helps at chapter/scene doors where the social move starts before the walls exist — not a manuscript-wide scenery dump, and not a reason to reopen the opening while still reading.

---

## 5. Early-read hypothesis (author @ Ch 5) — who carries the story?

**Caveat from author:** only through Chapter 5; may not hold for the whole book.

**Feeling:**

- No subconscious “main character” to follow.
- Nothing is carrying the story yet.
- Possible fixes floated: more Octavian in more situations; a grain throughline; some people have too much / too little; too much jammed into one book; maybe “too historical” without a dramatic through-line earning it.

**What the manuscript is designed to do (for testing as you continue, not as a veto):**

- **Ensemble by intention**, not a single protagonist. Regular historical rotation (Decimus, Brutus, Cassius, Antony, Cicero; Octavian peripheral early, rising later) plus fictional street/household cameras (Nysa, Seius, Laberius, Hordeonius).
- **Ch 1–5 specifically:** Cassius dinner → Hordeonius/Nysa street → Seius debt → Laberius/Brutus/Decimus Spain–Rome → **first Octavian chapter**. So by Ch 5 you have already changed camera five times before any Ides machinery starts. That can feel like “nobody owns the book” even if later Decimus / name-war / Philippi threads thicken.
- **Declared engines** (behavioural, not a person): (A) Ides incomplete-information detective; (B) who owns the dead man’s afterlife (will / name / heir). Grain, land, unpaid dirt are *weather and cost*, not currently a single named throughline with one follower.
- **Octavian:** designed as furniture → claim → pay; heavy only from Act 4 onward. Moving him earlier would be a real structural choice, not a polish.

**How to use this note while reading:**

- Watch whether someone (or an engine) starts to *carry* you after Ch 7–9 (recruitment / Decimus door) or after the Ides / funeral / name chapters.
- If by mid-book you still feel unmoored, the Ch 5 hypothesis graduates from “opening fog” to “architecture problem.”
- If a follow-character or grain spine emerges for you later, the early fog was the cost of the ensemble start — still worth remembering, not automatically a redesign.

**Do not yet:** redesign around Octavian, invent a grain quest, or split the book on the strength of Ch 1–5 alone.

---

## What not to do with these notes

- Do not turn them into a new audit framework or test suite.
- Do not reopen Chapters 1–3 without a concrete reason.
- Do not commission another broad prose pass from this list alone.
- Prefer finishing the read and gathering outside-reader feedback before large editorial decisions.
- Treat §5 as an **open hypothesis** until more chapters have been read.

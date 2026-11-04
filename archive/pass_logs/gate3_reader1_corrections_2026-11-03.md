# Gate 3, reader 1: triage and correction round (2026-11-03)

**Purpose and scope (§5):** the first independent reader's written review of the full DOCX export (main at 4804bc8). Every point classified under `writing/FINAL_READINESS_GATE.md` Gate 3. Reuben approved the recommended split on 2026-11-03: 11 "do now", 7 held for reader 2 and 4 declined. This file records the one correction round for the "do now" items. The held items wait for reader 2's notes, and then they and reader 2's points get one combined round.

Triage doc (decision dropdowns): https://claude.ai/artifact/GiTwf8oHRXF6gY377Y1Hdq. Summary of the review: project files `reports/gate3/reader1_review_2026-11-03.md`.

Built on PR #188 (missing-step audit), which touches the prologue and Ch 4, 13, 23 and 32.

## Accepted and done

| # | Point | Class | Fix |
|---|-------|-------|-----|
| 1 | Prologue a false start | Reader response | Ch 34 SC-88b: when Brutus reads the three versions of Porcia's death, he remembers her father watched at Utica, the sword taken and the wound sewn, and Cato opening it again. Moved from Ch 31 (as triaged) to Ch 34 because that is where Brutus learns *how*; Ch 31 has him refuse to hear it. |
| 3 | Nysa's wax burned without consequence | Reader response | Ch 19 SC-51: before she burns it she knows which consul the fragment meant: the one she watched turn the city with the gown that afternoon. Burning still changes nothing (NOTE-1 and the knowledge ban hold). |
| 4 | Price motif worn thin | Reader response (repetition, §1 light rule) | Ch 23: cut "Hordeonius priced the smell" and "priced the Puteoli question twice" (both repeat the stall's pricing already shown). Ch 32 SC-85: cut the interest-on-sleep line, "bookkeeping virtue", "Informers priced breath" and the March-smoke fragment. Kept: the Ch 32 SC-85c Atticus "kindness cleared at a rate no banker could match" beat. |
| 6 | Brutus's interiority repeats | Reader response (repetition) | Ch 34: cut "The GO night's clean hands felt suddenly like someone else's" and "brand as comfort, brand as trap". Ch 26: two warmth fragments folded into their sentences. Kept: Ch 17 "a man who forgave me" (the reader's own example of the clear statement) and the Ch 26 → Ch 34 warmth arc, which develops rather than repeats. |
| 8 | Decimus's death reported in two lines | Clarity defect | Ch 31 SC-82: the ford scene now names Camelus, the Gallic chief once in Decimus's pay, who holds him a night until Antony's rider comes; his man strikes at the neck (Appian *BC* 3.98). Octavian's courier line now reads "a Gaul called Camelus, and Antony's purse". |
| 10 | Fragments as default rhythm | Reader response; extends habit I (#186) | Verbless narration fragments folded: Ch 15 "Not a speech-sound. Not a vote-sound"; Ch 16 "One door. Too many togas", "Or half-sat", "The slight turn. The listening face", "Togas with red. Togas without dignity"; Ch 19 "Grief wanting a relic"; Ch 20 "Three versions. One pitch smell"; Ch 24 "Dust on him"; Ch 31 "Appearances, even here"; Ch 35 auction quarrels; Ch 36 "The orator's son". Left alone: short sentences with a verb; lists of news or rations; Cassius's perception at Philippi (Ch 35, "A shout. Arms round a body."), where the stop is the event. |
| 11 | "Not X. Y" antithesis | Reader response | Cut or folded: Ch 7 "useful, not urgent"; Ch 8 "not early, not late"; Ch 12 "necessary, costly, not optional"; Ch 13 "present as weight, not as a hymn"; Ch 17 Lepidus "not weak, not heroic"; Ch 28 "not mercy, timing"; Ch 34 "shame, not cleverness"; plus the Ch 15 and Ch 16 folds above. Dialogue left alone. |
| 12 | Soft, clean, warmth overused | Reader response | About twenty figurative uses cut or replaced: Ch 2, 6 (thesis line), 8, 12, 13, 14, 15 (×2), 16 (×3), 17, 19, 20 (×2), 21 (thesis line), 22, 24 ("soft power", also a modern concept → "Servilia rearranged his sentences"), 32 (thesis line), 34, 36. Kept: "soft chain" (load-bearing brand), Hordeonius's own *soft* vocabulary in Ch 10 (SIDE-1 ledger entries), *Clean* as his cipher, literal warmth and cleanliness, and the Ch 26 → 34 warmth arc. |
| 13 | Anachronistic idiom | Preference, one valid | Ch 36 steward: "It's a good house to be in, this spring … by the summer" → "There is bread in this house this spring … By the summer there may be soldiers at its door." Others kept (plain English, not modern concepts). |
| 14 | Scene titles read like notes | Reader response | `tools/export_book1_docx.py` and `tools/print/content.py`: scene titles no longer reach the reader; an unnamed break (three spaced points) marks each scene after the first in a chapter. The manuscript keeps its titles as working labels. `tools/print/docs.py` text updated. |
| 16 | Spare-Antony framed only as optics | Historical defect | Ch 9 SC-23: Brutus adds the hope Plutarch gives him (*Brut.* 18), that Antony, with Caesar gone, might be won to the Republic by the honour of saving it. Trebonius's following line now answers it. |
| — | Planning language in prose | Defect (24 Oct validation P2) | Ch 8 "the Appian shortlist's edges" → "the others … whose villas lined the Appian Way south of the city"; Ch 13 "the Appian edges" line rewritten. |

## Held for reader 2

2 compress Act 2 (Ch 8, 9, 12, about 15–20%); 5 a mistake Cassius owns; 7 Antony's interiority; 9 Cleopatra's one scene; 15 rumour around the wrong Cinna; 20 single protagonist / fold Amyntas; 21 Act 5 weight (split Ch 31 and 32).

## Declined

- 17 Trebonius's hold rushed: about 15 paragraphs, close to Plutarch's brief account.
- 18 Nysa at Julia's house: Julia's arms turn the centurion (Plut. *Ant.* 20), not Nysa's lie; #188 fixes "mistress's mother".
- 19 Twelve vultures: Appian *BC* 3.94 (six, then six) and Suetonius *Aug.* 95 (twelve) are both followed.
- 22 Nits: Suetonius *Jul.* 37 has the four triumphs "in the same month, with days between"; the spears of Mars in the Regia are a recorded prodigy (Gellius 4.6).

## Checks

- `python tools/export_book1_docx.py --check`: OK, 36 chapters, 2840 reading paragraphs, no leaks.
- Print interior rebuilt with `tools/print/build_book1_print.py` (word read-back check against the manuscript).
- Changed passages re-read in place with their neighbours (§5.4); no chapter re-audited.
- Reading words after the round: about 90,350.

## Open items

- Reader 2 is still needed for Gate 3; the triage doc's held rows go to that round.

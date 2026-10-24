# Story graph pass and padding check (2026-10-24)

**Why:** Reuben asked for a comprehensive fix for the gaps the story graph found (artifact “Book 1 story graph”), and a check for sections that had grown for the sake of length.
**Scope:** prologue and Ch 1–36 on main @ 13e936a. Development (HUMAN_VOICE_RULES §1a) for the graph gaps; revision (§1) only for passages that repeat what a newer scene already shows.
**Result:** reading words 89,760 → 89,121 (about 1,550 cut, about 900 added).

---

## 1. Padding check

**Method.** Word count of every chapter at every commit since the import (`git log --follow`), then a read of the chapters that more than doubled in the last week, looking for a passage that retells what a newer scene now shows, a recap of news the reader has just watched, or a closing paragraph that restates the scene.

**What grew.** Acts 1–3 grew in the reader-earn expansions of 19–21 October (Ch 1 554 → 1,543; Ch 4 1,613 → 2,403; Ch 13 1,304 → 2,240). Those passages were reviewed twice and copyedited, and a spot read found no seams. Acts 4–5 roughly tripled between 23 and 24 October:

| Ch | Before T8–T13 / S1–S5 | Now | What came in |
|----|------|-----|------|
| 21 | 1,638 | 3,696 | T10 Trebonius market day; T10 column; T13 Porcia |
| 27 | 1,599 | 3,528 | T9 Brundisium, Casilinum, the oath |
| 30 | 1,015 | 3,753 | S4 Forum Gallorum; T12 the pun |
| 31 | 1,750 | 5,465 | S3 Cularo; S5 the march on Rome |
| 32 | 1,614 | 6,126 | T11 Julia’s door, Gavius, Surety, Twice the Price |
| 33 | 760 | 3,335 | T11 Brothers, Hortensia |
| 34 | 1,257 | 4,700 | T8 the cedar box; T10 Laodicea; S1 Sardis |
| 36 | 1,437 | 4,093 | Nysa and Laberius endings |

**Finding.** The new scenes are real scenes with choices in them, and they are not padding. The padding is at the seams: the older summary passages from the first draft batches were left in place beside the new scenes that now dramatise the same events, and some scenes from those batches repeat a motif three or four times (the wine-shop “squeak” and “shadow” jokes in Ch 21–22; the overheard verdict after a scene).

**Cut** (each a passage that repeats something the reader has just been shown):

- Ch 21: the second courier’s contradictions; the third “wine-shop sport” report; the client trio in Cage with a View (the clerk scene keeps the signature beat); the closing restatement. The chapter now ends on Porcia.
- Ch 22: the courtyard elders’ “exercising” echo of Ch 21; three restating paragraphs in The Boy.
- Ch 23: one of three “watch Servilia” lines.
- Ch 24: Antony’s man’s second offer; the colonnade clients’ closing verdict.
- Ch 25: the mate’s speech (replaced by the Trebonius letter, below).
- Ch 27: the Sextus margin note and a filler courier; the queen’s return kept in two sentences.
- Ch 30 Mud: the Pansa-litter recap and the Capua/pay talk that Forum Gallorum now carries.
- Ch 31: the aide’s recap of the Lepidus news (Allies Evaporate already shows it); the “gods’ gift” senator.
- Ch 34: the courier’s news list cut to essentials; two closing restatements.
- Ch 35 and 36 (Philippi, protected): three stacked thesis lines after Cassius’s act; the duplicate “shrinking knot” in Brutus’s section; the second crown-refusal in Octavian’s; one corridor line in Peak. Only restatements were cut.

**Kept on purpose:** Formiae (Ch 33, protected); the gold spine (Ch 14–19) except the Ch 18 stitch below; the Ch 32 proscription scenes; Agrippa’s “homework with fasces”; the Sextus and queen plants that later chapters need.

## 2. Graph fixes

| Graph finding | Fix | Where |
|---|---|---|
| Seius off the page Ch 11–22 | Seius at the stall the week after the Ides asks to roll the canvass debt; Hordeonius asks for the Sabine farm and is refused; two and a half in the hundred instead | Ch 18 (development touch in the gold spine: one exchange replacing the unnamed junior) |
| Seius off the page Ch 24–31 | His interest arrives a day early with the extra half, carried by Dromo | Ch 30 |
| Hordeonius only prices other men’s choices before Ch 30 | Keeping Seius instead of calling him is his choice; the farm request pays in Ch 32 | Ch 18, 32 |
| Trebonius absent and unmentioned Ch 22–28 | His June letter from Smyrna in Cassius’s belt; Marcus Cicero’s dinner with him in Athens | Ch 25, 26 |
| Invented four never named by others | Octavian hears of “one girl in Antony’s kitchen” and sets Agrippa to find her (Nysa); Laberius’s plot copied to Agrippa’s list; Fulvia’s woman’s creditor column with *Hordeonius, at the Janus*; Rufrius names Laberius to Antony | Ch 31, 33, 35 |
| Laberius’s decisions touch nobody | Rufrius, spared at Forum Gallorum, asks Antony for the place on Laberius’s left at Philippi, and Antony gives up a quarter hour on the hill for it | Ch 35 |
| Decisions rarely cross storylines before Ch 23 | The Ch 18 rollover (Ides → canvass → farm → Gavius’s escape); Decimus’s true grain count arms Cicero’s motion for Octavian | Ch 18, 28 |
| Ch 28 only delivers plot | Decimus chooses to send the true number; Octavian chooses to march to rescue the man who walked Caesar in | Ch 28 |
| Ch 29 Amyntas only witnesses | He keeps back the orphans’ dowry book; says nothing to Cassius in Ch 34 | Ch 29, 34 |
| Fulvia’s ledgers (Ch 32) never seen | Her woman’s creditor column; she prices Hordeonius’s rate and does not borrow | Ch 33, 36 |

Each touched chapter has a “Graph pass 2026-10-24” line in its continuity notes.

**Not done:** G15 Galba’s debt (deferred by Reuben), G14 Brutus’s creditor as a person (Investigate).

*End story graph pass.*

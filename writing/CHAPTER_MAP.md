# Chapter Map — Draftable Units for LLM Pass

Maps scene cards → suggested chapter groupings. Titles are working labels only.

**Authority:** This map is a **structural preference** (preferred units for drafting and Continuity indexing), not a historical invariant. The same narrative requirement may be delivered by a different chapter/SC bundling if dramatic merit, anchors, and Continuity notes hold. See [`continuity/lock_architecture_audit.md`](../continuity/lock_architecture_audit.md) and `continuity/canon.md` lock tiers.

**Drafting instruction:** One chapter ≈ 1–3 scene cards. Generate **one chapter at a time**.

---

## ACT 1 — The Hollow Republic (c. 46 – 15 Feb 44)

| Ch | Scene cards | Primary POVs | Must-express |
|----|-------------|--------------|--------------|
| 1 | SC-08 | CAS | Clemency dinner (**D**, late 46); Africa-favour climber Sextilius; queen/child rumour |
| 2 | SC-01, SC-02 | F4, F1 | Cato/Africa market weather; spectacle residue; land hunger seed |
| 3 | SC-03, SC-04 | F2, F4 | Debt/patronage |
| 4 | SC-05, SC-06, SC-07, SC-09 | F3, BRU, DEC | Munda; Porcia pressure; will whisper (no dinner replay) |
| 5 | SC-10, SC-11 | OCT | Peripheral boy; Apollonia/Agrippa plant |
| 6 | SC-12, SC-14 (SC-13 folded into F4) | CIC, F4 | Dictator perpetuo; Parthia clock; offices market |
| 7 | SC-16, SC-15 | ANT, BRU/CAS | **Lupercalia** then first disclosure (chrono) |

*SIDE-1 body (Ch 10) is early Feb 44, before the Lupercalia: Act 2 is grouped by network, not strict date.*

---

## ACT 2 — The Network (early Feb – 14 Mar 44)

| Ch | Scene cards | Primary POVs | Must-express |
|----|-------------|--------------|--------------|
| 8 | SC-20, SC-21 | CAS, BRU | Recruitment heat; ancestral pressure |
| 9 | SC-22, SC-23 | DEC, CAS/BRU/DEC | Insider trust; **spare Antony** |
| 10 | SC-24, SC-25, SC-25b | F2, F4 | Almost-recruit; debt ask; **SIDE-1 body** |
| 11 | SC-26, SC-27 | F1, CIC | Omens; **manufactured Sibylline talk** |
| 12 | SC-28, SC-29, SC-30 | CAL, F1, CAE | Dread; fragment; Caesar opacity |
| 13 | SC-31, SC-32, SC-33, SC-34 | TRE/DEC, CIC, F3, BRU/CAS | Delay assignment; Cicero blind calm; veterans; GO |
| 14 | SC-35a–d | CAL/CAE/DEC, F1 | **Dreams + Decimus fetch**; Nysa tablet blocked (35d) |

---

## ACT 3 — The Ides (15–c. 20 Mar 44)

| Ch | Scene cards | Primary POVs | Must-express |
|----|-------------|--------------|--------------|
| 15 | SC-40, SC-41, SC-42 (+ SC-54b) | CAL/CAE, DEC, ANT | Morning omens; persuasion; Antony delayed; NOTE-1 unread on route |
| 16 | SC-43, SC-44 | CAS/BRU, F1 | **Murder**; false Antony-dead rumour |
| 17 | SC-45, SC-46, SC-47 | BRU, ANT/LEP, CIC | Capitol; no massacre; amnesty |
| 18 | SC-48, SC-49 | F4, ANT/F1 | Markets; **will** |
| 19 | SC-50, SC-51 | ANT/F1/F3, F1 | **Funeral riot**; **Cinna** |
| 20 | SC-52, SC-53, SC-54 | DEC/BRU, CLEO, OCT | Collapse; exit; delayed OCT |

---

## ACT 4 — The Name (Apr 44 – early 43)

| Ch | Scene cards | Primary POVs | Must-express |
|----|-------------|--------------|--------------|
| 21 | SC-60, SC-61 | CIC, BRU | Letters; Lanuvium cage |
| 22 | SC-62, SC-63 | OCT/CIC, ANT | **Name Caesar**; Antony underestimates |
| 23 | SC-64, SC-65, SC-66 | F4, F1, F2 | Bribes; scavenged house; majority cowardice |
| 24 | SC-67, SC-68a | F3, CIC | Veterans listen; **Antium consilium** |
| 25 | SC-68b, SC-69 | CIC, CAS/BRU | Philippics; East departure |
| 26 | SC-70 (+ CLEO-1/FS11 folded) | DEC | Cisalpine; Cleo/Sextus as rumour-margin only |
| 27 | SC-73, SC-74 | ANT/DEC, OCT | Mutina begins; Senate’s sword |

---

## ACT 5 — Lists and Plains (43–42)

| Ch | Scene cards | Primary POVs | Must-express |
|----|-------------|--------------|--------------|
| 28 | SC-80, SC-81 | F3, rumour | Mutina battles; poison rumour only |
| 29 | SC-82, SC-83 | DEC, OCT | Isolation; consulship |
| 30 | SC-84, SC-85 | OCT, F2/F4/F1 | Triumvirate; **proscriptions** |
| 31 | SC-86 | CIC | **Cicero death** |
| 32 | SC-87, SC-88 | CAS, BRU | Extraction; liberty brand crack |
| 33 | SC-90, SC-91 (SC-89 folded) | ANT/F3, CAS | Philippi I; **Cassius info-death**; OPEN-0 echo only |
| 34 | SC-92–95 (SC-94 in SC-92 breath) | BRU/OCT, ANT, report | Philippi II ordeal; lean SERIES-1 hooks |

---

## Generation batching for an LLM

**Batch A (voice test):** Ch 14–19 (dreams through funeral)  
**Batch B (politics):** Ch 21–24 (name + Antium)  
**Batch C (war):** Ch 28–34  
**Batch D (fill):** Ch 1–13, 20, 25–27  

After each batch: run `MUST_EXPRESS.md` checklist; log new D-inventions into `continuity/canon.md`.

---

## Expansion deposits (architecture-first)

See [`continuity/expansion/beat_deposit_map.md`](../continuity/expansion/beat_deposit_map.md) and [`archive/reports/expansion_integration_review.md`](../archive/reports/expansion_integration_review.md).  
Update this map only after beats are marked **LANDED** there. Review 2.0 was integrate-first; from 2026-10-23 a historical-subplot wave is open (see `continuity/expansion/README.md`). Still no padding toward LEN-1.

| Wave | Chapters | LANDED IDs | Integration flags |
|------|----------|------------|-------------------|
| Soft Middle | 17–24 | D1–D9 | IR-1: D2/D5 earned |
| War social | 25–30 | D10–D15 | D12 optional; D10/D13 light |
| Early mesh | 3, 4, 5, 10, 12 | D16–D18, D20–D21 | IR-1: D16 meta stripped (Ch 3 debt after dinner-first reorder) |
| Ides fringe | 14 | D22 | peaks PROTECT (≠ immunity); Ch 16 = A5 + dream quality |

**Invariants held:** AMB-1 · NOTE-1 dual · SIDE-1 OPEN-0 · OCT≠Augustus · no Actium · A5 Curia death · Formiae.  
**Working staging:** CHOREO-1 — continuity-preferred, revisable with review (not Anchor A5).

# Post-Development Cold Read 1D.6 — Readiness Gate

**Date:** 2026-10-17  
**Inspected commit (HEAD):** `c40bd24000a943e3a9b86db17a15abdff0c593d0` — *Phase 1F: Bononia I2 + E3 local craft fixes (#14)*  
**Branch at inspection:** `main` (clean working tree)  
**Scope:** Analysis only. No chapter rewrites.  
**Method:** Full chronological read of Ch 1–34 against current plans, `editorial_diagnosis_1b.md` (as hypothesis to retest), `craft_editorial_pass_1c.md`, `canon.md`, `CHAPTER_MAP.md`, `MUST_EXPRESS.md`. Phase 1B observations treated as claims to verify, not inherited defects.

**Adjacent work on this tree:** Phase **1F** (Bononia I2 + E3) landed on `main` after 1D.5 and before this gate. Findings for Ch 7/12/1/28/30 include that work.

**Baseline for length delta:** commit `eb776a8` (Craft Pass 1C; post-M5, pre-1D), recounted with the **same** body-word method as current.

---

## 1. Executive verdict

**What the novel has become after Phase 1D (+ 1F):** a canon-held Book 1 that now has **lived consequence** in the places 1B called postcard — Mutina, Decimus’s road, Bononia/lists, Philippi — and **earned deposits** before the knives (Brutus courtesy-burns; Decimus road-trust; Galba’s debt price; GO friction). The Ides gold spine (Ch 14–16, 19) remains the best prose and the dramatic centre, but Acts 4–5 no longer read as a timeline appendix wearing metaphors. Cold-read Ch 20→34 feels like continuous novel consequence with soft connective spots, not an illustrated digest.

**What it is still not:** a 45–70k intermediate manuscript, nor a book ready for external “is this finished?” review. Growth since pre-1D is real but modest (~**+3,700** body words; ~**29,900** now). Remaining problems are mostly **craft concentration** (house-style templates across POVs), **one mid-band energy trough** (esp. Ch 20–21/23 and Decimus’s gap before Cisalpine), and **thin connective tissue** (Ch 32; Decimus ally-evaporation asserted inside Ch 29) — not missing historical pivots or broken locks.

**Frank readiness:** Choose **Gate B** (see §10). Structure is sound enough for a **light, targeted house-style / local continuity pass**. Another ordeal-development wave is not justified by missing P0 causality. External developmental review is premature while template fatigue and mid-band trough remain unaddressed.

---

## 2. Exact word-count and chapter distribution

### Counting method (reproducible)

Body words = tokens matching `\b[\w']+\b` after stripping:

- `# Chapter` / `# SC-` / `###` beat labels  
- Banner lines (`**Phase…**`, `**M5…**`, `**Canon:**`, etc.)  
- Scene metadata lines (`POV:`, `Date / place:`, `Canon refs:`, `Info ENTER/EXIT:`, `Overhear risk:`)  
- `---` separators  
- Entire `## Continuity…` blocks (including mid-chapter continuity notes) until the next `# SC-` / `# Chapter`  
- `# Chapter … End matter` sections and trailing `**Rollup**` / polish lines  

Script equivalent used at inspection; re-run against any commit for comparison.

### Snapshot

| Metric | Value |
|--------|-------|
| HEAD SHA | `c40bd24000a943e3a9b86db17a15abdff0c593d0` |
| Chapter files present | **34 / 34** |
| Current body total | **29,936** |
| Pre-1D baseline (`eb776a8`, same method) | **26,257** |
| Net change | **+3,679** (~+14%) |
| Mean chapter (current) | ~880 |
| 1B reported baseline (different pass, ~26,240) | Compatible within method noise; do not treat as identical census |

### Limitations of the comparison

- 1B’s ~26,240 used a similar but not identically scripted strip; this gate recounts both ends with one method.  
- Phase **1F** is included in “current” but was not part of the five 1D batches; ~Ch 30/7/12/1 deltas partly reflect 1F.  
- Gold-spine chapters (14–16, 19) were not bulk-expanded (correct under locks); act-share shifts come from Acts 2/4/5 growth.

### By chapter (current body words)

| Ch | Words | Ch | Words | Ch | Words | Ch | Words |
|----|------:|----|------:|----|------:|----|------:|
| 1 | 519 | 10 | 875 | 19 | 981 | 28 | 797 |
| 2 | 629 | 11 | 536 | 20 | 837 | 29 | 995 |
| 3 | 511 | 12 | 697 | 21 | 792 | 30 | 1014 |
| 4 | 1060 | 13 | 1029 | 22 | 986 | 31 | 618 |
| 5 | 528 | 14 | 2318 | 23 | 610 | 32 | 673 |
| 6 | 622 | 15 | 1308 | 24 | 887 | 33 | 966 |
| 7 | 723 | 16 | 1172 | 25 | 754 | 34 | 1064 |
| 8 | 1022 | 17 | 1113 | 26 | 919 | | |
| 9 | 638 | 18 | 847 | 27 | 896 | | |

### By act (current)

| Act | Chapters | Words | Share |
|-----|----------|------:|------:|
| 1 | 1–6 | 3,869 | 12.9% |
| 2 | 7–13 | 5,520 | 18.4% |
| 3 | 14–20 | 8,576 | **28.6%** |
| 4 | 21–27 | 5,844 | 19.5% |
| 5 | 28–34 | 6,127 | 20.5% |

**Act-share change vs 1B picture:** Act 3 remains densest but no longer ~33% of a 26k book in the same way; Acts 4–5 together (~40%) now roughly balance Act 3. The “Ides novella + appendix” length geometry is **materially softened**, not erased.

### Chapters that materially changed in Phase 1D / 1F

(|Δ| ≥ 40 body words vs `eb776a8`)

| Ch | Before → After | Batch |
|----|----------------|-------|
| 4 | 733 → 1060 | 1D.4 |
| 7 | 648 → 723 | 1F E3 |
| 8 | 807 → 1022 | 1D.4 |
| 12 | 629 → 697 | 1F E3 |
| 13 | 802 → 1029 | 1D.4 |
| 21 | 646 → 792 | 1D.5 |
| 22 | 714 → 986 | 1D.5 |
| 24 | 710 → 887 | 1D.5 |
| 25 | 621 → 754 | 1D.3 |
| 26 | 608 → 919 | 1D.1 |
| 27 | 622 → 896 | 1D.1 |
| 28 | 611 → 797 | 1D.1 (+1F recheck) |
| 29 | 621 → 995 | 1D.1 |
| 30 | 732 → 1014 | 1D.3 + **1F I2** |
| 32 | 623 → 673 | 1D.3 |
| 33 | 729 → 966 | 1D.2 |
| 34 | 738 → 1064 | 1D.2 |

Gold spine Ch 14–20, 9, 23, 31 etc. essentially stable (as intended).

### Critical assessment of the 45–70k intermediate target

The 45–70k band was a **planning heuristic** for “ordeal enough to feel novelistic,” not a quota. Current ~30k with working Mutina/Philippi/lists/pre-Ides deposits shows that **scene quality moved more than raw count**. Chasing 45k by uniform expansion would reintroduce the symmetry error 1B forbade.

**Recommendation:** Retire 45–70k as a success gate. Keep it only as an optional upper bound if a *specific* missing scene (not “more words”) is identified. Length should follow backlog P0/P1 remedies, not a target band.

---

## 3. Chapter-by-chapter cold-read assessment

*(Compressed; full sequential read performed. “Defect” = confirmed problem; “Pref” = taste/optional.)*

### Act 1 — Ch 1–6

| Ch | Assessment |
|----|------------|
| **1** | Opening image strong (“price change with blood”); still a **reaction collage** (market → Cicero fringe → triumph street), not one rising want. Future-lean on Cicero **resolved** (present inadequacy). Pref: longer single-POV open. |
| **2** | Seius debt ladder works; Hordeonius voice planted. Soft: ledger essay half. |
| **3** | Laberius mud/pay theology lands; pre-battle inventory thin on choice. |
| **4** | **Major 1D.4 win:** burned Caesarian dinner; Decimus roads/Campus trust before heir whisper. Still three panels, but psychology deposit is real. |
| **5** | OCT inventory, not destiny — lock held. Dramatic vacancy: little resistance forcing a choice. Heavy *filed*. |
| **6** | Cicero compliance/disgust sharp; packing montage postcard-adjacent. |

**Q1 Opening compelling?** Partially. Hook is voice/texture; lasting elite want waits until Ch 4.

### Act 2 — Ch 7–13

| Ch | Assessment |
|----|------------|
| **7** | Diadem set-piece works. **E3 POV borders resolved** (Seius observed; Fulvia marked beat). Disclosure craft good; Antony after-beat still thin as person. |
| **8** | **1D.4 win:** Galba patron-note / brother’s debt cost. Brutus letter-burn tips commitment. Pref: second burn echoes Ch 4 motif. |
| **9** | Strongest pre-Ides conspiracy scene; spare Antony earned; Decimus as key. Mild memory lean: “later blurred who spoke first.” |
| **10** | SIDE-1 body without explaining Ides — lock held. Seius flinch clear. |
| **11** | Omens INF discipline good; reception > pursuit. |
| **12** | **E3 NOTE-1 muddy: resolved** (wrong emphasis; *consul?* misfiled). Soft future: “night that would break her.” |
| **13** | **1D.4 win:** GO friction (missing cousin, creditor, last doubt) — lock feels **chosen**. Packaging SC-31–33 still prep strips. |

**Q2 Decimus/Brutus earned?** Mostly yes. Decimus road-trust (4) → key (9) → habit (12–13). Brutus courtesy refusals → law’s face → spare → GO.  
**GO chosen vs checklist?** Chosen in SC-34; chapter packaging still procedural.

### Act 3 — Ch 14–20 (gold spine)

| Ch | Assessment |
|----|------------|
| **14–16** | Still the manuscript’s peak. Dream/fetch/Curia/false Antony-dead. Do **not** expand for symmetry. |
| **17–19** | Amnesty calculation, will/heir, funeral aim + Cinna INF-kill — aftermath holds. |
| **20** | Functional exits (Decimus Cisalpine logic, CLEO, OCT delayed news). Clearest **appendix-risk** chapter — exits more than ordeal. |

**Q3 Ides remains centre?** Yes. Risk of appendix is real from Ch 20, then **partially recovered** by 22/24/26–30/33–34.

### Act 4 — Ch 21–27

| Ch | Assessment |
|----|------------|
| **21** | **1D.5:** force-gap visitor clash; still letter-heavy; Brutus cage atmospheric/static. |
| **22** | **1D.5 peak:** aloud *Caesar* greeting; Atia/Philippus pressure; Antony dismisses veteran pay-door. Underestimate now behavioural with cost seed. |
| **23** | Retain flinch economy (correct). Lowest dramatic temperature; motto endings. |
| **24** | **1D.5:** Laberius dual-offer refuse; Antium room decides (Cassius cut; Servilia clause). |
| **25** | **1D.3:** marked Philippics copy = body risk; East sail still compressed dialectic. |
| **26–27** | **1D.1:** envoy+pay; failed parley (“You killed a man who trusted your cheer”). Ordeal **started**; field completes in 28–29. |

**Q4 Ch 17–25 sustain consequence?** Politically yes; emotionally uneven (best: funeral, name, Antium; weaker: letter desk / Ch 23).  
**Q5 Mutina ordeal?** Lean ordeal from 26–27; complete only with 28–29.

### Act 5 — Ch 28–34

| Ch | Assessment |
|----|------------|
| **28** | Soldier ordeal; Hirtius as local fact; AMB-2 held. Plains future-lean **resolved**. Borderline: “They would call it a great success…” (Laberius cynicism vs soft forward). |
| **29** | Decimus death as sensory trap — **major 1D.1 win**. Ally-evaporation largely asserted in-scene. OCT fasces without Augustus mind — held. |
| **30** | **1D.3 + 1F:** contested Cicero naming; chalk-wall street; Formiae feels bought. Proscriptions as catastrophe, not inventory. |
| **31** | Earned close for Chain 6; slightly over-articulates mid-litter. |
| **32** | Connective-competent (liberty-as-tax; west courier fog); not peak drama. |
| **33–34** | **1D.2:** fog; Cassius info-death; Brutus second-day weight; OCT fever/not genius; Antony Italy underestimation; SERIES hooks-only. Laberius “world narrowed to dust/mud…” **recycles** Ch 28 opener. |

**Q6 Decimus death weight?** High emotionally; long-arc ally betrayal thinner than the death scene.  
**Q7 Proscriptions?** Catastrophe wins (chalk market, unclean leases, Seius bed-rehearsal).  
**Q8 Philippi culmination?** Yes thematically; deaths choice-shaped.  
**Q9 Ending / SERIES?** Clean hooks-only; no Actium. Mild anti-Actium wink (“future city-name”) still points at the horizon.  
**Q10 One novel?** Yes as spine, with soft connective spots — **not** the 1B “novella + appendix” verdict.

---

## 4. Phase 1D.1–1D.5 effectiveness review

### 1D.1 — Mutina / Decimus (Ch 26–29)

| | |
|--|--|
| **Improved** | Envoy refusal + levy pay; parley as decision; Laberius Hirtius-fact; Decimus priced ford / ordinary ditch; OCT fasces learning. |
| **Remains** | Ally evaporation asserted inside Ch 29; SC-81 sketch-length beside SC-80; Cleopatra/Sextus stamps in Ch 26. |
| **Side effects** | Laberius battle-opener template later echoed at Philippi. |
| **Further revision** | **Optional (P1 local)** — not another Mutina ordeal batch. |

### 1D.2 — Philippi (Ch 33–34)

| | |
|--|--|
| **Improved** | Fog held; Cassius M18 ordeal; Brutus death lived; OCT ill/not genius; Antony Italy blindness embodied; SERIES lean. |
| **Remains** | SC-95 residual thesis/continuity tone; dual Laberius openers. |
| **Side effects** | Hordeonius ash/OPEN-0 echo tidy. |
| **Further revision** | **Optional (P2 polish)** — do **not** expand to match Curia length. |

### 1D.3 — Philippics / Bononia / East (Ch 25, 30, 32)

| | |
|--|--|
| **Improved** | Philippics body-risk; contested naming; liberty-as-tax; courier fog. (Bononia further deepened in **1F**.) |
| **Remains** | Ch 32 connective-thin; Ch 25 East still dialectic-on-deck. |
| **Side effects** | Historiographic “traditions would disagree” in Bononia tent air. |
| **Further revision** | **Optional** — Ch 32 only if cold-read seam still bothers; not required. |

### 1D.4 — Pre-Ides earning (Ch 4, 8, 13)

| | |
|--|--|
| **Improved** | Brutus behavioural hinge; Decimus–Caesar trust deposit; Galba cost; GO chosen. |
| **Remains** | Ch 8 burn-echo; Ch 13 prep-strip packaging; Antony still thin as person pre-Ides. |
| **Side effects** | Dual courtesy-burns (4 + 8) motif fatigue risk. |
| **Further revision** | **Unjustified as batch**; light polish only if touching files. |

### 1D.5 — Name-war (Ch 21, 22, 24)

| | |
|--|--|
| **Improved** | Name greeting cost; underestimate cost seed; Laberius listen-decision; Antium decides. |
| **Remains** | Ch 21 letter-essay residue; Brutus Lanuvium stasis. |
| **Side effects** | None material. |
| **Further revision** | **Optional** Ch 21 compression/scene heat — not a new name-war batch. |

### Adjacent 1F (not a 1D batch; on tree)

E3 local fixes (Ch 7/12/1/28) **resolved** against prior flags. I2 Bononia deepen **succeeded** (chalk-wall; Formiae inevitability).

---

## 5. Character and emotional-continuity audit

| POV | Arc continuity now | Missing / thin | Voice distinct? |
|-----|--------------------|----------------|-----------------|
| **Decimus** | Trust → key → fetch → Cisalpine → Mutina refuse → road meat | Mid-gap Ch 20→26; allies’ betrayal under-dramatised | Yes (cheer/key/logistics) |
| **Brutus** | Soft chain → burns → law’s face → spare → GO → cage → East tax → Philippi | Lanuvium/ship **stasis**; brand cost clearer at Philippi than mid-band | Mostly; philosophy can caption |
| **Cassius** | Slight → recruit → spare loss → East extraction → info-death | Ops body before mist still lean (acceptable) | Yes (geometry/contempt) |
| **Antony** | Diadem → spare object → funeral aim → squeak miss → Mutina competence → lists → Philippi peak/blind | Pre-Ides personhood thin; grief for Caesar still underplayed | Yes when present |
| **Cicero** | Blind calm → letters → Antium shelved → Philippics risk → tool-misread → Formiae | Risk of thesis-machine | Yes (sentence vanity) |
| **Octavian** | Inventory → delayed news → name → Senate sword → fasces → list silence → fever | Emotional cost of each step still compressed | Yes (inventory/fear) — **≠ Augustus** |
| **Calpurnia** | Dread → dream → failed veto | Thin before Ch 12 (pref) | Enough for Book 1 |
| **Nysa** | Listen → fragment → block → Cinna → lists chalk | Intentional thin after 23 OK | Yes (objects) |
| **Seius** | Debt → flinch → hide → list-absent shame | Do not heroise | Yes |
| **Laberius** | Mud → powder → funeral measure → listen → Mutina/Philippi | Opener recycle Mutina/Philippi | Yes (pay/eagle) |
| **Hordeonius** | Rates → SIDE-1 → will market → unclean acquire → sleepless fields | Keep unintentional humour | Yes (ledger-priest) |

**Duplicated functions:** Laberius as “battle sensor” in 28 and 33 risks sameness; F-triptych in 23 and 30 both do street-economy — 30 earns it, 23 is lighter by design.

**Assumption challenges (craft):** Decimus friendship-as-safety broken; Cassius numbers broken by fog; Antony squeak assumption costs later; Cicero voice≠power — all now **shown** at least once with cost.

---

## 6. Historical, POV, and mystery-integrity findings

| Lock / issue | Status | Evidence |
|--------------|--------|----------|
| Chronology / CHOREO-1 | **Held** | Cimber → Casca → chaos; Trebonius holds Antony (15); Curia Pompey |
| A/B/C/D discipline in prose | **Held** | Contested last words; contested Cicero naming; AMB-2 |
| One close-third per scene | **Mostly held** | Ch 7 leak **resolved** (1F); ensemble chapters use marked beats |
| Info characters can know | **Held** | Laberius Hirtius-by-touch; Cassius incomplete INF; OCT fever not genius map of Italy |
| False Antony-dead → funeral | **Held** | Ch 16 seed → 19 aim |
| NOTE-1 dual + ambiguity | **Held / improved** | Nysa ≠ Curia note; Ch 12 now misreadable |
| SIDE-1 subordinate | **Held** | Never explains Ides; OPEN-0 at end |
| AMB-2 Pansa | **Held** | Rumour labels; refuse sale |
| OCT ≠ Augustus | **Held** | Learning, sickness, no destiny smile |
| No Actium / SERIES-1 | **Held** | Hooks only; anti-Actium wink present but not plotting |
| Spare Antony outcome | **Held** | |

### Actual contradictions vs deliberate ambiguity

- **No hard contradictions** found against `canon.md` locks in this pass.  
- Deliberate ambiguities held: Caesar knowledge (AMB-1); NOTE-1 relation; Cicero naming; Pansa; SIDE-1b.

### Prior local flags (retest)

| Flag | Status | Evidence |
|------|--------|----------|
| Ch 7 POV leak | **RESOLVED** | Seius exterior; Fulvia marked beat |
| Ch 12 overhear too clean | **RESOLVED** | Broken mutter; misfiled wax |
| Ch 1 “would later write better” | **RESOLVED** | Present inadequacy |
| Ch 28 “plains would later” | **RESOLVED** | Absent; residual “They would call it a great success…” = **UNCERTAIN** (character cynicism) |

---

## 7. Updated prose and voice assessment

### Pattern frequencies (approx., body files)

| Pattern | Approx. hits | Assessment |
|---------|-------------:|------------|
| *weather* | ~28 lines | Still overused as default politics metaphor; **character-true** in Caesar opacity / cover-talk; **non-native** when every POV “files weather.” |
| *filed* / filing | ~13 | Mostly F4/OCT/Nysa-appropriate; Antony “filed the pallor” (Ch 7) is a mild borrow. |
| *was how* | ~19 | House-style tic across POVs (Hordeonius, Nysa, Cicero, Laberius, Octavian). Frequency = real fatigue risk, not automatic defect per instance. |
| Aphoristic closers | Common | Works after earned beats; fails when it **replaces** the beat (esp. Ch 23). |
| Image → gloss | Occasional | Mild; Curia largely clean. |
| Future-facing asides | Rare | Hard “would later / novelists later / plains would” **cleared** in targeted files; soft borders remain (Ch 12 “night that would break her”; Ch 28 “would call it success”; Ch 34 anti-Actium negation). |

### Preserve (do not “normalize”)

- F4 ledger-priest humour  
- Octavian inventory / fear  
- Laberius pay theology  
- Nysa object-precision  
- SAMPLE-1 density in Ch 14–16  
- Disputed last words; OPEN-0; SERIES hooks-only  

### Voice convergence risk

Confirmed: polished “X was how you Y” and “X was not Y; X was Z” cadences appear in multiple minds. **P1 for house-style pass**, not a structural rewrite.

---

## 8. Ranked remaining revision backlog

### P0 — structural / causal defects that materially damage the read

**None confirmed at this gate.**

The former P0 “Acts 4–5 postcard / Philippi cannot compete” hypothesis from 1B is **not sustained** after 1D.1–1D.2 (+ lists/name-war). Remaining issues do not make Ch 20→34 feel like an appendix.

### P1 — important emotional / scene / continuity problems

| ID | Ch | Defect | Evidence | Reader consequence | Remedy | Done when |
|----|----|--------|----------|--------------------|--------|-----------|
| P1-a | 20–21, 23 | Mid-band energy trough | Exit cards; letter desk; motto triptych | Post-Ides sag before name-war recovers | Prefer **compression + one live collision** per thin chapter when touched; do not bulk-expand | Cold read 19→24 without wanting to skip |
| P1-b | 20→26 | Decimus presence gap | Nearly vanishes after Cisalpine logic until envoy scene | Betrayal→siege moral continuum weakens | Optional **one short Decimus beat** (letter/road/refusal) between 20–26 — only if seam still hurts | Fetch→Mutina feels continuous |
| P1-c | 29 | Ally evaporation asserted | “Plancus hesitated, Lepidus smiled wrong” inside death chapter | Death hits; betrayal lattice thin | Seed **one earlier refusal** (tablet/envoy) before the ford — small | Death still surprises; betrayal doesn’t feel invented at the ditch |
| P1-d | global | House-style convergence | *weather / filed / was how* across POVs | Ensemble voices blur | **Targeted 1G pass**: cut non-native instances; preserve F4/OCT/Nysa/Laberius true uses | Spot-check 5 POVs without shared closer cadence |
| P1-e | 21 / Brutus mid | Lanuvium stasis | Cage restates without new cost | Brand arc stalls until East/Philippi | Optional one behavioural cost (refuse client / burn scrap already used — prefer **new** behaviour) | Brutus changes once between GO and East |

### P2 — optional craft improvements

| ID | Ch | Item | Remedy test |
|----|----|------|-------------|
| P2-a | 28/33 | Laberius opener recycle | Differ second battle open without losing sensor job |
| P2-b | 34 SC-95 | Thesis / anti-Actium wink | Soften continuity-essay tone; keep hooks |
| P2-c | 30 | “traditions would disagree” | Keep contested naming; remove historiographic step-out |
| P2-d | 1 | Opening collage | Optional single-POV longer open |
| P2-e | 8 | Dual courtesy-burns | If revisiting, vary second hinge |
| P2-f | 19 | Appian funeral-gesture VERIFY | When sources handy |
| P2-g | letters | Latin VERIFY | If verbatim lines kept |
| P2-h | 28 | “great success” borderline lean | Soft to present ditch irony only |

**Do not:** expand Ch 14–16 for length; solve SIDE-1b; draft Actium; run a global adverb purge; treat 45–70k as a quota.

---

## 9. Length recommendation

| Approach | Verdict |
|----------|---------|
| Chase 45–70k intermediate band | **Not useful as a gate** after this cold read |
| Chase LEN-1 90–130k now | **Premature** — would force symmetry expands |
| Stay ~30k and polish | **Viable** if SERIES/LEN targets are consciously reframed as multi-book or later growth |
| Grow only for P1 remedies | **Preferred** — likely **+1–3k** if P1-b/c done; not another +10k ordeal wave |

Missing scenes that would justify words: at most **one Decimus interstitial** and **one ally-refusal seed** — not Mutina/Philippi re-expansion.

---

## 10. Readiness verdict and next milestone

### Checklist (1B §H / craft §J, retested)

| Item | Now |
|------|-----|
| Cold read Ch 1–34 feels like one novel | **Mostly yes** (soft trough 20–23) |
| ≥45k **or** explicit lean-scope decision | **Neither yet** — recommend **explicit lean-scope acceptance** for Book 1 v1, with later growth optional |
| P0 consequence ordeal complete | **Yes** (Mutina→Philippi weight present) |
| P0-2 Decimus/coalition earning | **Yes** (Ch 4/8/9/13) |
| Canon locks held | **Yes** |
| MUST_EXPRESS behaviour-true | **Yes** on spot-check |
| P2 VERIFY logged | **Still open** (Appian; Latin) |
| Voice vs SAMPLE-1 on expands | **Mostly**; template convergence = remaining debt |
| No new future-winks | **Mostly**; soft borders remain |

### Gate choice: **Gate B**

**Gate B — Structure sufficiently sound for a light, targeted house-style pass.**

**Why not Gate A:** No remaining P0 structural/causal defect requires another development wave. Expanding again “because still shorter than Ides” or “because under 45k” would violate the project’s own anti-symmetry rule and the evidence of this cold read.

**Why not Gate C:** Template convergence (P1-d), mid-band trough (P1-a), and open VERIFY items mean an external developmental reader would spend capital on craft tics and soft connective tissue rather than on story architecture. External review after a short 1G-style pass (and optional P1-b/c) will be higher value.

### Recommended next milestone

1. **Phase 1G — Targeted house-style pass** (craft I3): *weather / filed / was how* hunt; soft future borders; SC-95 thesis tone; Laberius opener variance — **without** bulk scene adds.  
2. Optional micro-scenes only if P1-b/c still hurt after 1G.  
3. Then **cold-read spot-check** Acts 4–5 → consider Gate C or human line edit (1H).  
4. VERIFY pack rides along as P2.

---

## Appendix — Inspection provenance

- Chapters: `drafts/book1/ch01_*.md` … `ch34_*.md` (34 files)  
- Plans: `continuity/phase_1d{1,2,3,4,5}_*.md`, `phase_1f_bononia_e3_plan.md`  
- Prior diagnosis: `editorial_diagnosis_1b.md` (hypotheses retested)  
- Craft method: `craft_editorial_pass_1c.md`  
- Canon / map / express: `continuity/canon.md`, `writing/CHAPTER_MAP.md`, `writing/MUST_EXPRESS.md`  
- Logs: `../pass_logs/mid_tier_pass_log.md`, `continuity/future_research.md`  

*End of Phase 1D.6 cold read.*

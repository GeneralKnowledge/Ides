# Lock Architecture Audit 1.0

**Date:** 2026-10-18  
**Branch:** `cursor/lock-architecture-audit-cb1d`  
**HEAD inspected (baseline):** `68f5845` (*Integration Revision 1.0* on `main`)  
**Audit commit tip:** `cc75071`  
**Pass type:** Architecture / policy audit. **No chapter prose edited.**

**Governing principle:** Lock what must remain true; preserve freedom over *how* the story makes it true.

---

## 1. Scope

### Files audited (current versions)
- `continuity/canon.md`
- `story/historical_anchors.md`, `flexibility_zones.md`, `pov_lock.md`, `pov_structure.md`, `mysteries.md`
- `writing/CHAPTER_MAP.md`, `MUST_EXPRESS.md`, `LLM_WRITING_BRIEF.md`
- `continuity/expansion/` (README, summaries, tracks, deposit map, integration review)
- `../archive/pass_logs/integration_revision_1_pass_log.md`
- Spot: `deep_craft_audit.md` §7 exclude list; `story_first_intrigue_plan.md` / shortfall hold-locks; `mid_tier_pass_plan.md` non-goals

### Rule families
Historical anchors · narrative ambiguity · fictional continuity · POV allocation · chapter/scene structure · expansion PROTECT · editorial anti-padding · drafting-era process locks

---

## 2. Classification key

| Code | Meaning |
|------|---------|
| **A** | Historical invariant |
| **B** | Narrative invariant (deliberate story truth / reader experience) |
| **C** | Continuity commitment (invented, relied-upon; revisable with reconciliation) |
| **D** | Structural preference (design choice; guide, not veto) |
| **E** | Editorial guardrail (prevents known failure modes; exceptions evidence-led) |

**Dispositions:** KEEP · NARROW · RECLASSIFY · MERGE · RETIRE · CLARIFY

---

## 3. Inventory (meaningful locks only)

### A — Historical invariants → **KEEP**

| Lock | Source | Protects | Restricts |
|------|--------|----------|-----------|
| Anchors A1–A14 | `historical_anchors.md` | Outcomes, places, primary participants, public political meaning | Moving date/place/outcome; impossible futures |
| Meta: Ides = Curia of Pompey | `canon.md` §7 | Place of assassination | Relocating murder “for drama” |
| Meta: no Shakespeare last words as history | `canon.md` §6 | Historical honesty | Narrator asserting *Et tu* as fact |
| Meta: Fictional POVs ≠ overwrite A-outcomes | `canon.md` §8 | Anchor integrity | Local INF rewriting public history |
| Certainty A/B/C/D discipline | `canon.md` meta-1 | Epistemic honesty | Upgrading rumour to fact |

Already well-designed (Acceptable / Unacceptable columns). **No change of substance.** Clarified only that A5’s **choreography is C**, not A.

### B — Narrative invariants → **KEEP** (narrow implementational language)

| Lock | Source | Intended experience | Implementation (revisable) |
|------|--------|---------------------|----------------------------|
| **AMB-1** | canon | Reader does not get narrator-confirmed Caesar-knows | Which warnings reach him; Decimus reassurance staging |
| **AMB-2** | canon | Pansa foul play stays rumour | Which mouths carry poison talk |
| **AMB-3** | canon | No confirmed divine causation in narrator | Dream/omen *experience* vs meaning |
| **NOTE-1 dual** | canon | Two warning tracks remain distinct; unread Curia note ≠ Nysa fragment | Exact plant wording; who blocks what |
| **SIDE-1 / OPEN-0** | canon | Parallel murder pressure; does not explain Ides; solution may stay open | Clue schedule; which tablets surface |
| **OCT≠Augustus** | canon / A8 | Young, learning, unfinished | Which ordinary friendship beats show it |
| **SERIES-1** | canon | Book 1 ends Philippi emotional arc; hooks only | Exact hook wording |
| no Actium in Book 1 | expansion / series | Future not resolved as Book 1 plot | Mentions as rumour vs plotting |
| plural motives / no hive mind | canon | Conspiracy is argument, not unison | Which argument scenes carry it |
| disputed last words | CHOREO-1 §7 | Witnesses disagree; no Shakespeare Latin as truth | Which two ears hear what |

**NARROW:** Documents that said “do not reopen AMB-1 / NOTE-1” meant *do not collapse the invariant* — not “never add evidence consistent with multiple readings.” Clarified in `canon.md` and expansion README.

### C — Continuity commitments → **CLARIFY** (durable, revisable)

| Lock | Source | Nature |
|------|--------|--------|
| **DREAM-1**, **HOUSE-1**, **OMEN-1** (manufactured Sibylline) | canon | Invented/chosen traditions already in prose |
| **FIC-1..4** identities | canon / POV | Regular fictional sensors |
| **CLEO-1** lodging / April exit | soft lock | Working geography for Rome stay |
| **FUNERAL-1 / EXIT-1** soft dates | soft | Chronology texture |
| **MAP-1 / HOUSE-1 travel** | canon | Relative geography |
| Landed deposit facts (e.g. Nysa Ch 15 lie → Ch 19 burn; Plancus *yet*) | IR-1 / manuscript | Relied-upon invented beats |

**Principle:** Treat as continuity canon against *accidental* contradiction. A deliberate revision may replace them if dependents and `canon.md` are updated. They are **not** historical A-facts.

### D — Structural preferences → **RECLASSIFY**

| Lock | Was presented as | Should be | Disposition |
|------|------------------|-----------|-------------|
| **POV-1 / POV-2** ensemble + slot counts | “LOCKED” planning canon | Preferred architecture; knowledge bans stay B/A | **RECLASSIFY** + review route in `pov_lock.md` |
| **BEAT-1** five-act sheets | Locked | Preferred act map | **RECLASSIFY** |
| **CHAPTER_MAP** chapter numbers / SC bundling | Drafting authority | Preferred units; outcomes > chapter numbers | **CLARIFY** |
| **CHOREO-1** blow order | Staging “canon” often listed with Curia “PROTECT” as if A | Working staging (C→fictional); A5 outcome separate | **NARROW** |
| **DEC-PERS-1** persuasion composite | Working | Preferred fetch beats | **KEEP** as C/D |
| **NAMES-1** minor cast freeze | Frozen | Continuity convenience; new minors OK if logged | **NARROW** |
| **LEN-1** 90–130k | Soft target (already) | Preference / scale record | **KEEP** (already distinguished) |
| Deposit map D-IDs / wave order | Expansion authority | Guide; not story law | **KEEP** as E/D |

### E — Editorial guardrails → **KEEP** purpose / **CLARIFY** exceptions

| Rule | Purpose | Overprotection risk | Disposition |
|------|---------|---------------------|-------------|
| Architecture before dump / three novelist questions | Stop padding | Can chill legitimate densify of *existing* rooms | **CLARIFY** — applies to *new* beats, not line fixes |
| Stopping rule | End expansion without compelling reason | Fine | **KEEP** |
| Gold spine / PROTECT / “do not reopen” | Stop quota symmetry & prove-again | Reads as immunity to all improvement | **NARROW** — see §4 |
| No new mystery engine | Scope | Fine | **KEEP** |
| Anti-formula / no ≥2-laws inject sweep | Stop false-green craft theatre | Fine | **KEEP** |
| **DRAFT-1 / START-1** | First-pass drafting order | Stale as live “must” after full draft exists | **RETIRE** as active gate; keep as history |
| **HUMOR-1** near-off zones | Tone at terror | Fine as preference | **KEEP** |
| MUST_EXPRESS checklist | Behavioural coverage | Treat as audit aid, not scene-forced inventory | **CLARIFY** |

---

## 4. Overprotection findings (highest impact)

### 4.1 Anchor vs implementation — CHOREO-1 / “Curia knife core”

**Problem:** Expansion “Hold locks” and deep-audit exclude lists bundle **A5** (Caesar dies at Curia of Pompey) with **CHOREO-1** (working blow order) and “gold spine not evened,” so writers hear “never touch Ch 16.”

**Should protect:** Death, place, day, Trebonius-holds-Antony consequence chain, disputed last-words *stance*, continuous-dream quality.

**Should not auto-protect:** Exact petition wording, every camera cut, every private line, blow ordinal if a better C-staging is demonstrated with continuity review.

**Disposition:** **NARROW** in `canon.md` + expansion README.

### 4.2 Protected scene ≠ untouchable scene

**Problem:** `PROTECT` on D19/D23/D24 and review language (“Do not reopen”) block continuity fixes and genuine betterments unless someone re-litigates the whole architecture.

**Correct meaning:** Shield from padding, length symmetry, prove-again passes. Allow continuity error fixes, weak-line/transition improvement, and compelling rearrangements under stronger justification + dependent checks.

**Disposition:** **CLARIFY** PROTECT definition on deposit map + README.

### 4.3 Mystery protection vs paralysis

**Problem:** “Do not reopen NOTE-1 / AMB-1 / SIDE-1” can be read as forbidding new consistent evidence.

**Correct meaning:** Do not collapse dual warnings, confirm Caesar-knows, or make SIDE-1 explain the Ides. Do allow denser ambiguity, alternate info paths, stronger emotional cost of not knowing.

**Disposition:** **CLARIFY** in `canon.md` mystery section.

### 4.4 POV lock rigidity

**Problem:** `pov_lock.md` “LOCKED for planning” + canon POV-1 look permanent. Slot targets (2–4 scenes per cluster) read as hard caps.

**Correct meaning:** Historical knowledge bans (no OCT on Ides; Caesar POV ends at death; no future knowledge) are invariants. Ensemble *allocation* is preferred; new/changed POV requires proportional review (reader effect, invariants, continuity)—not a ritual for every line.

**Disposition:** **RECLASSIFY** + add review route; **no new POV in this audit**.

### 4.5 Chapter map / MUST_EXPRESS as fake invariants

**Problem:** Drafting tools still speak as if SC numbers and MUST_EXPRESS ticks forbid alternate delivery of the same narrative requirement.

**Correct meaning:** Same outcome may be delivered by a different scene arrangement if dramatic merit and continuity hold.

**Disposition:** **CLARIFY** in CHAPTER_MAP / brief cross-link; MUST_EXPRESS remains behavioural checklist.

### 4.6 Stale drafting locks

**DRAFT-1 / START-1** (first prose = Batch A / Ch 14) are process archaeology. Leaving them in the “LOCKED” column without marking obsolescence confuses new agents.

**Disposition:** **RETIRE** as active requirements; retain as dated history entries.

### 4.7 Already well-designed (leave alone)

- `historical_anchors.md` Acceptable/Unacceptable  
- AMB-3 / no narrator supernatural  
- SIDE-1 must not explain Ides  
- SERIES-1 / no Actium as Book 1 content  
- Flexibility zones F1–F16  
- Expansion stopping rule + three novelist questions (as anti-padding)  
- LEN-1 already soft / not completion gate  

---

## 5. Six diagnostic proposals (policy test)

| # | Proposal | Current rules feel | Should be | Invariants that survive | Checks |
|---|----------|-------------------|-----------|-------------------------|--------|
| 1 | New private Decimus–Brutus hour deepening timing quarrel (no outcome change) | Allowed via F1/F2 flex; expansion may over-chill “no new beats” | **Permit** if want/cost real; log if sticks | A9 split; plural motives | Continuity of Ch 20 clasp; no third mystery |
| 2 | Revised Nysa/attendant mutter that thickens NOTE-1 dual without merging tracks | “Do not reopen NOTE-1” may scare | **Permit** densify; **reject** merge into one note | NOTE-1 dual; AMB-1 | Dual Continuity notes; Ch 15/19 object path |
| 3 | Reorder Ch 23 cameras or linger on Seius before F4 | CHAPTER_MAP / mosaic habits resist | **Permit** with camera justification | SIDE-1 OPEN-0; boy-Caesar price | Info Enter/Exit; Antium seeds |
| 4 | Alternate CHOREO-1 blow order (still Cimber→Casca tradition family; Caesar dies at Pompey base; Trebonius holds Antony) | “PROTECT Curia / CHOREO-1” reads reject | **Escalate** deliberate review — not auto-reject | A5; Trebonius outside; disputed last-words stance | Dependent Ch 15–17; scene cards |
| 5 | New Decimus resentment beat that does *not* make SIDE-1 cause Ides | Fine if SIDE-1 rule held | **Permit** character deepen; **reject** if SIDE-1 becomes master key | SIDE-1 subordinate; AMB-1 | Canon SIDE-1 rules |
| 6a | Better Ch 16 transition that preserves continuous dream + A5 | Overprotected | **Permit** with strong justification | A5; dream quality; Trebonius leash | Gold-spine careful re-read |
| 6b | Pad Ch 16 with extra omen jokes for “grandeur” / word count | Correctly blocked | **Reject** | — | Stopping rule / PROTECT purpose |

---

## 6. Documentation changes made (this pass)

| File | Change |
|------|--------|
| `continuity/canon.md` | Lock-tier preamble; CHOREO-1 narrowed; mystery “reopen” clarified; POV/BEAT/DRAFT/START reclassified; continuity-revision note |
| `story/pov_lock.md` | Preference vs invariant; future POV review route |
| `story/historical_anchors.md` | A5 note: choreography C ≠ place/outcome A |
| `continuity/expansion/README.md` | Hold-locks rewritten; PROTECT ≠ immunity |
| `continuity/expansion/beat_deposit_map.md` | PROTECT definition |
| `writing/CHAPTER_MAP.md` | Map = preferred units; IR-1 flags cleaned |
| `writing/LLM_WRITING_BRIEF.md` | Pointer to lock tiers / this audit |
| `writing/MUST_EXPRESS.md` | One-line authority: checklist ≠ forced scene inventory |
| `../archive/reports/deep_craft_audit.md` | §7 exclude list marked as pass snapshot; pointer to this audit |
| `continuity/lock_architecture_audit.md` | This file |

**Not rewritten wholesale:** flexibility zones, mysteries.md (already ambiguity-friendly), integration review / pass-log historical text.

---

## 7. Remaining mild conflicts (live with / non-blocking)

| Tension | Note |
|---------|------|
| Pass logs still say “do not reopen CHOREO-1 knife pile” | Historical process language; superseded by narrowed canon — do not mass-edit old logs |
| SAMPLE-1 “voice gold” | Tone anchor, not plot lock — already stated; leave |
| Deep craft exclude list | Snapshot of a past pass; point forward to this audit rather than delete history |

---

## 8. Practical future examples

### Now clearly allowed (without breaking canon)
1. A continuity-safe line fix inside Ch 16 that does not move A5 or Trebonius-outside.  
2. Additional rumour mouths that keep NOTE-1 dual and AMB-1.  
3. A POV-scene reallocation inside an existing beat cluster that improves pressure, with Continuity update — no new historical POV required.

### Still must reject
**Narrator confirms Caesar knew the operational plot (collapses AMB-1),** or **SIDE-1’s killer is revealed as the “real” reason for the Ides,** or **Caesar survives / murder moves off Curia of Pompey (breaks A5).**

---

## 9. Success check

A future writer can distinguish:
- **Must remain true** — A-anchors; stated B invariants  
- **Should remain true unless compelling** — strong C commitments; gold continuous-dream quality  
- **Currently true (revisable)** — CHOREO-1 details; chapter bundling; deposit wording  
- **Preference / guardrail** — LEN-1; POV slot counts; stopping rule; anti-padding  

No automatic expansion. Default remains: leave effective material alone.

---

*End lock architecture audit 1.0.*

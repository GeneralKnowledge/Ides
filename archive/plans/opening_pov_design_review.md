# Opening Hook & POV Rhythm Design Pass

**Date:** 2026-10-18  
**Branch:** `cursor/opening-pov-design-cb1d`  
**Baseline HEAD inspected:** `b60b9b4` (`origin/main` — Lock Architecture Audit 1.0 merged)  
**Manuscript inspected:** `drafts/book1/ch01`–`ch34` (live prose, not chapter-map alone)  
**Pass type:** Discovery / design only. **No chapter prose, scene cards, canon, or map edits.**

**Lock hierarchy followed:** historical & narrative invariants (`canon.md`, `historical_anchors.md`) over continuity commitments over structural preferences (CHAPTER_MAP, POV slot targets) over editorial guardrails. See `lock_architecture_audit.md`.

---

## 1. Executive recommendation

### Opening strategy
**Recommend a carefully bounded private / semi-private gathering as the new dramatic front door — not Lupercalia as Chapter 1, and not a wholesale discard of the current street opening.**

Preferred path (**Concept B**, placement refined in §11):

1. **Rework the fictional dinner to late 46 BC** (post-triumph / Cleopatra newly across the river) and open **chronologically** — dinner as Ch 1 *or* F4 Thapsus shock then same-year dinner as Ch 2 — **without** jumping backward from 45 to 46.  
2. Retool the dinner’s Spain-posting slight into an **Africa-favour** slight so motives stay intact; keep queen/child talk (sharper when the lodging is new).  
3. Preserve F4 street INF in the same season; keep Lupercalia at ~Ch 7; push Porcia marriage pressure and Decimus will-whisper to their natural ~45 nest.

**Do not** prefer “dinner in late 45 → flashback to 46” unless Spanish-posting texture is judged non-negotiable (§11).  
**Do not** open on the eve-of-Ides Lepidus dinner (Suet. *Iul.* 87).

If the author prefers brand continuity over earlier principal introductions, **the existing Ch 1 is already strong enough to keep** after a POV-rhythm pass; it is not “broken.”

### POV policy
Adopt a flexible combination (already half-stated as G1/G2 in `story_first_intrigue_plan.md`, underused in practice):

| Default | Rule |
|---------|------|
| **Chapter default** | One dominant POV per chapter |
| **Second POV** | Only when it collides with the first’s unfinished question |
| **Character blocks** | Prefer multi-chapter or multi-scene runs for the same consciousness when events are continuous |
| **Multi-POV chapters** | Reserved for collective crises (Ides morning/Curia, funeral, Bononia/lists) with clear scene breaks |
| **No quotas** | Ignore “2–4 POV scenes per beat cluster” as a reason to cut away; keep historical knowledge bans |

Largest manuscript problem is **Problem B/C** (chapter fragmentation + short emotional runs), not unmarked head-hopping. Worst opening-act offender: **Ch 13** (four POV units, ~300w average).

### Next implementation step (do not start until approved)
**Pilot outline only (docs):** a 1–2 page “Opening reorder sketch” for Ch 1–4 showing scene order, POV ownership, and what moves vs stays — no prose rewrite. Optional parallel: mark Ch 13 merge candidates in a short annex.

---

## 2. Repository baseline

### Version
| Item | Value |
|------|--------|
| Inspected remote tip | `origin/main` @ `b60b9b4` |
| Working branch for this report | `cursor/opening-pov-design-cb1d` |
| Limitation | Prior agent branches exist; this pass treats **merged main manuscript + docs** as authority, not unmerged experiments |

### Current opening (what it already accomplishes)
**Ch 1 — Cato and Spectacle** (`drafts/book1/ch01_cato_and_spectacle.md`)

| Unit | POV | Chronology | Dramatic job |
|------|-----|------------|--------------|
| SC-01 | **F4 Hordeonius** (Cicero fringe in-frame, not a cut) | 46 BC, Forum / basilica | Thapsus/Cato news as price shock; sermons vs invoices; unfinished question: what victory costs the city |
| SC-02 | **F1 Nysa** | Triumph season, Domus Publica orbit | Street spectacle; veteran land spit; household eyes; collides with F4’s “Africa closed enough” |

**Hook offered now:** incomplete public information + moral shock converted into market weather; dual altitude (banker / household servant); Republic bruised without a famous-name roll call.

**Chronology:** Opens ~two years before the Ides (A1 Thapsus / Cato), then Munda (Ch 3), clemency whisper (Ch 4), *perpetuo* (Ch 6), Lupercalia 15 Feb 44 (Ch 7).

### Existing strengths to preserve
- Street INF identity (F4/F1) is a real brand asset, not padding.  
- Ambiguity and plural interpretation already work in SC-01 (marble vs onions; unfinished Cicero period).  
- Ch 5 (Octavian sole run) and Ch 7–8 (longer ~650–960w units) show the manuscript *can* dwell.  
- Lupercalia as mid-Act-1 public test already converts private resentment into city oxygen.  
- Lock audit correctly treats CHAPTER_MAP / POV allocation as **preferences**, not A-facts.

### Constraints that genuinely bind
- **A1–A14** outcomes/places (incl. A4 Lupercalia date/place as event; A5 Curia death).  
- **AMB-1 / NOTE-1 dual / SIDE-1 subordinate / AMB-3 / OCT≠Augustus / SERIES-1.**  
- Knowledge bans: no future knowledge; Caesar POV ends at death; Octavian zero Rome Ides.  
- CHOREO-1 = working staging, not A5; PROTECT ≠ immunity (`lock_architecture_audit.md`).

### Questions this pass must resolve
1. Can a gathering open introduce principals through behaviour without becoming a tour or assassination preview?  
2. Is Lupercalia better as open or as earned mid-act public test?  
3. Does the manuscript change POV too often in ways that cost immersion?  
4. Can a new open lead into the novel that exists (dual engines, Philippi end), not a different book?

---

## 3. Historical research — opening occasions

Certainty key matches project practice: **A** established · **B** supported but disputed · **C** plausible reconstruction · **D** deliberate invention.

### Candidate 1 — Lupercalia, 15 February 44 BC (required)

| Element | Class | Notes / sources |
|---------|-------|-----------------|
| Date & festival; Antony as consul among Luperci; Caesar watches from elevated seat; diadem/wreath offered and refused; sent toward Jupiter / Capitol | **A/B** | Plutarch *Caesar* 61; Suetonius *Iul.* 79; Dio 44.11; Cicero *Phil.* 2.85 (hostile, argues premeditation) |
| Crowd’s split applause; “experiment failed” reading | **B** | Plutarch’s staging of offer vs refusal applause; partisan colour in Cicero |
| Who stood where; exact words; whether staged by Caesar, Antony, both, or neither | **B/C** | Sources disagree on intent (humility theatre vs desire for kingship vs trap) |
| Fulvia pricing “temporary” at home; Seius pallor in crowd | **D** (already in Ch 7 prose) | Compatible with F1 flexibility |
| Broader “monarchy panic” as public weather after the day | **A/B** outcome of the tradition | Anchor A4 |

**Dramatic fitness:** Immediate concrete problem (crown / not-crown). Ensemble visible. Risk: page-one kingship spectacle can promise a “will he be king?” thriller and flatten the long runway of debt, clemency, and paper that this manuscript needs. **Already implemented well as Ch 7** — moving it to Ch 1 creates duplication or forces deletion of the best public set-piece later.

Useful links:  
- https://www.livius.org/sources/content/plutarch/plutarchs-caesar/the-lupercalia-incident/  
- http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.02.0132%3Alife%3Djul.%3Achapter%3D79  
- https://lexundria.com/dio/44.11/cy  
- https://dcc.dickinson.edu/cicero-philippics/ii-85  

### Candidate 2 — Senate brings honours; Caesar does not rise (early 44)

| Element | Class | Notes / sources |
|---------|-------|-----------------|
| Extravagant honours voted; Caesar remains seated when consuls/praetors + Senate approach; insult felt by Senate and people | **A/B** | Plutarch *Caesar* 60; Appian *BC* 2.106–108 tradition |
| Balbus restraining Caesar from rising | **B** | Plutarch; may be apologetic tradition |
| Exact calendar day relative to Lupercalia | **B** | Attalus / chronographic lists place seated insult and tribune deposition in early–mid Feb 44 orbit; precise day disputed |
| Which minor senators mutter what | **C/D** | Room for fiction |

**Dramatic fitness:** Political humiliation in a body of rivals; incomplete readings (illness? arrogance? theatre?). Less “spectacle comedy” than Lupercalia; more constitutional insult. Risk: can slide into honours-exposition.

Link: http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0244%3Achapter%3D60  

### Candidate 3 — Clemency / pardon social world (45–early 44)

| Element | Class | Notes / sources |
|---------|-------|-----------------|
| Caesar’s *clementia* after civil war; pardoned enemies living under obligation | **A** | Broadly attested practice; conspiracy includes beneficiaries (ancient and modern discussion) |
| Specific dinner with named host toasting mercy as sauce; “New-Spain” posting slight | **D** | Already in manuscript Ch 4 SC-08 |
| Queen / child / gardens as dinner poison | **B/C rumour** in-world | Must stay rumour (CLEO / audience-ahead rules); not Actium |

**Dramatic fitness:** Best match for “tense gathering” brief. Behaviour reveals Cassius, host, climbers; misunderstandings thrive. Smallest historical alteration: **invented precursor dinner**, not moving an A-event.

### Candidate 4 — Dinner at Lepidus, 14 March 44 (“best kind of death”)

| Element | Class | Notes / sources |
|---------|-------|-----------------|
| Caesar dines at Lepidus’s house night before Ides; talk of best death; Caesar prefers sudden/unexpected | **A/B** | Suetonius *Iul.* 87; also Plutarch tradition |
| Guest list including Cleopatra / Decimus as in some modern reconstructions | **C/D** | Do not present as documented |

**Dramatic fitness as opening:** **Reject.** Chronology dumps the reader on the eve of murder; overweights AMB-1/omen weather; fights SERIES and Act-1 runway.

Link: https://lexundria.com/suet_jul/87/r  

### Flexibility note
Moving Lupercalia to another year or inventing a second diadem day would be an **unacceptable** casual move of A4’s public meaning. Creating a **fictional dinner** in the clemency season, or opening on the **seated-honours insult** with C-attendance, is proportionate. Prefer smallest alteration that buys the dramatic effect.

---

## 4. Three opening concepts

### Concept A — Densify the existing street open (baseline)

**A. Premise.** Keep Thapsus/Cato morning as the book’s first movement: F4 prices Africa while the Forum invents morals; extend his run so the unfinished question (*what does closed Africa cost?*) lands harder before any second camera. Optional: fold a thin slice of triumph weather *into* F4’s afternoon rather than cutting to Nysa in the same chapter.

**B. POV.** **F4 Hordeonius** — proximity without power; misreads eloquence as air; concrete stake (Kalends payments, grain). Incomplete understanding is the point.

**C. Character introductions.** Cicero as bruise-in-frame (not POV); Sosia / cake-seller / veterans as street mouths; Domus runner as household pressure. Principals (Brutus, Cassius, Antony, Decimus) arrive later — by design.

**D. Hook.** Victory that is morally “closed” and economically unfinished; land hunger under spectacle.

**E. Continuity.** Preserves A1, FS10 seed, dual-engine street altitude; minimal map change. Downstream: Ch 2–7 unchanged in order.

**F. Risks.** Still slow to introduce elite rivalries; readers wanting “several important characters in one room” may feel delayed. Two-camera Ch 1 still splits if Nysa stays.

**G. Reader effect.** Knows: Africa won, Cato dead, city converting corpses to rates. Feels: grit, humour, unease. Suspects: land and paper will matter. Misunderstands: who will kill whom — correctly not yet on the table.

**Creative tests:** Character ✓ (F4 distinct) · Scene ✓ · Uncertainty ✓ · Emotion ✓ · Restraint ✓ · Continuity ✓ · POV: longer F4 block would help.

---

### Concept B — Clemency dinner as front door (private / semi-private gathering) ★

**A. Premise.** Night: a Caesarian host’s dining room. Clemency toasted as spice. Cassius digests insults and praise; a newly posted “New-Spain” laughs on cue; servants lean too near; Transtiberim queen/child talk prices something unnamed. Cassius leaves early; in the street, New-Spain’s confession makes forgiveness look like a posting market. **Shift:** resentment crystallises into geometry (who smiled wrong), not knives.

**B. POV.** **Cassius** — closest mix of proximity, grievance, and incomplete map. (Do not invent a new POV.) Alternate lens **F2 Seius** at the edge of such a room is possible but weaker for elite friction; keep Seius for later almost-recruit.

**C. Introductions (behaviour, not bios).**
- **Cassius** — courtesy as cover; leaves early; files silence with land.  
- **Host** — mercy as social technology.  
- **New-Spain** — employed laughter; corridor truth.  
- **Servants** — overhear risk as ordinary furniture.  
- Offstage pressure: Brutus as “spared ornament” named in talk, not yet present — or a burned-invitation aftermath from a prior beat folded lightly.  
- **Decimus** should *not* appear yet unless the scene is widened; save insider glow for a following portico beat.

**D. Hook.** Shared toast, incompatible interests: forgiveness that demotes; rumour that prices a foreign child; the sense that dinners are already doing politics.

**E. Continuity implications.**
- Fixed: clemency practice **A**; no A-event moved.  
- Invented: host, climber, exact dialogue (**D** — already soft-canon in Ch 4).  
- **Placement (see §11):** prefer **late 46** rework (Africa-favour climber) for chronological open; late-45 New-Spain + jump-back is the fallback.  
- Affected: Ch 4 SC-08 promoted/reshaped; F4 street same-year neighbour; Porcia / Decimus will-whisper decoupled to ~45; Ch 7 Lupercalia stays.  
- Avoid duplicating the dinner later — merge or demote any remnant.  
- Queen/child talk must remain rumour (no CLEO POV; no SIDE-1-as-Ides).

**F. Risks.** Overcrowd with conspirators; portentous maxims; accidental AMB-1 (“he knows”); starting too late and orphaning A1/Munda emotional runway unless street follow-up carries Africa/Cato.

**G. Reader effect.** Knows: pardoned men live under soft chains; postings and praise are uneven. Feels: social danger, humour with teeth. Suspects: resentment will organise. Misunderstands: schedule, knives, Caesar’s knowledge — correctly.

**Creative tests:** Character ✓✓ · Scene ✓ · Uncertainty ✓ · Emotion ✓ · Restraint (must police) · Continuity (needs careful reorder) · POV: **stay with Cassius for a long run**; do not cut to Brutus/Decimus in the same chapter.

---

### Concept C — Seated honours insult (senatorial occasion)

**A. Premise.** Consuls and Senate approach Caesar with voted honours; he remains seated. The room fractures into readings: illness, arrogance, Balbus’s hand, deliberate theatre. One consciousness — preferably **Decimus** (trusted legate glow) or **Cicero** (eloquence without legions) — must decide how to walk away from an insult to the *state* wearing a friend’s face.

**B. POV.** **Decimus** strongest for later betrayal voltage; **Cicero** strongest for “speeches vs power” theme. Prefer Decimus if the book wants insider unease early; Cicero if it wants Republic-as-rhetoric early.

**C. Introductions.** Caesar by refusal to rise (behaviour); Balbus if used (B); clustering senators by who laughs, who pales, who invents medical excuses; Decimus’s pride in access colliding with shame at the slight.

**D. Hook.** A constitutional insult delivered as etiquette; friendship and Republic no longer sit in the same chair.

**E. Continuity.** Preserves Plutarch 60 tradition (**A/B**). Chronology: early 44 — compresses or relocates 46–45 runway (A1/A2 become flashback/report). Risk of duplicating monarchy themes before Lupercalia.

**F. Risks.** Honours laundry-list exposition; looking like a “greatest hits of February 44” open when paired mentally with Lupercalia; Decimus interior may over-telegraph betrayal.

**G. Reader effect.** Knows: honours and insult. Feels: public shame. Suspects: something will answer the slight. Misunderstands: whether Caesar meant it — good; whether knives exist — not yet.

**Creative tests:** Character (medium) · Scene ✓ · Uncertainty ✓ · Emotion (medium) · Restraint (hard) · Continuity (harder than B) · POV: one long Decimus or Cicero chapter, not mosaic.

---

## 5. Comparative evaluation

| Criterion | A Current street | B Clemency dinner | C Seated insult |
|-----------|------------------|-------------------|-----------------|
| Immediate dramatic engagement | Strong (prices/blood) | Strong (room pressure) | Strong (public slight) |
| Natural multi-character intro | Weak–medium (street mouths) | **Strongest** | Medium (body as chorus) |
| Historical credibility | High (A1 news) | High if labelled **D** dinner | High (Plut. 60) |
| Emotional accessibility | High (F4 concrete) | High (Cassius digesting) | Medium (protocol) |
| Fit with existing MS | **Best** | Good with reorder | Fair (compresses Act 1) |
| Curiosity without fake mystery | Excellent | Excellent | Good if readings stay plural |
| Themes (plural motives, paper, speeches vs force) | Paper/land early | Clemency/obligation early | Dignity/honours early |
| Voice match to strongest passages | Matches F4 gold | Matches Ch 4/8 Cassius rooms | Needs new set-piece |

**Qualitative scores (1–5, secondary only):** A 4.2 · B **4.5** · C 3.7 — B wins on the brief’s gathering requirement; A remains the safest continuity choice.

### Why B over A
A delays the ensemble gathering the brief asked to investigate; B delivers rivalries and misunderstandings in one room without moving A4.

### Why B over C
C overlaps thematically with Lupercalia’s public monarchy weather and tempts a February-44 “hits reel.” B is socially specific and already half-written.

### Why not Lupercalia as Concept winner
It is the wrong *position*, not the wrong *scene*. As Ch 7 it converts private geometry into civic panic. As Ch 1 it spends the novel’s best public card before readers know why refusal smells like danger to these particular men.

### Sacrifices if B is chosen
- Africa/Cato moral shock becomes second movement (must not vanish).  
- Ch 4 needs demotion/merge to avoid double dinner.  
- Author must accept a modest Act-1 reorder (preference-level, not invariant).

---

## 6. POV audit

### Method
Inventory from **actual** `drafts/book1/*.md` POV headers (79 POV units across 34 chapters). Compared to CHAPTER_MAP / G1–G2 preferences.

### Opening-act inventory (Ch 1–13) — pattern summary

| Ch | POV units | Approx avg words/unit | Pattern |
|----|-----------|----------------------|---------|
| 1 | 2 (F4, F1) | ~520 | Intentional collision; still splits open |
| 2 | 2 (F2, F4) | ~484 | Alternating street INF |
| 3 | 2 (F3, F3) | ~384 | **Good block** (same POV) |
| 4 | 3 (Bru, Cas, Dec) | ~483 | **Fragmented principals intro** |
| 5 | 1 (OCT) | ~964 | **Model dwell** |
| 6 | 2 (Cic, F4) | ~512 | Acceptable if questions collide |
| 7 | 2 (Ant, Cas) | ~728 | Justified public→private |
| 8 | 2 (Cas, Bru) | ~830 | Strong rooms |
| 9 | 2 (Dec, Bru) | ~482 | Argument earns second lens |
| 10 | 3 (F2, F4, F4) | ~423 | SIDE-1 mosaic; F4 block partly saved |
| 11 | 2 (F1, Cic) | ~496 | Omens split |
| 12 | 3 (Cal, F1, Cae) | ~463 | Household mosaic pre-Ides |
| 13 | **4** (Treb/Dec, Cic, F3, Bru/Cas) | **~333** | **Worst fragmentation** |

### Three problems (do not collapse)

| Problem | Finding |
|---------|---------|
| **A — Scene clarity** | Generally **good**: POV labelled; little unmarked head-hopping in opening act. Ch 13 “Trebonius / Decimus” and Ch 27/30 shared labels are the soft spots. |
| **B — Chapter fragmentation** | **Real:** Ch 4, 10, 12, 13 change cameras before emotional consequence fully lands. Ch 13 is a sequence of summaries with one stronger GO room. |
| **C — Book-level rhythm** | Recurring: ~2 POV units modal; 11 chapters have 3+; only 3 chapters are true single-POV. Story-first plan already noted ~32/34 multi-POV historically; S-A2 fixed only some. Mid/late successes: Ch 5, 8, 26, 31. Persistent mosaics: Ch 19 (earned crisis), Ch 23, Ch 30 triptych. |

### Disruptive vs earned transitions
- **Earned:** Ch 7 Antony→Cassius (public test → disclosure); Ch 16 multi-POV (peak day); Ch 19 funeral mesh; Ch 3 F3–F3 continuity.  
- **Disruptive:** Ch 13 four-way; Ch 4 three short principal samples before any relationship run; Ch 1 cutting to Nysa before F4’s Kalends stake fully plays out; Ch 12 Caesar stub (~300w) after Calpurnia dread.

### Character blocks — costs/benefits
**Benefits:** Ch 5 and Ch 8 prove identification and private rationalisation improve when the camera stays.  
**Costs of forcing blocks everywhere:** would delay SIDE-1 street mouths and funeral polyphony; some characters cannot carry certain rooms.  
**Conclusion:** blocks by *dramatic unit*, not by quota.

---

## 7. Proposed opening-act rhythm map

Treatments are design guidance for a later pass — **not** implemented here.

| Existing | Current POV | Diagnosis | Proposed treatment | Reason |
|----------|-------------|-----------|--------------------|--------|
| Ch1 SC-01 | F4 | Strong open energy | **Keep**; extend run if Concept A; or **move to Ch2** if Concept B | Preserve street brand |
| Ch1 SC-02 | F1 | Early second camera | **Merge into F4 afternoon** *or* **defer to later Domus chapter** | G1: second POV only on unfinished question |
| Ch2 SC-03 | F2 | Debt world seed | Keep; consider **F2 mini-block** with Ch10 almost-recruit later | Relationship continuity |
| Ch2 SC-04 | F4 | Rates | Keep adjacent to SC-01 if F4 block pursued | Same consciousness |
| Ch3 SC-05/06 | F3 | Good block | **Keep unchanged** | Model |
| Ch4 SC-07 | Brutus | Short ancestral pressure | If Concept B: **follow dinner**, don’t lead; or **extend** into evening aftermath | Avoid three-sample chapter |
| Ch4 SC-08 | Cassius | Best gathering seed | **Promote toward open** (Concept B) / **extend** | Ensemble brief |
| Ch4 SC-09 | Decimus | Insider whisper | **Separate chapter or next-day block** | Don’t dilute dinner |
| Ch5 | OCT | Model sole POV | **Keep unchanged** | Earned dwell |
| Ch6 | Cic / F4 | Two altitudes | Keep if collision clear; else split chapters | Paper vs speech |
| Ch7 SC-16/15 | Ant / Cas | Earned pair | **Keep position**; do not open book here | Public payoff |
| Ch8 | Cas / Bru | Strong | **Keep**; prefer longer Brutus room | Recruitment |
| Ch9 | Dec / Bru | Argument | Keep; ensure spare-Antony consequence lands in Decimus | M6 |
| Ch10 | F2 / F4 / F4 | Busy | **Merge F4 pair**; keep F2 separate chapter if needed | SIDE-1 clarity |
| Ch11 | F1 / Cic | Split | Keep or place Cicero alone | OMEN-1 |
| Ch12 | Cal / F1 / Cae | Pre-Ides mosaic | **Calpurnia block**; fold Nysa; keep Caesar sparse but not stub-thin | Dread continuity |
| Ch13 SC-31–34 | 4 POVs | **Fragmentation peak** | **Merge Trebonius into Decimus camera**; move Cicero and F3 to adjacent chapters; keep GO room as Brutus/Cassius climax | Problem B fix |

### Wider manuscript (largest patterns only)
- **Preserve:** Ch 5, 8, 26, 31 sole/long runs; Ch 16–19 crisis polyphony.  
- **Revise later (not this pass):** Ch 23 three-way street; Ch 30 proscription triptych → one dominant + reports; Ch 20 Decimus→Cleopatra→Octavian (exit triptych — purposeful but cold).  
- **No full-book restructure required** unless Concept B open is approved.

---

## 8. Continuity impact (Concept B recommended path)

| Check | Result |
|-------|--------|
| Lead into following chapters? | Yes, if Ch1 street follows as “next weather” and Ch4 dinner is not repeated |
| Duplicate shortly after? | Risk only if SC-08 left intact later — **merge/demote** |
| Principals vanish too long? | Opposite risk: they arrive earlier; F4 must reappear soon so street brand doesn’t die |
| Promise wrong genre? | Avoid knives, omens-as-proof, SIDE-1 master key in open |
| New knowledge breaking later scenes? | Do not let Cassius learn ops facts Ch 8–9 assume he lacks; keep geometry, not schedule |
| Chronology distortion? | None if dinner stays 45–early 44 **D**; do not move A4/A5 |
| Mystery invariants? | AMB-1 untouched; NOTE-1 not planted here; SIDE-1 not Ides-cause; AMB-3 no narrator divine |
| Theme fit? | Soft chains, plural motives, speeches vs postings — yes |
| Voice? | Match Ch 4/8 Cassius manners-as-cover |
| Want the novel that exists? | Yes if street INF returns by movement two and Lupercalia remains mid-act |

**SIDE-1 / mysteries:** Opening dinner may mention debt and silence; must not frame ash-body as the road to the Curia.

---

## 9. Recommended next step (reviewable, small)

**Do not rewrite chapters yet.**

1. Author confirms **§11 verdict** (chronological late-46 dinner rework) or overrides to jump-back Option 1.  
2. Produce a **one-page Opening Reorder Sketch** for new Ch 1–4 (dates, POV, what retools vs moves) for approval.  
3. Regardless: schedule a **bounded POV rhythm pass** targeting Ch 13 first, then Ch 4/12 — merges and deferrals only, no new beats.

---

## 10. Decisions this report enables (without making them)

1. **Opening occasion:** current street (A) · clemency dinner gather (B) · seated honours (C) · Lupercalia-as-Ch1 (**not recommended**).  
2. **Dinner placement (§11):** late-46 chronological rework (**recommended**) · late-45 dinner then signalled jump to 46 · keep current Ch 4 seat.  
3. **POV rhythm:** retain mosaic habit · adopt one-dominant-default + crisis exceptions (**recommended**) · rigid character-block novel (**not recommended**).

---

## 11. Placement test — dinner-first jump vs chronological rework

**Question:** Given Concept B, which works better?

| Option | Shape |
|--------|--------|
| **1 — Jump** | Open on the current late-45 dinner energy → clearly signalled return to 46 BC (F4 Thapsus) → catch up |
| **2 — Rework date** | Move/retool the fictional dinner earlier so the book can open chronologically without a backward jump |

**Manuscript facts that decide it**
- Current SC-08 depends on **“New-Spain”** (Spanish posting) → dramatically natural **after Munda (45)**, not in spring 46. Beat sheet B08 already parks the dinner in **late 45**.  
- **Queen / child / Transtiberim** talk requires Cleopatra’s Roman lodging: soft anchor S2 = presence **46–44** (**B**); she arrives **late 46** after Caesar’s return/triumphs (Attalus year-46 lists; Suet. *Iul.* 52 / Dio 43.27 tradition). Gossip is usable from late 46 onward — **sharper** when the lodging is new.  
- Ch 4 bundles three seasons in one chapter: Porcia pressure (marriage soft-anchor **~45**), Cassius dinner (Spain slight), Decimus will-whisper (FS05 **45–early 44**). Those need not stay glued together.  
- Downstream callbacks (Ch 6 stalls, Ch 17–18 gardens/boy, Ch 20 Cleo payoff) need the *plant*, not the Spanish job title.

### Option 1 — Dinner first, then return to 46

**How it would work**
- Ch 1: Cassius dinner (keep New-Spain, soft-chain slight, queen talk) dated **late 45**.  
- Ch 2: Explicit temporal reset — chapter title + first-line date stamp + one didactic beat (“Two winters earlier, when Africa still smelled like a closed account…”) — into F4 Thapsus/Cato.  
- Then chronological climb through triumph → Munda → reconnect to late 45 *without replaying* the dinner.

**What it preserves**
- Post-Munda posting economy (strongest current slight).  
- Porcia / Decimus can stay in the late-45 nest beside the dinner.  
- Ensemble on page one.

**What it costs**
- **Reader trust:** invests in Cassius’s geometry, then spends chapters in a past that the reader already knows leads to soft chains — A1’s moral shock lands as illustration, not discovery.  
- **Reconnect tax:** when the timeline reaches late 45 again, the dinner must be treated as already lived (memory/echo only) or the open was a prologue cheat.  
- Signaling must be industrial-strength; soft “meanwhile” will read as confusion, not design.

**Verdict on Option 1:** Viable if Spanish-posting texture is judged essential. Inferior default for this manuscript’s dual-engine runway.

### Option 2 — Rework dinner date/placement for chronology ★

**Historically plausible rework (smallest change that unlocks chronology)**

| Element | Current (late 45) | Late 46 rework |
|---------|-------------------|----------------|
| Clemency toast | Soft chains after civil war | Same — after Thapsus/Cato; mercy as spice still **A**-practice |
| Climber’s posting | **New-Spain** | **New-Africa** (or “new grain / new Numidian favour”) — **D** rename |
| Queen/child talk | Transtiberim rumour | Same content; **hotter** — lodging just opened |
| Host / Cassius behaviour | Unchanged | Unchanged |
| Porcia SC-07 | Same night as dinner | **Decouple** → ~45 with marriage pressure (S1) |
| Decimus SC-09 will whisper | Same chapter | **Keep ~late 45** (FS05); do not force into 46 open |
| F4 Thapsus street | Ch 1 now | Same year, **before or beside** dinner (spring/summer news → autumn dinner) |

**Chronological open shapes (both OK)**
- **2a:** Ch 1 = late-46 Cassius dinner → Ch 2 = same-week F4 market weather (sermons vs ledgers) — ensemble first, **no jump**.  
- **2b:** Ch 1 = F4 Thapsus (spring/summer 46) → Ch 2 = late-46 dinner — chronological honesty + early ensemble without flashback.

**Motivation check:** Cassius “forgiven into irrelevance” still holds in 46 (clemency after Pharsalus/Africa climate). The slight becomes *who got Africa’s spoils*, not Spain’s — same emotional geometry. Munda (Ch 3) then **ironises** the peace toast: the war was not finished. That is a gain, not a loss.

**Continuity check:** Queen plant still predates Ch 6/17/18/20. SIDE-1 / AMB-1 / NOTE-1 untouched. No A-event moved. Only **D** dinner furniture retuned.

**What it costs**
- Lose New-Spain’s post-Munda specificity (replace with Africa-favour).  
- Split Ch 4’s three-camera sample across years (good for POV rhythm anyway).

### Head-to-head

| Criterion | Option 1 Jump | Option 2 Rework date |
|-----------|---------------|----------------------|
| Ensemble on/near page one | Strong | Strong (2a) / strong-by-Ch2 (2b) |
| Chronological clarity | Weak unless over-signalled | **Strong** |
| Historical plausibility | High (keeps late-45 D) | High (late-46 D; Cleo arrival fits) |
| Cassius motive integrity | High | High if Africa-favour retuned |
| A1 Thapsus as lived discovery | Damaged (flashback) | Preserved (2b) or same-year neighbour (2a) |
| Downstream continuity | Reconnect tax | Light retool only |
| Accidental confusion risk | **High** | Low |

### Recommendation
**Option 2 works better.** Rework the fictional dinner to **late 46 BC**, swap New-Spain → Africa-favour, keep queen/child talk, decouple Porcia and Decimus will-whisper to ~45, and open chronologically (prefer **2a** if ensemble-first is the priority; **2b** if A1 discovery-first is the priority).

Use Option 1 only if the author explicitly wants to keep the Spanish-posting slight and accepts a prologue-style open with a hard dated reset into 46.

**Still not implementing prose.** Next concrete doc step remains the one-page Opening Reorder Sketch under the chosen option.

---

*End opening & POV design review. No manuscript changes in this pass.*

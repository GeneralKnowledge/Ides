# Writing brief — Book 1

**Project:** *The Ides of March — Historical Fiction Foundation*  
**Stage (2026-10-24):** Book 1 is fully drafted (prologue, Ch 1–36, back matter) and with Gate 3 readers. Work now is revision, reader-led fixes and, where a story need is shown, development (`HUMAN_VOICE_RULES.md` §1a).  
**Not your job:** Rebuild the world, invent a new plot spine, resolve every mystery, or modernise Roman motives.

**Revising a landed chapter?** §12 (historical verification and change-impact review) applies to any substantive edit, alongside the evidence and stopping rules in `HUMAN_VOICE_RULES.md`. Release readiness is decided by `FINAL_READINESS_GATE.md`.

**Lock tiers:** Not every entry in `canon.md` is the same kind of lock. See [`continuity/lock_architecture_audit.md`](../continuity/lock_architecture_audit.md): historical invariant · narrative invariant · continuity commitment · structural preference · editorial guardrail. Preserve what must remain true; prefer freedom over *how* the story makes it true. Protection ≠ immunity.

---

*Section numbers are kept from the drafting-era brief so cross-references (§8, §12) still hold; §5–6 and §9–10 are retired to the history note at the end.*

## 1. What to read

Read what the job touches, not the whole library:

- **Any change:** the chapter itself in `drafts/book1/` and its continuity notes; this brief; `HUMAN_VOICE_RULES.md`; `STYLE_GLOSSARY.md`.
- **A fact, date or who-knows-what:** `continuity/canon.md`, `story/historical_anchors.md`, and §12 below.
- **A POV or voice question:** `story/pov_lock.md`, `voice/POV_DICTION.md`, `continuity/character_profiles/`.
- **New story (development):** `continuity/expansion/subplot_tracks.md`, `story/flexibility_zones.md`, `story/mysteries.md`.

If a choice conflicts with a **historical or narrative invariant** in `canon.md` or an Anchor A#, **canon/anchor wins**. Structural preferences (chapter map, POV allocation, CHOREO-1 ordinals) guide; they do not veto a stronger demonstrated solution that keeps invariants.

---

## 2. What success looks like

A book that:
- Hits historical anchors in the right order  
- Rotates the POV ensemble (knowledge bans stay hard)  
- Keeps information asymmetric (characters do not share the author’s knowledge)  
- Preserves ambiguity on narrative-invariant mysteries (densify evidence OK; collapse not)  
- Feels Roman (patronage, honour, religion-as-practice, debt, veterans) not fantasy-Westeros or modern Capitol Hill  
- May steal **craft** from Spartacus dialogue bite + GRRM grey humour (`TONE-1`) without importing dragons, “m’lord,” or arena soap  

---

## 3. Hard prohibitions

1. No confirmed supernatural narrator voice (omens stay ambiguous).  
2. No Shakespearean “Et tu, Brute?” as historical fact.  
3. No Octavian-as-Augustus calm mastermind in 44–42.  
4. No hive-mind conspirators; motives stay plural.  
5. No moving Ides date/place/outcome; murder is at **Curia of Pompey**.  
6. No Octavian in Rome on 15 March 44.  
7. No secret child of Caesar who steers history; no time-traveller irony spoken aloud.  
8. No solving all mysteries; do not explain every omen.  
9. Do not make Cicero a dagger conspirator.  
10. Do not give Liberators a secret army in Rome on the Ides that would make their collapse incoherent.  
11. Do not teleport; respect travel times in `rome_topography.md` / locations.  
12. Do not turn SIDE-1 into the “real” reason for the Ides.  
13. Do not run detector-led prose loops or scrub character-true diction into sameness — see `HUMAN_VOICE_RULES.md` (feel over scores; two style-only passes per chapter at most).

---

## 4. POV rules for prose

**Regular POVs:** Decimus, Brutus, Cassius, Antony, Cicero, Octavian, plus F1 Nysa, F2 Seius, F3 Laberius, F4 Hordeonius.  
**Specials:** Caesar (sparse, Acts 1–2 only), Calpurnia, Servilia, Fulvia, Cleopatra.

- Close third person limited **or** first person — pick one per book and stay consistent (**VOICE-1 default below**).  
- Only one POV per scene. A scene card may split into sub-headed POV movements (e.g. *Antony / Decimus*), each a clean single POV with a visible break; no head-hopping inside a movement.  
- POV only knows their information state (see the chapter’s continuity notes).  
- Filter sensory world through status (senator ≠ freedwoman ≠ centurion).

**VOICE-1:** Close third person limited, past tense, minimal free indirect “wink” at the future.

---

## 7. Tone & world texture (must)

- Patronage mornings, debt, slaves listening, mud, ritual blood, bad teeth, perfume over rot.  
- Religion practised sincerely *and* cynically — often in the same person.  
- Liberty rhetoric can be real *and* self-serving.  
- Veterans and crowds outvote eloquence.  
- Letters are physical objects (seals, couriers, forgery fear).  
- Avoid: purple-glow aesthetic, modern quips, egalitarian banter across status without cost, clean white-marble tourism Rome.

---

## 8. Mystery & theory hygiene

Keep live (do not settle in narration):
- M1 Caesar’s knowledge  
- Dream meaning  
- Whether omens were “true”  
- Decimus’ deepest motive  
- Spare-Antony wisdom vs folly  
- Pansa poison  
- SIDE-1 killer  

Seed evidence for ≥2 interpretations when a mystery appears.

---

## 11. When unsure

1. Check `canon.md`  
2. Check the chapter’s continuity notes and `CHAPTER_MAP.md` row  
3. Prefer ambiguity + consequence over clever twist  
4. Leave a `// TODO_EDITOR:` comment rather than inventing a new historical fact  

If you invent a minor D-detail (servant name, exact dinner dish), keep it consistent and list it under Continuity notes for later canon logging.

---

## 12. Revising landed chapters (mandatory for substantive edits)

A **substantive edit** changes a fact, a date or sequence, who knows what, a relationship, an object, a promise or debt, or what a line of dialogue means. Typo, punctuation and pure rhythm fixes are not substantive. Every substantive edit must pass both checks below and the evidence-before-edit rule in `HUMAN_VOICE_RULES.md` §1.

### 12a. Historical and chronological verification

Any historical claim that could materially mislead a reader is checked against a reliable source: an ancient text (Cicero’s letters, Appian, Plutarch, Suetonius, Dio, Nicolaus) or standard modern scholarship. Another project document is a pointer, not a source. A disputed fact does not become certain because several project files repeat it.

Take particular care with:

- dates, travel times, offices held, and the order in which news arrives;
- who could know what, and when;
- quotations, Latin, names, titles and terminology;
- the line between documented fact, disputed evidence and invented private behaviour.

Record the source and an A/B/C/D certainty label (`docs/README.md`) in `research/citation_verification.md` or the relevant research file.

**Acceptance:** no unresolved high-impact factual error; lower-impact uncertainty is recorded, not silently treated as fact.

### 12b. Change-impact review

A chapter is not approved in isolation when the change reaches other chapters. Trace the dependencies of *this* change and verify those; do not rerun every continuity audit.

- Does each character know what the scene now assumes they know?
- Do travel, orders, letters and rumours still arrive in the right sequence?
- Do injuries, objects, promises, debts and relationships persist correctly before and after?
- Do later scenes that rely on the passage still make sense?
- Has an ambiguity or mystery (§8) been resolved by accident?

Note the dependents you checked in the PR or pass log. If a continuity commitment in `canon.md` moves, update the log and its dependents in the same change.

**Acceptance:** the revision introduces no broken causal chain and no unexplained change in knowledge, chronology or established fact.

---

## History: first-pass drafting (retired 2026-10-24)

The book was first drafted from scene cards (now in `archive/planning/story/scene_cards/`). The drafting rules below are kept as a record. They do **not** bind revision: there are no per-scene word targets, no required overhears, and no ensemble percentages.

- Scenes were drafted one at a time from `SCENE_TEMPLATE.md`, ending when the information state changed.
- Default ensemble mix per act was roughly 40% historical principals, 30% fictional POVs, 20% specials and letters, 10% crowd texture; the point was not to write the Ides only from Brutus.
- Draft order was Act 2–3 first to test voice, or Act 1→5 for continuity, one chapter at a time.
- Book 1 was drafted as a single volume through Philippi with sequel hooks only (SERIES-1, `canon.md`).


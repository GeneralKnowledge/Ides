# LLM Writing Brief — First-Pass Draft Instructions

**Project:** *The Ides of March — Historical Fiction Foundation*  
**Your job:** Write a **first-pass draft** (scenes/chapters) that will be human-edited later.  
**Not your job:** Rebuild the world, invent a new plot spine, resolve every mystery, or modernise Roman motives.

Read this file before drafting. Obey it over improvisation.

**Lock tiers:** Not every entry in `canon.md` is the same kind of lock. Prefer [`continuity/lock_architecture_audit.md`](../continuity/lock_architecture_audit.md): historical invariant · narrative invariant · continuity commitment · structural preference · editorial guardrail. Preserve what must remain true; prefer freedom over *how* the story makes it true. Protection ≠ immunity.

---

## 1. Mandatory reading order (before any prose)

1. `docs/executive_overview.md`  
2. `continuity/canon.md` (**locks + tiers**) + skim `continuity/lock_architecture_audit.md` when proposing structural change  
3. `story/historical_anchors.md`  
4. `story/pov_lock.md` + `story/characters/*`  
5. `story/scene_cards/` for the act you are drafting  
6. `story/ides_week_hour_map.md` (for Act 2–3)  
7. `writing/MUST_EXPRESS.md` (behavioural checklist — outcomes may travel by alternate scene delivery)  
8. `writing/STYLE_GLOSSARY.md`  
9. `writing/voice/TONE_SPARTACUS_GRRM.md` + `voice/POV_DICTION.md` (humour / personality lenses)  
10. Supporting: `research/tables/conspirator_matrix.md`, `research/rome_topography.md`, `story/information_network.md`, `story/mysteries.md`

If a choice conflicts with a **historical or narrative invariant** in `canon.md` or an Anchor A#, **canon/anchor wins**. Structural preferences (chapter map, POV slot counts, CHOREO-1 ordinals) guide; they do not auto-veto a stronger demonstrated solution that keeps invariants.

---

## 2. What success looks like

A usable first pass that:
- Hits historical anchors in the right order  
- Rotates the preferred POV ensemble (knowledge bans stay hard)  
- Keeps information asymmetric (characters do not share the author’s knowledge)  
- Preserves ambiguity on narrative-invariant mysteries (densify evidence OK; collapse not)  
- Feels Roman (patronage, honour, religion-as-practice, debt, veterans) not fantasy-Westeros or modern Capitol Hill  
- May steal **craft** from Spartacus dialogue bite + GRRM grey humour (`TONE-1`) without importing dragons, “m’lord,” or arena soap  
- Leaves threads for editing (rough is OK; contradiction with invariants is not)

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

---

## 4. POV rules for prose

**Regular POVs:** Decimus, Brutus, Cassius, Antony, Cicero, Octavian, plus F1 Nysa, F2 Seius, F3 Laberius, F4 Hordeonius.  
**Specials:** Caesar (sparse, Acts 1–2 only), Calpurnia, Servilia, Fulvia, Cleopatra.

- Close third person limited **or** first person — pick one per book and stay consistent (**VOICE-1 default below**).  
- Only one POV per scene.  
- POV only knows their information state (see scene card Enter/Exit).  
- Filter sensory world through status (senator ≠ freedwoman ≠ centurion).

**VOICE-1 default for first pass:** Close third person limited, past tense, minimal free indirect “wink” at the future.

---

## 5. How to draft a scene

Use `writing/SCENE_TEMPLATE.md`:

1. Copy the scene card (SCxx).  
2. Fill Enter info → play the beat → Exit info must match the card.  
3. Include at least one overhear/leak risk if the card marks overhear ≥ Medium.  
4. End scene when the info state has changed — do not overstay.  
5. Tag draft header with: `SC-id · POV · Anchor/Mystery · Certainty notes`

Target length first pass: **800–2000 words** per scene unless card is a set-piece (Antium, Ides, funeral, Philippi) → **1500–3500**.

---

## 6. Ensemble pacing (default)

Per act, aim roughly:
- ~40% historical principals  
- ~30% fictional POVs (F1–F4)  
- ~20% specials / letters / reports  
- ~10% public/crowd texture without head-hopping  

Do not write the whole Ides only from Brutus.

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

## 9. Series shape for this pass

**SERIES-1 default:** Draft as a single volume through Philippi (Acts 1–5), with sequel hooks (land rage, Sextus, Antony–Octavian) — **do not** write Actium/Egypt endgame.

Suggested draft order for an LLM pass:
1. Act 2–3 first (conspiracy + Ides) if testing voice  
2. Or Act 1→5 in order for continuity  

Prefer **scene-by-scene** generation following `writing/CHAPTER_MAP.md`, not one-shot whole novel.

---

## 10. Output format per scene file

```
# SC-XX — Short title
POV: …
Date/place: …
Canon refs: …
Info enter → exit: …

[prose]

## Continuity notes (bullets)
- What new Private/Faction knowledge exists now
- Open mysteries touched
```

---

## 11. When unsure

1. Check `canon.md`  
2. Check scene card  
3. Prefer ambiguity + consequence over clever twist  
4. Leave a `// TODO_EDITOR:` comment rather than inventing a new historical fact  

If you invent a minor D-detail (servant name, exact dinner dish), keep it consistent and list it under Continuity notes for later canon logging.

# Punic War experiment: voice rules

**Status:** Frozen for the draft on 7 November 2026, after Reuben read the voice pilot ("Sounds good as a base"). Changed only by Reuben.

These are the Book 1 rules as they ended (`writing/HUMAN_VOICE_RULES.md`, `writing/STYLE_GLOSSARY.md`), cut down to what can be checked, plus what the pilot set. The pilot scenes in [`pilot/`](pilot/) are the reference for tone.

## Every scene

1. Close third person, past tense, one POV per scene.
2. No narrator explainer sentences ("X was the …", history lessons). A POV may hold a fact in one clause of memory. Dialogue may tell a listener something he does not know, remind him of something the way people do, or use a fact as leverage. No briefing someone on what both know.
3. Each real person is introduced once, through what the POV sees and knows; later scenes show them, they do not list their traits again.
4. Hannibal has no POV and is never given a thought the viewer could not see or hear.
5. Nothing marked "to check" in the canon is stated as fact in a scene without being flagged in the scene's header.

## Sentences

6. No em dashes in prose.
7. No caption fragments (habit I): no one-word or verbless sentence that labels the sentence before it. One-word sentences in narration only where the stop itself is the event, about one per act.
8. No "filed", no ledger dialect in mouths that do not own it. Hanno counts money because he is Hanno; nobody else does it for colour.
9. One simile per beat at most; prefer what a body does.
10. No proverb that sums up a cost already shown (habit D). End scenes on a thing, an act or a line of speech, not a thesis.
11. No modern weekdays or hours; Roman dates in Roman mouths, seasons for weather (chronology calendar warning).

## The voice set by the pilot

12. **Plain and physical.** Weather, cold, food, feet, money. The war is felt before it is understood.
13. **Dry humour from people who do not know they are funny** (Sabidius and breakfast; Hanno being slow and old). None at Cannae or the head.
14. **Each POV sounds like their job.** Vettius: body and rumour. Hanno: weight and price. Fabius: slow, few words. Varro: crowds and quick sums of votes. Scipio: performance, half aware of itself. Maharbal: horses, ground and distance. Silenus: a writer's eye, vain about a good sentence, counting omens and numbers. Pacuvius: two cities, timing.

## Spelling and marks

15. UK spelling. Curly quotes and apostrophes; ’s possessives (Mago’s, Fabius’s).

## Checks

`tools/punic_draft_check.py` counts em dashes, one-word narration sentences, "filed" and "little did", and words per scene against the storyboard. A scene over its budget by more than 20% is flagged.

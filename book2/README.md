# Book 2: the Second Punic War

Working folder for the second book in the series: one novel from Hannibal's descent from the Alps (218 BC) to the Metaurus (207 BC). Book 1 (the Ides) is untouched by anything here.

The method is the one in [Book 2 plan: lessons from Ides](https://claude.ai/artifact/XpDbPjMytLQwm5fhUsfENy): settle the shape and the facts first, draft each act once at full length, and put a stamped copy in front of an outside reader at the end of every act.

## Where things stand

| Stage | What | Status |
|---|---|---|
| 1 | [Book contract](CONTRACT.md) | Merged (#203) |
| 2 | Canon pack: [chronology](canon/chronology.md), [character sheets](canon/characters/README.md), [names](canon/names.md), [places](canon/places.md) | Merged (#203); Cannae and Metaurus passages still to check by hand |
| 3 | [Storyboard](storyboard/README.md) and reader questionnaire | Storyboard v1.1 (68 scenes); fixes settled 7 Nov; [Act I questionnaire](storyboard/questionnaire_act1.md) written |
| 4 | [Voice pilot](pilot/README.md) (two scenes) | Approved as a base (7 Nov); voice locked in [RULES.md](RULES.md) |
| 5 | Draft by act | Act I drafted (18 scenes, 22,600 words, `draft/act1/`); awaiting outside reader |
| 6 | Readers and freeze | Not started |

No prose until stages 1 and 2 are approved.

## Checks

```
python3 tools/book2_canon_check.py          # structure, sources, duplicate names
python3 tools/book2_canon_check.py --strict # also fails on anything still marked "to check"
python3 tools/book2_storyboard_check.py   # rewinds, POV gaps, act budgets, Cannae position
python3 tools/book2_draft_check.py        # words per scene, em dashes, banned words, straight quotes
python3 tools/export_book2_docx.py --acts I   # stamped reading copy; chapter numbers assigned here only
```

The canon check's `--strict` mode will be needed before the act that uses each "to check" line is drafted.

## Changelog

One line per change.

- 2026-11-07: Folder created. Contract drafted under Reuben's four decisions (Alps to Metaurus; Hannibal from outside; 100,000 words; this folder). Chronology, POV character sheets, major figures and names list drafted; first source check against Polybius and Livy.
- 2026-11-07: POV open questions settled on the recommended answers (Reuben: "go with what makes most sense"): Varro gets an Etruria scene in 207; Fabius's toga story is hearsay; Ticinus told straight; Maharbal fades after Act III; Silenus sees the head; Pacuvius runs to Capua's fall; the soldier farms near the Via Latina.
- 2026-11-07: Places and travel times added. Second source pass confirmed Liv. 21.12, 22.8, 22.25, 23.2, 26.8–9; Perolla dropped. Storyboard v1: 67 scenes, ~100k words, Cannae at 28%; storyboard check script.
- 2026-11-07: Storyboard fix 1 made (I-15b, Fabius warns Paullus); soldier named Lucius Vettius. Voice pilot written: I-04 The River (Trebia, Vettius) and II-12 Rings (Carthage, Hanno).
- 2026-11-07: Voice pilot approved as a base; rules locked in RULES.md. Act I drafted in full (18 scenes, 22,600 words against a 26,600 budget); draft check and stamped DOCX exporter added; Act I reader questionnaire and key.

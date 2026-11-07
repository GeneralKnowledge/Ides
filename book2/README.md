# Book 2: the Second Punic War

Working folder for the second book in the series: one novel from Hannibal's descent from the Alps (218 BC) to the Metaurus (207 BC). Book 1 (the Ides) is untouched by anything here.

The method is the one in [Book 2 plan: lessons from Ides](https://claude.ai/artifact/XpDbPjMytLQwm5fhUsfENy): settle the shape and the facts first, draft each act once at full length, and put a stamped copy in front of an outside reader at the end of every act.

## Where things stand

| Stage | What | Status |
|---|---|---|
| 1 | [Book contract](CONTRACT.md) | Draft, awaiting Reuben |
| 2 | Canon pack: [chronology](canon/chronology.md), [character sheets](canon/characters/README.md), [names](canon/names.md) | First version, awaiting Reuben; places and travel times still to do |
| 3 | Storyboard and reader questionnaire | Not started |
| 4 | Voice pilot (two chapters) | Not started |
| 5 | Draft by act | Not started |
| 6 | Readers and freeze | Not started |

No prose until stages 1 and 2 are approved.

## Checks

```
python3 tools/book2_canon_check.py          # structure, sources, duplicate names
python3 tools/book2_canon_check.py --strict # also fails on anything still marked "to check"
```

The storyboard gate runs with `--strict`.

## Changelog

One line per change.

- 2026-11-07: Folder created. Contract drafted under Reuben's four decisions (Alps to Metaurus; Hannibal from outside; 100,000 words; this folder). Chronology, POV character sheets, major figures and names list drafted; first source check against Polybius and Livy.
- 2026-11-07: POV open questions settled on the recommended answers (Reuben: "go with what makes most sense"): Varro gets an Etruria scene in 207; Fabius's toga story is hearsay; Ticinus told straight; Maharbal fades after Act III; Silenus sees the head; Pacuvius runs to Capua's fall; the soldier farms near the Via Latina.

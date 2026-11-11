# Book 2

The second book of the series. It follows straight on from Book 1: it opens in spring 41 BC, the morning after Laberius steps over the twine near Capua, and runs to the peace of Brundisium in autumn 40 BC. Its war is the Perusine War.

(An earlier trial of the planning method on a different story, the Second Punic War, lives in `experiments/punic_war/`. Nothing in it is canon here.)

The method is in [Book 2: starting where Book 1 ends](https://claude.ai/artifact/FBQquskjMXjX38ZkcVkY6r). In short: settle the handover, contract, canon, mind sheets and storyboard before any prose; pass a blind voice pilot against Book 1's model scenes; draft each act once at full length; check each act once (three-tests self-audit, continuity audit, one outside reader on a stamped copy); finish with a structure audit and one criticism-only cold read with nothing protected.

## Where things stand

| Stage | What | Status |
|---|---|---|
| 0 | [Handover from Book 1](canon/handover.md) | Checked against Book 1's text |
| 1 | [Contract](CONTRACT.md) | Approved by Reuben, 11 Nov |
| 2 | Canon pack: [chronology](canon/chronology.md), [places and travel times](canon/places.md), [names across both books](canon/names.md) | First version; lines marked (check) still to confirm |
| 3 | [Mind sheets](voice/MIND_SHEETS.md) (carried and new POVs), [storyboard](storyboard/README.md), questionnaire | Storyboard v2 with Reuben's seven picks (44 scenes, 88,800 words); questionnaire and key written |
| 4 | [Blind voice pilot](pilot/README.md) (three scenes, shuffled with three Book 1 model scenes) | PASSED 11 Nov (reader ranked the Book 2 scenes 2nd, 3rd and 6th of six; "belong to the same novel") |
| 5 | Draft by act, one PR per act | Not started |
| 6 | Structure audit, cold read, freeze (DOCX only) | Not started |

No prose until the storyboard and the voice pilot pass.

## Authorities

- Voice: `writing/voice/MIND_SHEETS.md` (Book 1 sheets carry over; Book 2 adds a short "since Philippi" note for each carried POV and new sheets for new POVs).
- Standing rules carried from Book 1: history accuracy; real people first, invent only where the record is silent; no em dashes; no caption fragments; no narrator explainer sentences; no bans or quotas; DOCX only.
- New for Book 2: no chapter or scene is protected from criticism (protect named beats only); chapter numbers are assigned at export from scene order; one changelog line per change, no pass logs.

## Checks

```
python3 tools/book2_names_check.py       # one handle, one person, across both books
python3 tools/book2_storyboard_check.py  # rewinds, POV gaps, act budgets, where the Ides of March 40 falls
```

## Changelog

One line per change.

- 2026-11-11: Folder created. Reuben chose the span (spring 41 to Brundisium, autumn 40). Handover and contract drafted on the recommended answers for POVs, the twine opening and length, pending his check.
- 2026-11-11: Canon pack first version. Chronology 42–40 BC with sources (Appian *BC* 5, Dio 48, Suetonius *Aug.* 13–15, Plutarch *Ant.* 25–31 read in translation; Suetonius 62–73 not reachable, marked check). Places and travel times. Names across both books with a check script. Handover check lines confirmed against Book 1 (Rufrius not mentioned after Philippi; Lepidus and Africa; Calpurnia at her father's; Atia dead in 43).
- 2026-11-11: Mind sheets for Book 2 (since-Philippi notes for Laberius, Nysa, Octavian, Hordeonius; new sheets for Fulvia and Lucius Antonius). Storyboard v1: 43 scenes, 87,000 words, Ides of March 40 at 72%; seven fixes for Reuben.
- 2026-11-11: Reuben picked all seven storyboard recommendations. Storyboard v2: Hordeonius II-06b and III-08b added, IV-11 cut (Nysa's wedding count ends the book), twine promise set (until the beans are in), one Nonius. Contract approved; hinge at 75%. Reader questionnaire (34 questions) and key.
- 2026-11-11: Voice pilot written (I-01 Laberius, II-03 Fulvia, II-06 Lucius) and the blind packet built with three Book 1 scenes; key in project files only.
- 2026-11-11: Voice pilot passed. B and F endings restored after the reader praised them; explaining lines trimmed in D and F; Laberius sheet asks for more particulars.

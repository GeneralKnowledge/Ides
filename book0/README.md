# Book 0

The prequel. It runs from January 49 BC, the morning after the Rubicon, to autumn 47 BC, when Caesar's legions are called *Quirites* on the Field of Mars and promised land with no date. Book 1's prologue (Utica, April 46) follows a few months later.

The series plan, with the through-line and the options for the period, is in [Series plan and Book 0](https://claude.ai/artifact/B1rPPha17L6VAEmSPWJJZq). The method is Book 2's ([book2/README.md](../book2/README.md)): settle the handover, contract, canon, mind sheets and storyboard before any prose; pass a blind voice pilot against Book 1's model scenes; draft each act once at full length; one outside reader per act.

Because Book 0 is written after Books 1 and 2, its handover runs backwards: it lists what the later books have already fixed. Building it found some things in Books 1 and 2 worth settling; those are in [CROSS_BOOK_FINDINGS.md](CROSS_BOOK_FINDINGS.md).

## Where things stand

| Stage | What | Status |
|---|---|---|
| 0 | [Handover from Books 1 and 2](canon/handover.md) (what is already fixed) | First version, checked against Book 1's text |
| 1 | [Contract](CONTRACT.md) | Working draft on the series-plan recommendations; awaiting Reuben |
| 2 | Canon pack: [chronology](canon/chronology.md), [places](canon/places.md), [names](canon/names.md) | First version; lines marked (check) still to confirm |
| 3 | [Mind sheets](voice/MIND_SHEETS.md) ("before" notes), [storyboard](storyboard/README.md), [questionnaire](storyboard/questionnaire.md) | Storyboard v1 |
| 4 | Blind voice pilot | Not started; needs Reuben's go |
| 5 | Draft by act | Not started; recommended after Book 2 |
| 6 | Structure audit, cold read, freeze | Not started |

No prose until the storyboard and the voice pilot pass.

## Checks

```
python3 tools/book0_storyboard_check.py
python3 tools/book2_names_check.py --names book0/canon/names.md
```

## Changelog

- 2026-11-11: Folder created on Reuben's request to build Book 0 out like Book 2. Handover (backwards), contract draft, canon pack first version, mind-sheet "before" notes, storyboard v1, questionnaire and key, cross-book findings.

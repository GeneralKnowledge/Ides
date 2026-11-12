# Book 0

The prequel. It runs from January 49 BC, the morning after the Rubicon, to autumn 47 BC, when Caesar's legions are called *Quirites* on the Field of Mars and promised land with no date. Book 1's prologue (Utica, April 46) follows a few months later.

The series plan, with the through-line and the options for the period, is in [Series plan and Book 0](https://claude.ai/artifact/B1rPPha17L6VAEmSPWJJZq). The method is Book 2's ([book2/README.md](../book2/README.md)): settle the handover, contract, canon, mind sheets and storyboard before any prose; pass a blind voice pilot against Book 1's model scenes; draft each act once at full length; one outside reader per act.

Because Book 0 is written after Books 1 and 2, its handover runs backwards: it lists what the later books have already fixed. Building it found some things in Books 1 and 2 worth settling; those are in [CROSS_BOOK_FINDINGS.md](CROSS_BOOK_FINDINGS.md).

## Where things stand

| Stage | What | Status |
|---|---|---|
| 0 | [Handover from Books 1 and 2](canon/handover.md) (what is already fixed) | First version, checked against Book 1's text |
| 1 | [Contract](CONTRACT.md) | Approved by Reuben, 11 Nov |
| 2 | Canon pack: [chronology](canon/chronology.md), [places](canon/places.md), [names](canon/names.md) | First version; lines marked (check) still to confirm |
| 3 | [Mind sheets](voice/MIND_SHEETS.md) ("before" notes), [storyboard](storyboard/README.md), [questionnaire](storyboard/questionnaire.md) | Storyboard v1 approved with Reuben's six picks, 11 Nov |
| 4 | [Blind voice pilot](pilot/README.md) | PASSED 11 Nov: Book 0 scenes ranked 1st to 3rd of six |
| 5 | Draft by act ([draft/](draft/)) | All four acts drafted 11 Nov: 42 scenes, about 76,700 words; one outside reader per act next |
| 6 | Structure audit, cold read, freeze | Not started |

No prose until the storyboard and the voice pilot pass. (Both passed; the draft is in `draft/act1` to `draft/act4`.)

## Checks

```
python3 tools/book0_storyboard_check.py
python3 tools/export_book0_docx.py [--acts I,II]
python3 tools/book2_names_check.py --names book0/canon/names.md
```

## Changelog

- 2026-11-11: Folder created on Reuben's request to build Book 0 out like Book 2. Handover (backwards), contract draft, canon pack first version, mind-sheet "before" notes, storyboard v1, questionnaire and key, cross-book findings.
- 2026-11-11: Reuben: "Lets go with your recommendations." Contract approved; storyboard choices settled (see storyboard README); Book 2 suggestions and the Labienus name fix passed to the Book 2 thread; pilot and prose wait for Book 2.
- 2026-11-11: Book 2 already drafted, so the voice pilot ran: I-01 Antony, II-04 Laberius, III-10 Brutus, each paired blind with a Book 1 scene of the same person. Packet in project files.
- 2026-11-11: Pilot PASSED (blind ranking B > D > F > E > A > C). Antony continuity note added to the mind sheets; no line edits, per the reader's advice.
- 2026-11-11: Reuben: "Do that" (draft Book 0 to parity with Book 2, with the cast-check additions). All four acts drafted, each with a self-audit and its history checks in the act README. 42 scenes, about 76,700 words against the 90,000 ceiling; Pharsalus at about 66%. Pilot scenes used unchanged as I-01, II-04, III-10. IV-06 moved to August 47 (after Zela). Reading copy built with `tools/export_book0_docx.py`.
- 2026-11-12: First outside reader on the full draft (reader_feedback/2026-11-12_outside_reader_1.md): 20 hit, 5 partial, no misses; asked for a restrained pass. Two explaining lines cut (III-09, IV-02); key rows 23 and 25 corrected; structural notes held for a second reader.

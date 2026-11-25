# Book 1 dramatic revision, 25 Nov 2026

Commissioned by Reuben's own assessment of Book 1 (25 Nov): one bounded editorial revision on the dramatic weak points, not a polish pass. Priorities in his order: P1 opening orientation (Ch 1–6), P1 Ch 26 recruitment, P1 Ch 32 Decimus, P2 selective voice and parenthetical edits (Ch 26, 29, 32, 34); Ch 29 Apollonia as a secondary item, only with restraint. Ledger rows W–Z in `reader_feedback/BOOK1_OPEN_CRITICISMS.md`.

Built on PR #226 (which carries #223, #224 and #225), since none of the four had merged. About 560 words added across the book.

Not touched: Ch 38 (final image and the “which side of the line” sentence), Ch 20–23, the six POVs, structure, scene count.

## Export check

`tools/export_book1_docx.py` strips the `Date / place:` line with the rest of the scene metadata (`META_PREFIXES`), so Reuben is right that the reading copy has no anchors from it. The fix is in the prose; the exporter is unchanged.

## Per chapter

**Ch 1 (1.1, Cassius).** Opened on what he wanted, with the room arriving in the third paragraph. Now: “From the third couch in the host’s dining room, under lamps lit early against the winter dark, Cassius smiled with his teeth…”. The later “third couch” sentence reworded to avoid the repeat.

**Ch 2, Ch 3, Ch 4.1, 4.2, Ch 6.1, 6.2.** Already placed in the opening sentences (the basilica board, the Velabrum oil-seller, the tribunal in the Forum, the rain at Munda, Porcia's atrium, the Domus Publica court, the Tusculum doorway). Left alone.

**Ch 4.3 (Decimus).** Opened “Caesar had kept him half an hour on roads” straight after Marcus Brutus at home, so “him” read as Brutus. Now names Decimus and the room: “standing at the clerks’ table in the room off the portico while the afternoon clients waited outside.”

**Ch 5 (Octavian, Apollonia).** Opened on a remembered line from a boat rail, then a memory of the temple steps; the drill ground arrived in paragraph six. New first sentence: the drill ground under the town wall, the baggage shed (already in the scene), the sea in the distance. Apollonia stands inland of the coast, so the sea is “on a clear day”.

**Ch 6.3 (Hordeonius).** After Cicero at Tusculum, the second sentence now puts the list on his board under the basilica arch.

**Ch 26 (Brutus, Athens).** Escalation, no new recruit.
- The general paragraph on the young men cut to three sentences, ending “Each was easier to give than the one before.”
- Statilius: Brutus offers him the best command left, across the table in front of the others. Statilius puts it down face up and eats his fish: “Give it to the Cicero boy. He wants a horse… If I take that, I came for that.” Brutus folds the appointment under his cup, aware of how it looked. Afterwards Statilius “did not once mention March” (was “that dinner”, which now would be ambiguous).
- Horace: his father's slavery is told to Brutus “as a reason”; that evening two senators' sons ask whether it is true, and Brutus gives them the same composed sentence.
- Hortensius and the last paragraph (“He had disliked it then. He disliked it now, and kept it.”) unchanged. The line runs: Brutus chooses easily, is refused, chooses against objection, and is chosen.

**Ch 29 (secondary item, restrained).**
- 29.3 opens “on the road west across Macedonia”.
- After the sixth day, one new paragraph: the officers argue Gaius's fate at dinner. The Pompeians want chains (Antony has Decimus shut in Mutina, so a brother is worth a legion in bargaining); Vatinius wants a ship to Italy; Marcus Cicero says his father would know and goes red. Brutus says he will decide when he has seen the man, and lies awake composing what he will say and cannot get past the first sentence. The gate scene, the Caesar's-warmth paragraph and Horace on the rampart are unchanged, so the decision now has something to push against. Siege detail unchanged.
- P2: 29.1 untangled the stacked appositives on Dolabella (consul, proconsul, son-in-law) into a second sentence. 29.2 last line cut (“It had not been rehearsed. That was why it had to go.”); the scene stops on Cicero's instruction, which already shows it.

**Ch 32.**
- P1, 32.2 (Decimus): after “The valley changed on its own”, the senior centurion of the recruits, a Mutina man who liked to be told why a thing was the width it was, stops bringing the morning strength return himself and sends his optio. On the third morning Decimus goes down; the centurion answers everything and asks nothing; the extra foot on the north bank is done by evening, exactly, and he does not come up to say so. The summary sentence about the recruits talking in the evenings is cut; the Plancus sequence, the bridge and “He counted them as they went” are unchanged.
- P2, 32.1 (Octavian): the opening sentence (“entered the politics of force”) made plain. The Martian centurion now speaks like a soldier (“Him that fetched Caesar out of his house that morning. And who pays us there?”); the tribune reported, Agrippa's summary given plainly. Agrippa's “They're counting legions. It's progress.” cut; he keeps “That's the letter answered” and “That's the art”. After the vultures, the two “belonged” sentences cut; “He would not correct them” kept. “agenda” replaced (watchlist word). Cornelius, “He had not told Cornelius to say it. He had not told him not to.”, Atia and Octavia, Cicero last, the pay tables: unchanged.

**Ch 34 (P2).**
- Varro's “It is cheaper to take the owner off the books” was a banker's line in an antiquarian's mouth; now “A man doesn’t like to meet the owner of the books he has been standing his cup on.”
- Hordeonius's four maxims on Atticus's kindness cut to two sentences (“Atticus had put kindness on the books… The market in it had closed in April, and he had been on the wrong side.”).

## The name-stripping exercise

Read without names, most lines in Ch 26, 29, 32 and 34 belong to their speakers already: Marcus Cicero's cheek, Statilius's refusals, Amyntas's figures, Cornelius, Atia, Calenus's household. The ones that could have been anyone's were the Martian centurion's and Varro's (both sounded like Hordeonius) and the narrator's closing maxims in 29.2, 32.1 and 34.2. Those were changed; the rest were left.

## Exports

`exports/Ides_Book1_FULL_Ch01-38.docx` regenerated (CI check). A4 and 6x9 copies in project files `exports_2026-11-25_dramatic_revision/`. The print package and EPUB are not rebuilt.

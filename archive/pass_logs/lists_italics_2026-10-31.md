# Book 1: lists and italics inventory

Audit of main @ 39c16c4 (2026-10-31). Covers the reading text exactly as the DOCX exporter sees it: Prologue, Ch 1–36, Historical Note and Cast. Fixes 1–4, 6–8 and the print rebuild (9) were applied on Reuben’s go-ahead, with 5 (*medimni*) taken too; the Ch 35 “evil spirit” note was left as is.

## Proposed fixes

| # | Where | Now | Proposed | Why |
|---|---|---|---|---|
| 1 | Ch 13 | Cicero’s letter to Atticus in quotation marks (“The city is theatrical,” he wrote…) | Italic, no quotation marks | Every other letter extract (Ch 3, 21, 23, 25, 26, 29, 34) is italic |
| 2 | Ch 30 | Hordeonius’s three Pansa explanations are a roman numbered list | Italicise the three entries (keep the list), or fold into one sentence of italic entries | Ledger entries are italic everywhere else; the only list in the narrative |
| 3 | Ch 25 | “Philippics, he called them.” roman in dialogue | *Philippics* | Ch 6 italicises Brutus’s *Cato* in dialogue |
| 4 | Ch 15 | “And the exta, someone said…” | *exta* | Unnaturalised Latin; naturalised words (atrium, fasces, haruspices) stay roman |
| 5 | Ch 29 | “Barley, so many medimni.” | *medimni* (optional) | Foreign unit, not English |
| 6 | Ch 25, Ch 28 | meant *please leave before you become my problem.* / He thought *survive the week … fear.* | Full stop outside the italics | Other lowercase “meant *X*” spans keep the stop roman |
| 7 | Historical Note, sources | “Cassius Dio, books 43–47”; “Cicero’s letters to Atticus and to his friends” | “Cassius Dio, *Roman History*, books 43–47”; “Cicero, *Letters to Atticus* and *Letters to Friends*” | Every other source gives an italic title |
| 8 | DOCX export | Ch 30 list renders as indented, justified prose; Cast names and Historical Note lead-ins lose their bold | Render list items with a hanging indent, bold labels as small caps | Matches what the print interior already does (tools change only, no prose) |
| 9 | Print PDFs | Built 2026-10-25, before PR #186; 59 paragraphs and Ch 11 italics (*Occupied*, *clear*) differ from main | Rebuild print interior and signatures before printing | Stale |

Optional, not italics: Ch 35 has the apparition say “evil spirit”; the Historical Note says “evil genius”.

## Checked and left alone

- Latin and Greek quotations are correct: *laudandum adulescentem, ornandum, tollendum* (Fam. 11.20), *De germanis, non de Gallis, duo triumphant consules* (Velleius 2.67), *kai su, teknon* (Suet. Jul. 82), Iliad 6.429–30 and 1.259, *EID MAR*.
- Titles italic: *Phaedo*, *Cato*, *Iliad*, *Lives*, *Julius*, *Augustus*, *Civil Wars*, *Life of Augustus*, *Philippics* (back matter). Ch 33 “a final Philippic” is a speech, not the title, so roman is right.
- Words-as-words, ledger entries and “meant *X*” spans are italic throughout (Gate 2 rule).
- Forms of address in dialogue (domina, domine, Imperator) stay roman; Ch 34 “hailed them both as *Imperator*” is word-as-word, so italic is right.
- Untagged direct thought is italic, tagged thought (“Now, Cassius thought”) is roman. Consistent.
- The three versions of Cicero’s *laudandum* line (Ch 30, 31 ×2) punctuate differently. Read as deliberate: Cicero’s delivery, then Labeo’s report, then the quoted line.
- Italic density is light (227 spans in about 88,000 words). The longest runs (Ch 14, 15 word lists; Ch 34) are scenes about overheard or translated words.
- No stray asterisks; DOCX `--check` passes and its italics match the manuscript.

## Lists

- Narrative: one list, Ch 30 (item 2 above). No bullets anywhere in Ch 1–36.
- Historical Note: 28 bullets. Cast: 80 bullets. Both read cleanly.

## Every italic span (227)

| # | Chapter | Span |
|---|---|---|
| 1 | Chapter 1 | forgiven |
| 2 | Chapter 1 | forgiven |
| 3 | Chapter 1 | Phaedo |
| 4 | Chapter 2 | Thapsus |
| 5 | Chapter 2 | Utica |
| 6 | Chapter 2 | new-ring |
| 7 | Chapter 2 | Colonies. |
| 8 | Chapter 2 | new-ring: rate held / unpaid |
| 9 | Chapter 2 | Africa: closed enough |
| 10 | Chapter 3 | Why not hear Cicero speak? It has been a long time. The case is decided anyway. Ligarius is a bad man and an enemy. |
| 11 | Chapter 3 | You are safe. You may come home. I have spoken to him myself, and I give you my word that he means it. Thank him. |
| 12 | Chapter 3 | Thank him. |
| 13 | Chapter 3 | Men come nearest to the gods when they give other men their lives. |
| 14 | Chapter 4 | donative dated |
| 15 | Chapter 4 | colony rumour |
| 16 | Chapter 4 | Lucius Junius Brutus, who drove out the last king, and put his own sons to death when they plotted to bring the king back. |
| 17 | Chapter 4 | Gaius Servilius Ahala, on my mother’s side, who killed a man for reaching after a crown. |
| 18 | Chapter 4 | Decimus Brutus, not the other one |
| 19 | Chapter 6 | Praetor urbanus. |
| 20 | Chapter 6 | C. Cassius Longinus, inter peregrinos. |
| 21 | Chapter 6 | Cato |
| 22 | Chapter 6 | dictator perpetuo |
| 23 | Chapter 6 | king |
| 24 | Chapter 6 | forever |
| 25 | Chapter 6 | perpetuo |
| 26 | Chapter 6 | dead calendar |
| 27 | Chapter 6 | Parthia: packing noise |
| 28 | Chapter 6 | offices: closed forward |
| 29 | Chapter 7 | Rex. |
| 30 | Chapter 7 | regnum |
| 31 | Chapter 7 | king |
| 32 | Chapter 7 | temporary |
| 33 | Chapter 7 | regnum |
| 34 | Chapter 7 | market day |
| 35 | Chapter 7 | Casca |
| 36 | Chapter 7 | law’s face |
| 37 | Chapter 7 | temporary |
| 38 | Chapter 8 | debt |
| 39 | Chapter 10 | Suppose a city has fallen under one man. |
| 40 | Chapter 10 | inquiry, political softness, refuse |
| 41 | Chapter 10 | soft hours, storm weather |
| 42 | Chapter 10 | Visellius, A.: doubtful |
| 43 | Chapter 11 | beware |
| 44 | Chapter 11 | Occupied |
| 45 | Chapter 11 | clear |
| 46 | Chapter 12 | stays |
| 47 | Chapter 12 | spare |
| 48 | Chapter 12 | friends |
| 49 | Chapter 12 | friends · spare? · stay / danger · consul? |
| 50 | Chapter 12 | friends |
| 51 | Chapter 12 | consul |
| 52 | Chapter 14 | metal |
| 53 | Chapter 14 | king |
| 54 | Chapter 14 | king |
| 55 | Chapter 14 | domina |
| 56 | Chapter 14 | he will go with this man |
| 57 | Chapter 14 | friends |
| 58 | Chapter 14 | spare |
| 59 | Chapter 14 | stay |
| 60 | Chapter 14 | danger |
| 61 | Chapter 14 | consul |
| 62 | Chapter 15 | blood |
| 63 | Chapter 15 | knives |
| 64 | Chapter 15 | Brutus |
| 65 | Chapter 15 | liberty |
| 66 | Chapter 15 | murder |
| 67 | Chapter 15 | the consul |
| 68 | Chapter 15 | where is the consul |
| 69 | Chapter 16 | you are a little more than we are |
| 70 | Chapter 16 | kai su |
| 71 | Chapter 16 | you too |
| 72 | Chapter 16 | child |
| 73 | Chapter 16 | Antony |
| 74 | Chapter 17 | libertas |
| 75 | Chapter 17 | libertas |
| 76 | Chapter 17 | liberty |
| 77 | Chapter 20 | yet |
| 78 | Chapter 20 | son |
| 79 | Chapter 21 | not yet money / already joke |
| 80 | Chapter 21 | not yet |
| 81 | Chapter 21 | the deed was fair; the result is nothing |
| 82 | Chapter 21 | To the father of his country. |
| 83 | Chapter 21 | O my wonderful Dolabella |
| 84 | Chapter 21 | I call him mine now. Before, believe me, I had my doubts. |
| 85 | Chapter 21 | plan |
| 86 | Chapter 21 | the mistress |
| 87 | Chapter 21 | dead |
| 88 | Chapter 22 | Caesar |
| 89 | Chapter 22 | Gaius Julius Caesar. |
| 90 | Chapter 22 | Octavianus |
| 91 | Chapter 22 | Caesar |
| 92 | Chapter 23 | boy-Caesar rumour: watch veterans |
| 93 | Chapter 23 | Antium soft paper: watch Servilia orbit |
| 94 | Chapter 23 | noise |
| 95 | Chapter 23 | danger |
| 96 | Chapter 23 | spare |
| 97 | Chapter 23 | stay |
| 98 | Chapter 23 | coward |
| 99 | Chapter 23 | I will not sign for the Republic. I don’t believe in it, and you know I don’t, and you were right not to ask me in February. But if there is ever a thing to be done that wants a friend and not a cause, I am the same man you used to argue with, and I am not doing anything else. |
| 100 | Chapter 24 | Caesar |
| 101 | Chapter 24 | eagle refuse / Servilia paper |
| 102 | Chapter 25 | a great many |
| 103 | Chapter 25 | son |
| 104 | Chapter 25 | Gaius Caesar |
| 105 | Chapter 25 | a great many |
| 106 | Chapter 25 | Hector, you are my father now, and my mother, and my brother |
| 107 | Chapter 25 | And my husband, young and strong. |
| 108 | Chapter 25 | please leave before you become my problem. |
| 109 | Chapter 25 | fleeing |
| 110 | Chapter 25 | tax terror |
| 111 | Chapter 25 | necessity |
| 112 | Chapter 25 | Dolabella is still in Italy, borrowing |
| 113 | Chapter 25 | When he comes through I shall feed him and wave. Come and eat my figs on your way to wherever you are going. Bring Brutus. Do not let him bring a book. |
| 114 | Chapter 25 | libertas |
| 115 | Chapter 25 | move |
| 116 | Chapter 25 | libertas |
| 117 | Chapter 26 | my son Marcus |
| 118 | Chapter 26 | The Republic is in your hands |
| 119 | Chapter 26 | I said so in the House, and they did not laugh. |
| 120 | Chapter 26 | GO |
| 121 | Chapter 27 | my father |
| 122 | Chapter 27 | what is owed |
| 123 | Chapter 27 | The shadow learned. |
| 124 | Chapter 27 | Caesar’s too. |
| 125 | Chapter 27 | We didn’t enrol to fight the consul. |
| 126 | Chapter 27 | when |
| 127 | Chapter 27 | yet |
| 128 | Chapter 27 | Yet |
| 129 | Chapter 27 | partial |
| 130 | Chapter 28 | yet |
| 131 | Chapter 28 | at his own cost |
| 132 | Chapter 28 | adoption |
| 133 | Chapter 28 | armies |
| 134 | Chapter 28 | empire |
| 135 | Chapter 28 | survive the week without looking grateful for their fear. |
| 136 | Chapter 29 | hospitality to a passing magistrate |
| 137 | Chapter 29 | Gaius Trebonius |
| 138 | Chapter 29 | my friend |
| 139 | Chapter 29 | friend |
| 140 | Chapter 29 | O my wonderful Dolabella. I call him mine now. |
| 141 | Chapter 30 | this is what the boy paid five hundred for. |
| 142 | Chapter 30 | and Antony paid this one a hundred, and laughed about it. |
| 143 | Chapter 30 | Rumour |
| 144 | Chapter 30 | Pansa: cause open |
| 145 | Chapter 30 | prudence |
| 146 | Chapter 30 | Laudandum adulescentem, |
| 147 | Chapter 30 | Ornandum. Tollendum. |
| 148 | Chapter 30 | Tollere. |
| 149 | Chapter 30 | tollendum |
| 150 | Chapter 30 | tollendum |
| 151 | Chapter 31 | Laudandum adulescentem, |
| 152 | Chapter 31 | ornandum, tollendum. |
| 153 | Chapter 31 | our |
| 154 | Chapter 31 | the Republic’s |
| 155 | Chapter 31 | I can |
| 156 | Chapter 31 | Laudandum adulescentem, ornandum, tollendum. |
| 157 | Chapter 31 | theirs |
| 158 | Chapter 31 | You have nineteen. Count them before anyone else does. |
| 159 | Chapter 31 | If you will not make him consul, this will. |
| 160 | Chapter 31 | his father’s river |
| 161 | Chapter 31 | not yet |
| 162 | Chapter 31 | Laberius |
| 163 | Chapter 31 | consul |
| 164 | Chapter 31 | nineteen |
| 165 | Chapter 32 | acquired: unclean |
| 166 | Chapter 32 | The master has put his own uncle on it. |
| 167 | Chapter 32 | informers the same |
| 168 | Chapter 32 | Fulvia, wife of M. Antonius, hostis: called, per Sosia, in full |
| 169 | Chapter 32 | prudence |
| 170 | Chapter 32 | wages |
| 171 | Chapter 32 | nothing anyone would remember |
| 172 | Chapter 32 | acquired: unclean |
| 173 | Chapter 32 | Calenus’s steward: lent |
| 174 | Chapter 32 | Clean. |
| 175 | Chapter 33 | Let me die in the country I have so often saved. |
| 176 | Chapter 33 | Marcus |
| 177 | Chapter 33 | you |
| 178 | Chapter 33 | De germanis, non de Gallis, duo triumphant consules. |
| 179 | Chapter 33 | De germanis, non de Gallis. |
| 180 | Chapter 33 | No part in the honours. |
| 181 | Chapter 33 | Shame! |
| 182 | Chapter 33 | Hordeonius, at the Janus |
| 183 | Chapter 34 | pay |
| 184 | Chapter 34 | contribute |
| 185 | Chapter 34 | now |
| 186 | Chapter 34 | in due season |
| 187 | Chapter 34 | Decimus: incomplete |
| 188 | Chapter 34 | paid |
| 189 | Chapter 34 | EID MAR |
| 190 | Chapter 34 | EID MAR |
| 191 | Chapter 34 | If Cato could see the ledgers. |
| 192 | Chapter 34 | libertas |
| 193 | Chapter 34 | Not out of anger |
| 194 | Chapter 34 | Out of arithmetic. While he lives, his brother has a reason to come east, and every Antonian in your ranks has a man to look at. |
| 195 | Chapter 34 | For his own safety |
| 196 | Chapter 34 | You are the gentlest man in Rome |
| 197 | Chapter 34 | and it will cost the Republic everything it has left. Do you think he would spare you? |
| 198 | Chapter 34 | Do you think he would spare you? |
| 199 | Chapter 34 | Imperator |
| 200 | Chapter 34 | you |
| 201 | Chapter 34 | I |
| 202 | Chapter 34 | We are not pirates |
| 203 | Chapter 34 | people |
| 204 | Chapter 34 | But listen to me. You are both younger than I am. |
| 205 | Chapter 34 | Iliad |
| 206 | Chapter 34 | GO |
| 207 | Chapter 35 | I am your evil spirit, Brutus. You will see me at Philippi. |
| 208 | Chapter 35 | Then I will see you. |
| 209 | Chapter 35 | Antony’s |
| 210 | Chapter 36 | EID MAR |
| 211 | Chapter 36 | EID MAR |
| 212 | Chapter 36 | EID MAR |
| 213 | Chapter 36 | paid |
| 214 | Chapter 36 | Philippi |
| 215 | Chapter 36 | Calenus’s steward: lent |
| 216 | Chapter 36 | Clean |
| 217 | Chapter 36 | the boy |
| 218 | Chapter 36 | the young Caesar |
| 219 | Chapter 36 | girl |
| 220 | Chapter 36 | you |
| 221 | Historical Note | kai su, teknon |
| 222 | Historical Note | Lives |
| 223 | Historical Note | Julius |
| 224 | Historical Note | Augustus |
| 225 | Historical Note | Civil Wars |
| 226 | Historical Note | Life of Augustus |
| 227 | Historical Note | Philippics |

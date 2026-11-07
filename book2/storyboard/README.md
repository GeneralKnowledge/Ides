# Book 2 storyboard

**Status:** First version, stage 3. Built from the [contract](../CONTRACT.md) and the [canon pack](../canon/). No prose until Reuben has read this and picked fixes.

The source of truth is [`scenes.tsv`](scenes.tsv): one row per scene, with the scenes it depends on. The table below is a reading copy of it. Scene IDs are permanent; chapter numbers are assigned by the exporter at freeze, never here.

```
python3 tools/book2_storyboard_check.py
```

## What the check says

- **67 scenes, about 100,200 words.** Act I has 25,700, Act II 21,400, Act III 30,000 and Act IV 23,100. All four are within 10% of the contract.
- **Cannae starts at 28,100 words, 28% of the book.**
- **No date rewinds, no scenes where nothing changes, and no dependency points forward.**
- **POV share** runs from Silenus at 15,000 words (10 scenes) down to Hanno at 9,100 (7 scenes). No quotas apply; this is only to see the balance.
- **14 POV absences are longer than 15,000 words.** Four are by design: Maharbal fades and Pacuvius ends at Capua's fall (the decisions of 7 November), and Pacuvius only enters at the end of Act I. The rest are listed under the fixes.

## Fixes to pick

| # | Problem | Proposed fix | Recommended |
|---|---|---|---|
| 1 | Fabius is off the page for 22,800 words, from the ox night (I-11) to Rome after Cannae (II-09) | Add a 1,200-word Fabius scene in spring 216: his dictatorship over, he warns Paullus about Varro and about Hannibal (Livy 22.39, to check). Trim I-15 (Varro elected) to 1,200 | Yes |
| 2 | Hanno is off the page for 22,800 words, from early 216 to Mago's rings | Accept. News reaches Carthage late, and his absence is the gap the reader feels | Accept |
| 3 | Scipio is off for 18,700 words between Placentia and the camp before Cannae | Accept. The record is empty for 217 | Accept |
| 4 | Varro is off for 17,200 words between Picenum (215) and the walls (211), and for 16,400 between 210 and the Metaurus news | Accept. Both gaps are years where the record is empty | Accept |
| 5 | Maharbal has a 25,700-word gap between Cannae and Tarentum | Accept. This is the thinning agreed on 7 November | Accept |
| 6 | The Metaurus battle has no POV on the field: it arrives as news to Varro in Etruria, then as the head to Silenus | Keep. The protected beat is the head, not the battle, and no POV can honestly be at the Metaurus | Keep |
| 7 | The invented soldier has no name | Pick at this gate. It must avoid every nomen in the [names list](../canon/names.md) | Choose now |

## The reader questionnaire

Following the method, the questionnaire and its answer key are written from this storyboard once Reuben has picked fixes, so each question tests a scene that will exist.

## Scenes

### Act I. The Crossing

| ID | Date (BC) | POV | Place | Scene | What changes | Reader knows by the end | Words | At | Sources |
|---|---|---|---|---|---|---|---|---|---|
| I-01 | 218-10 | Silenus | Alpine descent; Taurini | The descent from the snow; the army counted; the Taurini's town taken | Silenus starts writing a history he thought would be a triumph | Hannibal brought perhaps 26,000 men out of the mountains; Silenus is with him to write the war; Hannibal is seen only from outside | 2,200 | 0.0k | Pol. 3.54-56, 3.60 |
| I-02 | 218-11 | Scipio | near the Po (Ticinus) | The cavalry fight; the consul wounded; his son rides back for him | Scipio is hailed by his father and learns what Numidian horse can do | The boy is seventeen; Rome's first fight in Italy is lost; a voice says a slave saved the consul | 1,600 | 2.2k | Pol. 10.3; Liv. 21.46 |
| I-03 | 218-12 | Maharbal | Trebia, Carthaginian side | Numidians bait the Romans across the freezing river; Mago waits in the stream bed | Maharbal sees the method that will win every battle | How Hannibal's cavalry and ambush work; the Romans come out unfed | 1,500 | 3.8k | Pol. 3.71-74 |
| I-04 | 218-12 | Soldier | Trebia, Roman ranks; Placentia | Wading the river at dawn; the centre breaks through and walks to Placentia | The soldier survives a defeat by pushing forward | The ranker's view: cold, hunger, the elephants; 10,000 break through | 1,500 | 5.3k | Pol. 3.72-74 |
| I-04b | 218-12 | Scipio | Placentia | The wounded consul and his son hear the Trebia army come in | Scipio sees his father beaten twice and still giving orders | Placentia holds; the Gauls go over to Hannibal | 1,200 | 6.8k | Pol. 3.74-75 (to check) |
| I-05 | 217-03 | Hanno | Carthage | The council hears of the Trebia; Hanno asks what it costs | Hanno sets himself against the celebrating council | Carthage at home: the Barcid faction and Hanno's peace party; news arrives months late | 1,300 | 8.0k | Liv. 21.3, 21.10 (background) |
| I-06 | 217-03 | Varro | Rome | Rome after the Trebia; the people elect Flaminius consul | Varro sees the Assembly's anger is a weapon | Varro is a popular man in a Senate of nobles | 1,300 | 9.3k | invention inside the record |
| I-07 | 217-04 | Silenus | Arno marshes | Four days in floodwater; Hannibal rides the last elephant and loses an eye | Silenus stops writing heroics | The cost of speed; Hannibal is half-blind | 1,400 | 10.6k | Pol. 3.79; Liv. 22.2 (to check) |
| I-08 | 217-06 | Maharbal | Lake Trasimene | The mist; the trap; 6,000 surrender to Maharbal on terms; Hannibal says he had no power to give them | The first crack between Maharbal and Hannibal | Flaminius is dead; Hannibal breaks Maharbal's word | 2,200 | 12.0k | Pol. 3.84-85; Liv. 22.4-6 |
| I-09 | 217-06 | Fabius | Rome | The news in the Forum; mothers at the gate; Fabius named dictator | Fabius gets power and decides not to fight | Fabius's strategy: deny battle and food | 1,600 | 14.2k | Liv. 22.7-8; Pol. 3.87 |
| I-11 | 217-09 | Fabius | Ager Falernus | Hannibal boxed in; the oxen with burning horns; the pass is lost | Fabius is outwitted and still will not fight | Rome mocks Fabius; Hannibal spared his farm | 1,800 | 15.8k | Pol. 3.93-94; Liv. 22.16-17 |
| I-12 | 217-10 | Varro | Rome | Varro speaks for giving Minucius equal command | Varro moves from crowd to policy | The people overrule the dictator | 1,300 | 17.6k | Liv. 22.25-27 |
| I-13 | 217-autumn | Soldier | Gerunium | Minucius's half-army trapped on the hill; Fabius's men come over the ridge | The soldier owes his life to the slow man | Minucius calls Fabius father | 1,400 | 18.9k | Pol. 3.103-105; Liv. 22.28-30 |
| I-14 | 216-01 | Silenus | Hannibal's winter camp, Gerunium | Sosylus and Silenus; the camp tells Hannibal's dream; hunger | Silenus sees the army needs a big win soon | The dream story (Silenus's own); Hannibal must have battle | 1,200 | 20.3k | Cic. Div. 1.49 |
| I-14b | 216-02 | Hanno | Carthage | Trasimene celebrated; the council votes thanks and almost nothing else | Hanno sees the Barcids winning the argument without paying for it | Carthage is rich and stingy; Hanno warns the war will ask for more | 1,200 | 21.5k | invention inside the record |
| I-15 | 216-03 | Varro | Rome | Varro elected consul against the nobles; Paullus his colleague | Varro has the army he asked for | Eight legions; two consuls who disagree | 1,500 | 22.7k | Pol. 3.106; Liv. 22.34-35 (to check) |
| I-10 | 216-04 | Pacuvius | Capua | After the Trebia and Trasimene, Pacuvius locks the Capuan senate in its house and saves it from the mob | Pacuvius owns the senators before Rome needs them | Capua's politics; his Roman marriages; Hannibal is burning the next valley | 1,500 | 24.2k | Liv. 23.2-4 |

### Act II. Cannae

| ID | Date (BC) | POV | Place | Scene | What changes | Reader knows by the end | Words | At | Sources |
|---|---|---|---|---|---|---|---|---|---|
| II-01 | 216-06 | Maharbal | Cannae depot | The horse take the citadel and grain at Cannae at harvest | Maharbal sees the open plain he wants | Where Cannae is; Rome must answer | 1,000 | 25.7k | Pol. 3.107 (to check) |
| II-02 | 216-07 | Scipio | Roman camp on the Aufidus | Tribune Scipio between consuls who command on alternate days | Scipio learns the army has two minds | The alternate-day command; Paullus's doubts | 1,400 | 26.7k | Pol. 3.110 (to check) |
| II-03 | 216-08-02 | Varro | Roman camp, dawn | Varro's day; the red cloak out at dawn; the line forms | Varro commits | The Roman plan: a deep centre to break Hannibal's | 1,400 | 28.1k | Pol. 3.113 (to check) |
| II-04 | 216-08-02 | Soldier | Cannae, the Roman centre | The centre pushes, the crescent gives, the line closes round | The soldier lives inside the encirclement | The shape of the battle from inside; the slaughter | 2,600 | 29.5k | Pol. 3.113-117 (to check) |
| II-05 | 216-08-02 | Maharbal | Cannae, the horse | The Roman horse broken; the Numidians in the rear | Maharbal's arm wins the day | How it was won; Paullus down | 1,500 | 32.1k | Pol. 3.115-116 (to check) |
| II-06 | 216-08-02 | Varro | Road to Venusia | Varro rides off the field with a handful of horse | The consul survives the army | Paullus is dead; Varro chose to live | 1,000 | 33.6k | Pol. 3.116; Liv. 22.49 (to check) |
| II-07 | 216-08-03 | Maharbal | The field, morning | Among the dead; "you know how to win, not how to use a win" | Maharbal is refused | The protected question: why not march on Rome | 1,800 | 34.6k | Liv. 22.51 (to check) |
| II-07b | 216-08-03 | Silenus | The field, evening | The gold rings taken from the dead knights, counted by the measure | Silenus writes the number and does not believe it | The scale of the loss; the rings Mago will carry home | 1,200 | 36.4k | Liv. 23.12 (rings) |
| II-08 | 216-08 | Scipio | Canusium | Busa feeds the survivors; Scipio draws his sword on Metellus's plan to leave Italy | Scipio becomes a leader at nineteen | The army is not finished; Busa | 1,600 | 37.6k | Liv. 22.52-54 (to check) |
| II-08b | 216-08 | Pacuvius | Venusia | Capuan envoys come to the beaten consul at Venusia | Pacuvius judges Rome by Varro and makes up his mind | Capua weighs its choice; Varro asks for help and gets an excuse | 1,200 | 39.2k | Liv. 23.4-6 (to check) |
| II-09 | 216-08 | Fabius | Rome | The city after Cannae: guards on the gates, the Vestals, the burial alive in the Forum Boarium | Fabius holds the city together and is proved right | Rome's fear and its answer | 1,600 | 40.4k | Liv. 22.55-57 (to check) |
| II-10 | 216-09 | Varro | Rome | The Senate refuses to ransom the prisoners; Varro comes home and is thanked | Varro is spared and cannot forgive himself | Rome will not negotiate | 1,500 | 42.0k | Pol. 6.58; Liv. 22.58-61 (to check) |
| II-11 | 216-autumn | Pacuvius | Capua | Capua goes over; Hannibal at dinner; Pacuvius talks his son out of the knife | Pacuvius chooses Hannibal and saves his life | Capua's terms; Decius Magius sent away | 2,000 | 43.5k | Liv. 23.2-10 |
| II-12 | 216-autumn | Hanno | Carthage | Mago's rings poured out in the senate porch; Hanno's reply | Hanno loses the vote and says why | Carthage sends little to Italy | 1,600 | 45.5k | Liv. 23.11-13 |

### Act III. Italy Chooses

| ID | Date (BC) | POV | Place | Scene | What changes | Reader knows by the end | Words | At | Sources |
|---|---|---|---|---|---|---|---|---|---|
| III-01 | 215-spring | Soldier | Sicily | The Cannae men shipped to Sicily in disgrace | The soldier is exiled for surviving | They serve there while the war is in Italy | 1,400 | 47.1k | Liv. 23.25 |
| III-02 | 215 | Fabius | Rome | Consul again; the Oppian law; the women give up their gold | Fabius sees what the war costs at home | The war economy; women's part | 1,200 | 48.5k | Liv. 34.1 |
| III-03 | 215 | Hanno | Carthage | The council sends Mago to Spain, not Italy; Philip of Macedon's treaty | Hanno wins by not losing | Carthage's other wars; Hannibal starved of men | 1,500 | 49.7k | Liv. 23.13, 23.32; Pol. 7.9 |
| III-04 | 215 | Pacuvius | Capua; Nola | Hannibal's winter in Capua; Nola holds out under Marcellus | Pacuvius's bargain starts to cost | Capua is now the front line | 1,600 | 51.2k | Liv. 23.14-18 (to check) |
| III-05 | 215 | Varro | Picenum | Varro raising men in Picenum | Varro works without honour | Rome keeps raising legions | 1,200 | 52.8k | Liv. 23.32 (to check) |
| III-06 | 214 | Silenus | Hannibal's camp, Apulia | Castulo, his wife's city, goes over to Rome; Hannibal's silence | Silenus sees the general's private loss from outside | Spain is slipping | 1,200 | 54.0k | Liv. 24.41 |
| III-07 | 213 | Scipio | Rome | Scipio stands for aedile though under age | Scipio learns the people | His ambition and charm | 1,300 | 55.2k | Liv. 25.2 (to check) |
| III-08 | 213 | Fabius | Suessula | The consul, his son, makes his father dismount | Fabius is proud and old | Rome's discipline | 1,200 | 56.5k | Liv. 24.44 (to check) |
| III-08b | 213 | Silenus | Hannibal's camp near Tarentum | The long wait outside Tarentum; envoys from Macedon that bring nothing | Silenus sees the war turning into waiting | Philip will not come; Hannibal needs a port | 1,200 | 57.7k | Pol. 7.9 (background) |
| III-09 | 213 | Soldier | Syracuse | The siege; Archimedes' engines seen from the ranks | The soldier sees a war of machines | Syracuse went over; Marcellus | 1,900 | 58.9k | Liv. 24.33-34 (to check) |
| III-10 | 212-spring | Soldier | Sicily, winter quarters | The Cannae men send envoys to Marcellus asking to fight | Refused Italy again | Their disgrace is policy | 1,300 | 60.8k | Liv. 25.5-7 |
| III-11 | 212 | Maharbal | Tarentum | Tarentum opened by night; the citadel holds | Maharbal sees a city won and not held | Hannibal's need for ports | 1,500 | 62.1k | Pol. 8.24-34; Liv. 25.7-11 (to check) |
| III-12 | 212-autumn | Soldier | Syracuse | The city falls; a soldier kills an old man drawing in the dust | The soldier hears what happened and is sickened | Archimedes is dead | 1,400 | 63.6k | Liv. 25.31 |
| III-13 | 212 | Hanno | Carthage | The fleet for Syracuse sent too late | Hanno right again and no happier | Carthage cannot hold Sicily | 1,400 | 65.0k | to check |
| III-14 | 211-spring | Pacuvius | Capua, besieged | Capua under siege writes to Hannibal | Pacuvius waits for rescue | Rome has surrounded Capua | 1,700 | 66.4k | Liv. 26.1-6 (to check) |
| III-15 | 211 | Maharbal | Before Rome | Hannibal camps forty stades from Rome; Maharbal looks at the walls | The march he wanted, five years late | Rome does not recall the Capua army | 1,600 | 68.1k | Pol. 9.5-7; Liv. 26.7-11 |
| III-16 | 211 | Fabius | Rome | Hannibal at the gate; the ground he camps on sold at full price | Fabius's patience wins | Rome is not afraid any more | 1,500 | 69.7k | Liv. 26.11 |
| III-16b | 211 | Varro | Rome, the walls | Varro on the walls looking at Hannibal's fires at Pupinia | Varro sees the man he lost to, eight miles off, and is not afraid | Hannibal cannot take Rome and turns back | 1,200 | 71.2k | Liv. 26.9-11 |
| III-17 | 211 | Scipio | Rome | News that his father and uncle are dead in Spain | Scipio decides to go | Spain is nearly lost | 1,300 | 72.4k | Liv. 25.32-36 (to check) |
| III-18 | 211 | Pacuvius | Capua | Capua falls; Vibius Virrius's last dinner; the senators executed | Pacuvius survives his city | What Rome does to cities that leave | 2,200 | 73.7k | Liv. 26.13-16 (to check) |
| III-19 | 211-autumn | Silenus | Hannibal's camp, Bruttium | News that Capua has fallen; the Capuans who come to the camp and are not received | Silenus understands that Italy has watched what happens to Hannibal's friends | Italy's other cities will not follow Capua | 1,200 | 75.9k | invention inside the record |

### Act IV. The Brother

| ID | Date (BC) | POV | Place | Scene | What changes | Reader knows by the end | Words | At | Sources |
|---|---|---|---|---|---|---|---|---|---|
| IV-01 | 210 | Scipio | Rome | Elected to the Spanish command at twenty-four | Scipio has an army | He is young and a private citizen | 1,500 | 77.1k | Liv. 26.18 |
| IV-02 | 210 | Varro | Rome | Varro in the Senate as Scipio is chosen | Varro sees a young noble get what he never did | The war's new men | 1,100 | 78.6k | invention inside the record |
| IV-02b | 210 | Soldier | Sicily | The Cannae men fight on in Sicily; Italy still forbidden | The soldier stops hoping to go home | Sicily is won for Rome by the men it disowned | 1,300 | 79.7k | Liv. 26.1; 26.40 (to check) |
| IV-03 | 209 | Scipio | New Carthage | The march; the lagoon ebbs; Neptune; the city taken | Scipio's first victory | New Carthage, the hostages, Silenus's figure | 2,400 | 81.0k | Pol. 10.9-15; Liv. 26.42-46 |
| IV-04 | 209 | Scipio | New Carthage | The captive girl given back | Scipio performs restraint | Two versions of the story | 900 | 83.4k | Pol. 10.19; Liv. 26.50 |
| IV-05 | 209 | Hanno | Carthage | News of New Carthage | Hanno's fear comes true | The Barcid base is gone | 1,100 | 84.3k | to check |
| IV-06 | 209 | Fabius | Tarentum | The Bruttian commander, the woman and her brother; Tarentum retaken | Fabius wins by patience and a love affair | Hannibal loses his port | 2,100 | 85.4k | Liv. 27.15-16 |
| IV-07 | 209 | Silenus | Hannibal's camp | Tarentum lost; Maharbal no longer at the fire | Silenus counts who is gone | The army is ageing | 1,500 | 87.5k | invention inside the record |
| IV-08 | 208 | Scipio | Baecula | Hasdrubal slips away with money and elephants; the Spaniards hail Scipio king | Scipio refuses a crown and lets Hasdrubal go | Hasdrubal is heading for Italy | 1,700 | 89.0k | Pol. 10.38-40 |
| IV-09 | 208 | Silenus | Near Venusia | Marcellus killed in an ambush | Silenus sees Hannibal honour a dead enemy | Rome's best fighting general is dead | 1,500 | 90.7k | Pol. 10.32; Liv. 27.26-27 |
| IV-10 | 208 | Soldier | Sicily | News that Marcellus is dead | The soldier loses his advocate | Still barred from Italy | 1,200 | 92.2k | invention inside the record |
| IV-11 | 207 | Hanno | Carthage | Word that Hasdrubal has crossed the Alps | Hanno hopes for the first time | The brother is coming | 1,000 | 93.4k | to check |
| IV-12 | 207 | Fabius | Rome | Hasdrubal's letters intercepted; Nero leaves his army and marches north; the Senate waits | Fabius fears a gamble he did not make | The race north | 1,700 | 94.4k | Liv. 27.43-45 (to check) |
| IV-13 | 207 | Varro | Etruria | Varro holding the Etruscans quiet; riders with the news of the Metaurus | The man blamed for Cannae hears the war turn | Hasdrubal dead; Nero heading back | 1,700 | 96.1k | Liv. 27.35, 27.46-50 (to check) |
| IV-14 | 207 | Silenus | Hannibal's camp, Apulia | A head thrown before the outposts | Silenus sees Hannibal recognise the fortune of Carthage | The ending image | 2,400 | 97.8k | Liv. 27.51 (to check) |
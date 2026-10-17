# Relationship Network

Rome is a **multiplex graph**: the same edge can carry love, debt, patronage, and betrayal simultaneously. Avoid single-label factions.

**Edge types:** FAM family · MAR marriage · FRI friendship · PAT patronage · CLI clientage · MIL military loyalty · POL political alliance · FIN financial/debt · RIV rivalry · RES personal resentment · IDE ideological conflict · ENM shared enemy · SEX sexual/romantic connection · INF information channel

**Intensity:** 1 low – 5 defining  
**Certainty:** A/B/C/D

---

## 1. Core kinship & marriage cluster (Servilia–Brutus–Cassius)

```
Servilia
 ├─ mother of → M. Brutus
 ├─ mother of → Junia Tertia ─MAR─ C. Cassius
 ├─ SEX/POL history with → Caesar (B/C intensity)
 └─ influence over → marriage politics of children

Cato (dead)
 └─ father of → Porcia ─MAR─ Brutus
      └─ IDE memory pressure on Brutus (A as cultural fact)
```

| Edge | Types | Int | Cert | Notes |
|------|-------|-----|------|-------|
| Servilia–Caesar | SEX, POL, INF | 4 | B | Long association; political gossip fuel |
| Servilia–Brutus | FAM, PAT | 5 | A | Maternal power |
| Brutus–Cassius | FAM (in-law), POL, MIL | 5 | A | Conspiracy axis; not identical motives |
| Brutus–Porcia | MAR, IDE | 4 | A | Cato’s moral inheritance |
| Cassius–Junia Tertia | MAR | 4 | A | Binds Cassius into Servilia house |

**Narrative tension:** Brutus can love Servilia, honour Cato, accept Caesar’s favours, and kill Caesar — without being “inconsistent” in Roman terms if honour codes collide.

---

## 2. Caesarian command cluster (pre-Ides)

```
Caesar
 ├─ MIL/PAT → Antony
 ├─ MIL/PAT → Lepidus
 ├─ MIL/PAT → Decimus (also FAM-ish trust)
 ├─ MIL/PAT → Trebonius (later betrayal)
 ├─ PAT → Balbus / Oppius (agents)
 ├─ FAM/will → Octavian (latent until published)
 ├─ MAR → Calpurnia
 ├─ SEX/POL → Cleopatra
 └─ PAT → many senators via clemency
```

| Edge | Types | Int | Cert | Notes |
|------|-------|-----|------|-------|
| Caesar–Antony | MIL, POL, FRI? | 5 | A | Trust vs irritation traditions C |
| Caesar–Decimus | MIL, PAT, will | 5 | A | Highest betrayal voltage |
| Caesar–Lepidus | POL, MIL | 4 | A | |
| Caesar–Cleopatra | SEX, POL, FIN (grain) | 4 | A | Roman elite hostility |
| Caesar–Octavian | FAM, PAT | 3→5 | A | Intensity jumps after will |
| Caesar–Cicero | POL, FRI thin | 2 | A | Literary respect ≠ power sharing |
| Caesar–Brutus | PAT, RES?, IDE | 4 | A/B | Clemency binds awkwardly |
| Caesar–Cassius | PAT, RES | 4 | B/C | |

---

## 3. Antonian household & street power

```
Antony ─MAR─ Fulvia
Fulvia ─prior MAR─ Clodius / Curio (street politics inheritance)
Antony ─FAM─ L. Antonius, G. Antonius
Antony ─RIV─ Octavian (from spring 44)
Antony ─RIV/ENM─ Cicero (44–43)
Antony ─later SEX/POL─ Cleopatra
```

| Edge | Types | Int | Cert | Notes |
|------|-------|-----|------|-------|
| Antony–Fulvia | MAR, POL | 5 | A | Political partnership |
| Antony–Cicero | ENM, IDE | 5 | A | Philippics war |
| Antony–Octavian | RIV, POL, MIL | 5 | A | Oscillates alliance/war |
| Antony–veterans | MIL, PAT | 5 | A | Contested with Octavian |
| Antony–Trebonius | POL→trap | 3 | B/C | Ides delay |

---

## 4. Octavian early network (44–42)

```
Atia / Philippus ─FAM counsel─ Octavian
Octavian ─FRI─ Agrippa (rising)
Octavian ─FRI/PAT─ Maecenas (rising)
Octavian ─POL instrumental─ Cicero (43)
Octavian ─MIL─ Caesarian veterans (name as claim)
Octavian ─will rivalry symbolic─ Caesarion (propaganda later)
```

| Edge | Types | Int | Cert | Notes |
|------|-------|-----|------|-------|
| Octavian–Cicero | POL | 3 | A | Temporary; ends in betrayal structure 43 |
| Octavian–Agrippa | FRI, MIL | 3→5 | B early / A later | Plant early, grow |
| Octavian–Antony | see above | 5 | A | |
| Octavian–Lepidus | POL | 3 | A | Junior then discard |

---

## 5. Debt, money, and favour (FIN edges)

| Debtor/Dependent | Creditor/Patron | Cert | Story use |
|------------------|-----------------|------|-----------|
| Many young nobles | Caesar (gifts, loans, clemency) | B | Why gratitude fails |
| Cities in East | Brutus/Cassius exactions 43–42 | A | Hatred under “liberty” |
| Candidates | Moneylenders / *faeneratores* | A pattern | Election pressure pre-war memory |
| Clients | Atticus (equestrian banker-friend) | A | Neutralish information hub |
| Cleopatra’s Egypt | Rome’s grain need | A | Soft power |

**Principle:** Financial dependency does **not** equal political obedience. Caesar’s beneficiaries help kill him (**A** pattern).

---

## 6. Ideological conflict without simple enmity

| Pair | IDE conflict | Concurrent other edges |
|------|----------------|------------------------|
| Cicero–Caesar | Republic vs personal rule | Literary courtesy; survival |
| Brutus–Caesar | Liberty vs order/favour | Patronage |
| Antony–Liberators | Caesarian vengeance vs tyrannicide | Temporary amnesty talks |
| Octavian–Senate elders | Youth with army vs auctoritas | Mutual instrumentality |

---

## 7. Shared enemies (ENM) producing false friendships

| Shared enemy | Temporary partners | Break condition |
|--------------|--------------------|-----------------|
| Antony (43) | Cicero + Octavian | Octavian’s consulship/triumvirate |
| Liberators | Antony + Octavian (42) | Post-Philippi partition |
| Sextus | Various deals | Convenience |

---

## 8. Information-channel relationships (INF)

| Channel | From → To | Reliability | Notes |
|---------|-----------|-------------|-------|
| Tiro / secretaries | Cicero’s circle | High literacy | Letters |
| Balbus–Oppius | Caesar → Senate world | High | Managers |
| Household slaves | Domus → street | Variable | Leak engine |
| Fulvia’s network | Street/collegia memory | Medium-high | Clodian inheritance |
| Military couriers | Armies ↔ Rome | Medium | Capture/forge risk |
| Atticus | Cross-faction friend | High discretion | Rare honest broker |

---

## 9. Multiplex examples (use in scenes)

### Brutus ↔ Caesar
- PAT: offices, favour  
- IDE: hatred of *regnum*  
- FAM pressure: Servilia  
- RES: possible personal (**C**)  
- FRI public performance: warmth  

### Decimus ↔ Caesar
- MIL: years of trust  
- will: secondary heir  
- POL: conspiracy leadership  
- Outward FRI  

### Antony ↔ Octavian (44–43)
- POL alliance against Liberators later  
- RIV over name, money, veterans  
- ENM shared vs Senate manipulation  
- FIN fight over funds  

### Cleopatra ↔ Roman elite
- FIN/grain leverage  
- SEX scandal lens  
- POL need for recognition  
- RES xenophobia  

---

## 10. Graph rules for writers

1. Before writing a private scene, list **all active edge types** between participants.
2. Never reduce a relationship to one adjective (“loyal,” “treacherous”).
3. When an alliance forms, state what **shared enemy** or **shared resource** creates it.
4. When someone “switches,” check which edge broke (FIN? MIL? IDE?) — usually not all at once.
5. Enslaved/freed persons often hold the real INF edges between domus networks — model them.

---

## 11. Open edges to research/expand

- Exact debt figures for Brutus in East (Cicero letters — pull quotations later)
- Antony’s private finances March 44
- Which senators dined with whom in Feb–Mar 44 (mostly D)
- Agrippa’s first attested actions (date-scrub carefully)
- Women of consular houses as INF brokers beyond Servilia/Fulvia/Calpurnia

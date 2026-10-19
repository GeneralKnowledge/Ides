# Em-dash removal log

**Purpose:** Record every place U+2014 was removed from drafts, and sanity-check the replacements.

**Compared:** `12f4591` (pre-purge) → current working tree (purge `aa2d173` + hand polish).

| Artifact | Role |
|----------|------|
| [`em_dash_removal_log.jsonl`](em_dash_removal_log.jsonl) | Machine log: one `site` record per removed em dash + one `line` record per changed line |
| [`_regen_em_dash_removal_log.py`](_regen_em_dash_removal_log.py) | Regenerator |
| [`em_dash_author_voice.md`](em_dash_author_voice.md) | Policy |

## Totals

| Metric | Count |
|--------|------:|
| Em-dash characters removed | **929** |
| Site records (one per dash) | 929 |
| Lines that had ≥1 em dash | 697 |
| Completeness gaps (pre-purge lines with EM not logged) | 0 |
| Hand-polish lines (no EM on before-line) | 0 |

### Replacement kinds (heuristic per site)

| Kind | Count |
|------|------:|
| `comma_or_paren` | 666 |
| `colon` | 134 |
| `comma` | 43 |
| `other` | 36 |
| `ellipsis` | 28 |
| `paren` | 15 |
| `unknown_cap` | 6 |
| `period` | 1 |

### By file

| File | Em dashes removed |
|------|------------------:|
| `drafts/README.md` | 1 |
| `drafts/book1/ch01_clemency_dinner.md` | 16 |
| `drafts/book1/ch02_cato_and_spectacle.md` | 18 |
| `drafts/book1/ch03_debt.md` | 15 |
| `drafts/book1/ch04_munda_and_soft_chains.md` | 39 |
| `drafts/book1/ch05_octavian_edge.md` | 15 |
| `drafts/book1/ch06_perpetuo.md` | 15 |
| `drafts/book1/ch07_lupercalia.md` | 27 |
| `drafts/book1/ch08_recruitment.md` | 28 |
| `drafts/book1/ch09_spare_antony.md` | 19 |
| `drafts/book1/ch10_side1.md` | 28 |
| `drafts/book1/ch11_omens_manufactured.md` | 17 |
| `drafts/book1/ch12_dread_fragment.md` | 33 |
| `drafts/book1/ch13_go.md` | 23 |
| `drafts/book1/ch14_the_house_wakes_wrong.md` | 54 |
| `drafts/book1/ch15_the_litter_and_the_portico.md` | 39 |
| `drafts/book1/ch16_the_curia.md` | 26 |
| `drafts/book1/ch17_capitol_and_amnesty.md` | 55 |
| `drafts/book1/ch18_paper_and_heirs.md` | 29 |
| `drafts/book1/ch19_funeral_and_cinna.md` | 27 |
| `drafts/book1/ch20_smoke_and_distance.md` | 46 |
| `drafts/book1/ch21_letters_and_lanuvium.md` | 32 |
| `drafts/book1/ch22_the_name.md` | 25 |
| `drafts/book1/ch23_prices_and_cowards.md` | 28 |
| `drafts/book1/ch24_antium.md` | 25 |
| `drafts/book1/ch25_philippics_and_ships.md` | 25 |
| `drafts/book1/ch26_provinces_and_shadows.md` | 28 |
| `drafts/book1/ch27_mutina_begins.md` | 18 |
| `drafts/book1/ch28_mutina_field.md` | 20 |
| `drafts/book1/ch29_isolation_and_fasces.md` | 34 |
| `drafts/book1/ch30_lists.md` | 35 |
| `drafts/book1/ch31_cicero.md` | 11 |
| `drafts/book1/ch32_eastern_ledger.md` | 32 |
| `drafts/book1/ch33_philippi_i.md` | 25 |
| `drafts/book1/ch34_philippi_ii_and_hooks.md` | 21 |

## Sanity check

Not automatic defects. Highest-priority review:

### 1. Double punctuation (0)

_None._

### 2. Period that may have replaced an em dash after a lowercase letter (1)

Risk: false sentence break where an apposition should be a comma or parenthesis.

Known acceptable after hand review:
- `drafts/book1/ch13_go.md` GO list: `thickened. Ligarius’s pride…` (new sentence inside Cassius’s speech; keep).

- `drafts/book1/ch13_go.md` L107 **(reviewed: keep)**
  - BEFORE: Cassius’s finger stopped on one blank place in the list he kept only in his head. “Ligarius’s cousin,” he said. “The one who swore he would stand at the door with a message if the Forum thickened[EM]Ligarius’s pride was sup
  - AFTER:  Cassius’s finger stopped on one blank place in the list he kept only in his head. “Ligarius’s cousin,” he said. “The one who swore he would stand at the door with a message if the Forum thickened. Ligarius’s pride was su

### 3. Hand polish after automated purge (0)

_None as separate line records (hand fixes may sit on the same lines as em-replacements)._

## How to read the JSONL

- `type: site` [EM] one removed em dash: `path`, `before_line`, `context` (with `⟦[EM]⟧` marker), `repl_kind`, full before/after line texts.
- `type: line` [EM] whole-line before/after for grep-friendly review.

```bash
python3 archive/reports/_regen_em_dash_removal_log.py
# or
git diff 12f4591 -- drafts/book1 drafts/README.md
```

## Policy

Do not restore U+2014. If a replacement feels wrong, fix with comma / period / colon / parentheses / ellipsis only.

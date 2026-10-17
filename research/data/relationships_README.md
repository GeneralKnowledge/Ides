# Relationships Edge Table

Machine-readable edges: `research/data/relationships.csv`

**Columns:** from · to · edge_types · intensity_1to5 · certainty · notes · active_from · active_to

**Edge type codes:** FAM · MAR · FRI · PAT · CLI · MIL · POL · FIN · DEB · RIV · RES · IDE · ENM · SEX · INF · will · trap · almost · SIDE1

**Rules**
1. Multiple types on one edge are pipe-separated.  
2. Intensity is situational max in the active window — re-score if writing a later act.  
3. Certainty A/B/C/D as elsewhere; fictional edges are **D**.  
4. Before a private scene, filter CSV for both participants and list all active types.  
5. Human-readable discussion remains in `relationships.md`.

**Stage 3 count:** 40 seed edges (core historical + F1–F4 + SIDE-1). Expand freely; do not delete historical A-edges without note in `contradictions.md`.

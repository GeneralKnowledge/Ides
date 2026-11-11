#!/usr/bin/env python3
"""Build the Book 0 blind voice pilot packet (DOCX) and its key into project files. Run from the repo root."""
import re, docx
from docx.shared import Pt
B1='drafts/book1/'
def scene(path, start_marker):
    lines=open(path,encoding='utf-8').read().split('\n')
    i=next(k for k,l in enumerate(lines) if l.startswith(start_marker))
    j=next(k for k in range(i+1,len(lines)) if lines[k].strip()=='---')   # end of header
    k=next(m for m in range(j+1,len(lines)) if lines[m].strip()=='---' or lines[m].startswith('# ') or lines[m].startswith('## '))
    return '\n'.join(lines[j+1:k]).strip()
def pilot(path):
    t=open(path,encoding='utf-8').read()
    return t.split('\n---\n',1)[1].strip()
S={
 'A':('Book 1: Laberius, Ch 4 SC-05 (Munda)', scene(B1+'ch04_munda_and_soft_chains.md','# SC-05')),
 'B':('Book 0 pilot: Brutus, III-10 (Larissa)', pilot('book0/pilot/III-10_larissa.md')),
 'C':('Book 1: Antony, Ch 27 SC-70a (Brundisium, the legions)', scene(B1+'ch27_provinces_and_shadows.md','# SC-70a')),
 'D':('Book 0 pilot: Laberius, II-04 (Ilerda)', pilot('book0/pilot/II-04_between_the_camps.md')),
 'E':('Book 1: Brutus, Ch 6 SC-11b (the first praetorship)', scene(B1+'ch06_perpetuo.md','# SC-11b')),
 'F':('Book 0 pilot: Antony, I-01 (Ariminum)', pilot('book0/pilot/I-01_the_carriage.md')),
}
d=docx.Document()
st=d.styles['Normal']; st.font.name='Georgia'; st.font.size=Pt(11)
d.add_heading('Six scenes: a blind read',0)
d.add_paragraph('Six scenes about three people, in no particular order. Please read them straight through once, then answer the questions at the end from memory. Short answers are fine; "don’t know" is useful.')
def add_par(text):
    p=d.add_paragraph()
    for part in re.split(r'(\*[^*]+\*)',text):
        if part.startswith('*') and part.endswith('*') and len(part)>2:
            p.add_run(part[1:-1]).italic=True
        else:
            p.add_run(part)
for L in 'ABCDEF':
    d.add_page_break(); d.add_heading(f'Scene {L}',1)
    for para in re.split(r'\n\s*\n',S[L][1]):
        para=para.strip()
        if para in ('* * *','· · ·'): d.add_paragraph('· · ·'); continue
        if para: add_par(para.replace('\n',' '))
d.add_page_break(); d.add_heading('Questions',1)
Q=['Rank the six scenes from the one you liked best to the one you liked least.',
'Did any of them feel as if a different writer, or a different book, had written them? Which?',
'Where did the narration tell you something the scene had already shown you? Quote a line if you can.',
'Three people each appear twice. Did each one feel like the same person both times? Which pair felt least alike?',
'Which person felt most particular, and which most like a type?',
'Which ending was weakest?',
'Did any scene seem to know what would happen to these people later?',
'Anything that felt wrong for the period?']
for i,q in enumerate(Q,1): d.add_paragraph(f'{i}. {q}'); d.add_paragraph('')
out='/mnt/project-files/exports_2026-11-11_book0_voice_pilot/'
d.save(out+'Book0_voice_pilot_blind.docx')
with open(out+'KEY_do_not_send.md','w') as f:
    f.write('# Key: Book 0 blind voice pilot (do not send to the reader)\n\n| Scene | Source | Words |\n|---|---|---|\n')
    for L in 'ABCDEF': f.write(f'| {L} | {S[L][0]} | {len(S[L][1].split())} |\n')
    f.write('\nPairs: Laberius A (Book 1) / D (Book 0); Brutus E (Book 1) / B (Book 0); Antony C (Book 1) / F (Book 0).\n\n**Pass:** the Book 0 scenes (B, D, F) are not picked out as a group as the weaker ones in Q1 or Q2, and Q4 does not find a Book 0 scene unlike its Book 1 pair. Q7 should be "no".\n**If they fail:** fix the mind sheets (the "before" notes), not the scenes, and rerun once with fresh scenes.\n\nNew this time: each Book 0 scene is paired with a Book 1 scene of the same person, so Q4 tests whether the younger person reads as the same person. Different Book 1 scenes from the Book 2 pilot (except E, Brutus Ch 6, the contract\'s model scene), so a reader who did that pilot meets mostly fresh Book 1 text.\n')
for L in 'ABCDEF': print(L, len(S[L][1].split()), S[L][1][:60].replace('\n',' '))

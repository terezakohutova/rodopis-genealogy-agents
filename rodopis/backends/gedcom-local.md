# Backend: GEDCOM or local files

Used when `rodopis.config.md` says `backend: gedcom` or `backend: files`. Nothing here needs a browser or a tree platform account. The agents never write into your genealogy program; they hand you verified facts with citations, and you enter them.

Any genealogy program works: Gramps (free and open source), FamilySearch Family Tree, Ancestry, MyHeritage typed in by hand, RootsMagic, Legacy, or paper.

## gedcom: what the lead reads

Export your tree as GEDCOM (`.ged`) and set `gedcom_file` in the config (default `genealogy/tree.ged`). The lead reads it for context: who is in the tree, under which ID, with which dates, places and links. **The `.ged` file is never rewritten by an agent.** A new export replaces it when you have entered new facts.

GEDCOM is plain text, one line per field, `0 @I123@ INDI` starting a person. Do not read a large file whole; Grep it, or use the script that ships with this repo, [gedcom_find.py](../gedcom_find.py) (standard library only). Its core:

```python
import re, sys

def people(path, needle):
    """Print INDI records whose text contains needle (case insensitive)."""
    with open(path, encoding='utf-8-sig', errors='replace') as f:
        record = []
        for line in f:
            if line.startswith('0 '):
                text = ''.join(record)
                if record and ' INDI' in record[0] and needle.lower() in text.lower():
                    print(text)
                record = []
            record.append(line)

people(sys.argv[1], sys.argv[2])
```

`python -I rodopis/gedcom_find.py genealogy/tree.ged "Novak"` prints each matching person with their `NAME`, `BIRT`, `DEAT`, `FAMC` (family as a child) and `FAMS` (family as a spouse) lines. Follow `FAMC` and `FAMS` IDs to the `FAM` records for parents, spouses and children.

The tree ID written into `status.md` is the GEDCOM cross reference, e.g. `@I123@`. It changes when a program re-exports with new numbering; then search by name and dates and update `status.md`.

## files: no tree program

The same workflow without a `.ged`. The person folders in `genealogy/people/` are the tree: `status.md` holds the key facts and relationships, `research/` the evidence. Pending edits still go to `genealogy/pending-tree-edits.md`, so the file can later be typed into any program.

## What the lead writes: `genealogy/pending-tree-edits.md`

Every fact that passed verification against the original goes here immediately, one block per fact, in this fixed form:

```
### <person name> <tree ID> | <event>
- Date: <date as in the record, and normalized>
- Place: <place, house number>
- Details: <occupation literally (today's equivalent), cause of death, names of parents, spouse, witnesses as relevant>
- Citation: <register type> <parish/place>, <archive>, ref. <x>, <ID>, image <n>, p. <p>, entry <e>, URL
- Grade: source original/derivative, information primary/secondary, confidence Proven/Probable
- Crop: genealogy/people/<slug>/crops/<file>
- Research: genealogy/people/<slug>/research/<NN-topic.md>
- Status: to enter
```

Rules for the file:

- Only Proven or Probable facts. Possible, Speculative and unresolved conflicts stay in the research files.
- Corrections of something already in your tree say so in Details: "replaces <old value> (<reason>)". Conflicts keep both values with both sources.
- Relationships get their own block (event "Relationship: child of <father> and <mother>") with the record that proves them.
- Deleting or merging people is never a pending edit. It is a recommendation in `genealogy/tree-status.md`, for you to decide.

## What you do

1. Open `genealogy/pending-tree-edits.md`, enter each block with status "to enter" into your program: event, date, place, citation, and attach the crop as media to the citation.
2. Change the status line to `Status: entered <date>`.
3. From time to time export a fresh GEDCOM over `gedcom_file`, so the lead sees the current tree.

The lead treats a person's checklist point 11 ("everything verified entered in the tree") as done only when all of that person's blocks say "entered". Until then the point is partial (`[~]`), and the auditor names it as a gap for you, not for a member.

## What changes compared to MyHeritage

- No Smart or Record Matches. Matches from other trees can come from you (paste them into `genealogy/people/<slug>/attachments/`) or from `rod-dna` working your DNA exports. They are pointers, never sources.
- No browser for the lead. Records behind a login (FamilySearch images, paid collections) come back from members as "to open" pointers; you open them, save the image into the person's `attachments/` folder, and `rod-matriky` reads and crops it.
- The portrait badge is a file in `genealogy/people/<slug>/portrait/`; you set it as the profile picture in your program.

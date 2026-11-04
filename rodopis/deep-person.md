# One person in depth

Step by step procedure for researching one person to the "fully done" level of [methodology.md](methodology.md#fully-done-checklist). The token thrift rules of the methodology apply throughout.

## Folder of the person

`genealogy/people/<person-slug>/`

- `status.md`: key facts, the fully done checklist, open gaps (template in `rodopis/templates/`)
- `research/NN-topic.md`: one file per member output, numbered on, never overwritten
- `crops/`, `attachments/`: crops of records, scans, photos, archive replies

Optional for a long running person:

- a gap map by life phase (see phase 1)
- a chronological evidence file: year by year, transcript, source, page, URL, crop, confidence
- a queue of what is verified and not yet in the tree (only with the myheritage backend; with gedcom and files this is `genealogy/pending-tree-edits.md`)

## Phases (the order matters)

0. **Preparation (lead, about 10 calls).** Read the card and the immediate family, Grep every earlier mention of the person in the tree status, history and research files (by tree ID and name). Create the folder and `status.md`. Write down what the researcher knows about the person from the family.
1. **Gap map.** Go through the phases of life: birth and family, childhood and school, work, marriage, children, residences year by year, wars and occupation, old age, death and grave. Mark each line D (documented), H (hypothesis or OCR only) or M (missing), with a confidence grade. This map decides what gets searched; without it nothing is searched. `rod-auditor` turns it into gaps for named members.
2. **Members (read only, one per topic, at most 2 at once, about 25 to 40 calls each).** Registers (the whole book, marginal notes included), censuses, address books, press (Kramerius, ANNO), graves and burials and death notices, military service (men), school and employer, places and houses (postcards), objects and photos (clubs, museums), context of the place. Each brief says what exactly to search, what is already negative (do not search again) and the output format (in the member's definition).
3. **Lead reads the results critically.** Check the key find against its source. Separate "a different person" into an exclusion list. Lower the confidence where only the name matches.
4. **Lead enters** (the only writer): events, citations, crops, photos of places. No hypothesis without a source goes into the tree.
5. **Researcher:** questions to the family (concrete, as a list) and archive requests as drafts from `rod-archivy`. Before drafting, check the record is not online. The researcher sends.
6. **Closing the person:** status and history updated, a closing line with what is waiting and for whom; negatives recorded (what was searched and found nothing) so the next run does not repeat them; new techniques written into the backend file.

## What has worked

- Full text press through APIs (Kramerius, national library portals) and ANNO; cemetery registers and grave passports; Holocaust victim databases.
- Garbled names, OCR variants and fuzzy queries; write every query down.
- Record negatives immediately; next time they are not repeated.
- Identity never from the name alone: it needs a second fact (year, place, occupation, family).

## Order of people

Closest to the researcher first, then by how many online sources exist for the place and period. Deceased people only; for living relatives nothing beyond what the researcher provides.

## Budget per person

Gap map about 10 calls, three or four members at about 30 calls each, entering about 25 calls. Never more than `members_at_once` members at the same time. Archive requests at the end, only for what is not online.

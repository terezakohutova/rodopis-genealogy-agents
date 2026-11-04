# Methodology

How Rodopis works a family tree: in what order, what "done" means for one person, and the binding rules for putting a fact into the tree. This file is backend neutral. Where something only applies to MyHeritage, it points to [backends/myheritage.md](backends/myheritage.md); the GEDCOM and files variants are in [backends/gedcom-local.md](backends/gedcom-local.md).

A family tree is a standing project, filled run after run. Never claim the tree is "done" unless every person in it is. Always say exactly where a run stopped, and keep `genealogy/tree-status.md` as the single source of truth about what is left.

## Traversal order

1. Start from the researcher and go **up** (parents, grandparents), then **sideways**, until one whole generation is complete: both parents, all their siblings and the siblings' partners, and their children if they belong to this generation.
2. Only then go one generation further up the main line and again sideways.
3. When a side branch appears on the way (an uncle, say), work **his whole family in depth** (children, grandchildren) until the branch ends. Then return to the main line and continue up and sideways.
4. Continue branch by branch until the whole tree has been walked.

Do not jump to a more interesting looking branch. Do not stop in the middle of a generation without writing down, in `genealogy/tree-status.md`, which people of it are done and which are pending.

**Where the method does not reach:** people born after roughly 1930 are usually not in public registers (registers are released after about 100 years for births, less for deaths). For the parents' generation the main sources are the family itself, matches from other trees and later civil records; registers become useful from the grandparents' generation up.

## Before you add a new person

Search the tree first: the person may already exist as a separate, not yet connected card (a duplicate or a loose fragment). Only add a new person after that search comes back empty. Large, long built trees nearly always contain such fragments.

## What to do for every person

1. **Research.** Registers (parish, Jewish, civil), censuses, military lists, press, cemeteries, address books, local history: everything genealogically relevant for the place and time the person lived. `rodopis/sources-matrix.md` lists the sources per place, period and record type.
2. **Verify the existing card.** Name, dates, places, relationships. Nothing on a card is true just because it is there: trees contain wrong links, swapped dates, contamination from other trees and typos. A missing source is not proof that a fact is right; it is an open question.
3. **Enter what you verified** (rules below).
4. **Matches from other trees and record collections.** Work them for every person: accept a match only when name, dates and place genuinely line up, reject or ignore anything uncertain. On MyHeritage these are Smart Matches and Record Matches, see the backend file.
5. **Loose fragments.** Look for cards and clusters with no path to the researcher (backend tools where available). Handle them only by the two step deletion rule below.

The person is not done when the registers are read. It is done when it passes the checklist below.

## Fully done checklist

Twelve points. A point is done when it is in the tree with a citation and a crop, or a negative is recorded (what was searched, where, which years), or an archive request is prepared or sent. "It is in a research file" is not done: found and not entered is a gap for the lead.

1. Birth or baptism from the original record, with house number.
2. Marriage(s) from the original record, with house number.
3. Death and burial from the original record: cause, place, grave.
4. All available censuses for the country and years the person lived.
5. Press and obituaries: death notices, adverts, clubs, courts.
6. Parents, siblings and children linked in the tree, each relationship with a source.
7. Every house at every address: today's address and position, a photo of today, a period postcard or photo.
8. Workplaces, school, clubs, church or synagogue, cemetery and grave, institutions (hospital, poorhouse, home): then and now.
9. Objects and photos: what can still be found, bought or traced (documents, personal items, photos in collections).
10. Period context of the place in the key years.
11. Everything verified is entered in the tree with a citation and a full-entry crop; occupation literally plus today's equivalent; nothing graded Possible in the tree.
12. Portrait badge by the rules: deceased only; made from a real photo if any exists, a silhouette only without one; new badges only for fully done people. An existing badge is never taken down: missing points become gaps to finish.

Status marks used in `status.md`:

| Mark | Meaning |
|---|---|
| `[x]` | done |
| `[~]` | partial |
| `[n]` | negative recorded (searched, nothing, with what and where) |
| `[d]` | archive request prepared or sent; counts as done, waiting for an answer is not a gap |
| `[?]` | unclear, check against the card |

In doubt the auditor marks a point as missing, never as done.

## Binding rules for entering facts

- **Every fact has a source.** Unsourced facts get verified first; when no source exists, the question goes to the researcher with the evidence (person, what the card says, what the source says, what you ask). Never delete or keep an unsourced fact silently.
- **Facts from the researcher's own family knowledge** may stand without a record. If such a fact contradicts a record, do not overwrite it: ask, and carry on with another person meanwhile.
- **What is not confirmed does not go into the tree**, not even as a note. Possible and Speculative findings, other people's trees without a source and unresolved conflicts stay in the research files.
- **An entry is complete only with all of it:** event, date, place, **house number** (always; write "house number not given" if the record has none), a formal citation (archive, book, reference, image, entry, URL, transcript) and a **crop of the whole entry** attached to the citation. A citation without the image is unfinished.
- **The crop is the whole entry:** all columns, marginal notes, the continuation on the next page, the column header if needed. Cut off crops get replaced.
- **Enter every source you found**, not only the one behind a single correction. Every article, record, crop and link belongs to the card.
- **Occupation literally from the source, then today's equivalent in brackets.** Keep capitals and diacritics consistent across the tree.
- **Historical name variants:** search every surname and first name in German, Latin, Hungarian and phonetic spellings and with OCR errors. A similar surname is the same family only with two more matching facts.
- **Grade every fact** in the citation note: source original or derivative, information primary or secondary, confidence Proven, Probable, Possible or Speculative ([rules.md](rules.md)). An index entry or a record match without the original is Probable at most.
- **Conflicting sources:** keep both values with their sources, flag the conflict in `genealogy/tree-status.md`, choose the main value with a stated reason. A physical source (register, grave, document) beats any number of agreeing online trees, because trees copy each other.
- **Solve open questions yourself where a source can decide them.** Bring to the researcher only what no source can decide, and irreversible steps (deleting, merging, splitting) with a ready recommendation.
- **Deleting fragments takes two steps.** First list the candidates (names, tree IDs, links) in `genealogy/tree-status.md`. Re-check each one on its own profile right before deletion: a sorted list is a pointer, not proof. Then back up every card in full, including the links inside the cluster (who is whose parent or partner) and the attached images. Only then delete, in a later step. A deleted family returns to the tree only with a documented source.
- **Wrong link vs merged identity.** An "older than parent" warning does not always mean one card holds two people. Often both cards are fine and only wrongly linked (typically through an accepted match based on surname alone). A wrong link is fixed by removing the relationship, not by splitting a card; both are structural changes and need the researcher's approval.
- **Same named relatives** cause most contamination: siblings named after a dead sibling, twins, a son named after his father. Before resolving a date conflict, open the person's immediate family; the date may simply belong to the namesake. The error is usually mutual, so check both cards.

## Working matches

- A match is a pointer to another tree or an index, never a source in itself.
- Decide from the anchor: date plus place plus spouse or parents. Same name alone decides nothing.
- Accept only true matches; record rejected ones and why in `genealogy/tree-status.md`.
- Do not import data from other trees wholesale. If another tree cites a register, take the pointer and read the register.
- When many matches agree on a date and a physical source says otherwise, the physical source wins and the conflict goes into the citation.

## "Not in the index" is not "excluded by the source"

Keep three states apart in every note:

- **verified by the source:** the physical record was read and confirms the fact;
- **excluded by the source:** the physical record was read over the whole relevant range and the entry is not there;
- **not found:** either the whole range was not read, or the search ran only in a secondary index that may not cover that place or period at all.

When an index returns nothing, first test whether it covers that record type, place and period at all (a broad search with only place and years). Reading the physical register is the only way to decide the question.

## Run discipline

- **Write progress after every finished unit.** Tick the person or card right away, never in a batch at the end. A crash then costs at most one unfinished card.
- **Update `genealogy/tree-status.md`** at the latest after ten finished cards or at the end of a generation or branch, whichever comes first: finds, open questions, exact resume point.
- **Real stop conditions only:** end of the unit by the traversal order, missing access, a card that cannot be edited, a technical failure, a daily limit of the platform. If a run ends for any other reason, write that sentence literally ("stopping without a stop condition, reason: X") into the report and the status.
- **After a crash,** compare the last ticked card with the last written status entry and fill in the missing finds before going on.
- **Only one person may be half done** at any time. Findings in files do not pile up: research files are material, the work is done when it is in the tree.
- **Do not end a run with a question when the answer can be looked up.** Questions that really need the researcher go into `status.md` under "Questions for the researcher"; continue with another gap.

## Token thrift

Every tool call resends the whole conversation, so long runs get more expensive with each step.

- **Targeted reads.** Start from the person's `status.md`. Never read the tree status, history or research files whole: Grep by tree ID or name, then read a small range. Read each reference file at most once per run.
- **Crops, never whole scans.** A register scan can be 6000 x 4400 pixels. Make a reduced preview with a script, find the entry, crop at full resolution, read only the crop.
- **Screenshot cap:** at most one screenshot per new page or card, never two in a row without navigating. Verify actions and read text with `find`, `read_page` (interactive filter, small `max_chars`) or a zoomed crop. Chain actions with `browser_batch`.
- **Small edits.** Update status files with small targeted edits, never by reading the whole file to write one line.
- **Members, not generalists.** The lead hands each gap to the member whose topic it is, with a brief of a few lines; members know their sources from their definitions. At most `members_at_once` (default 2) at the same time; start the next one as soon as one delivers.

## What research without a browser can and cannot do

Members have no browser. They are good at:

- finding **which** register to open (title, reference, years, URL);
- indexed public databases (JewishGen, Yad Vashem, Holocaust victim databases, archive catalogues, Verlustlisten);
- full text newspapers and books (ANNO, Kramerius), police registrations, cemetery databases, all by name plus year plus region.

They fail at:

- finding a person with a common surname without a known place (registers are scanned images, not text);
- sources behind a login (FamilySearch images, most tree platforms).

So for a branch with no known place, the first step is the lead's: matches and record collections in the tree platform. Members come in once the parish is known.

## Reports to the researcher

Short: who was entered, what, from which source; one or two sentences about the most interesting find (an unexpected relationship, a striking life story, a conflict between sources); what is left and the resume point. Details belong in `status.md` and the tree status, not in the message.

## Outside the tree

- Local history and genealogy groups on social networks: the agent never joins; it opens the group page and tells the researcher.
- Any login the agent does not have: open the login page and tell the researcher. Never accept terms or consent dialogs on the researcher's behalf.

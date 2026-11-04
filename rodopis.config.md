# Rodopis settings

Edit the values after the colons. Every agent reads this file once at the start of a run.

## Tree

- backend: files
  - `myheritage`: genealogy-agent reads and writes your MyHeritage tree through Claude in Chrome (you stay logged in yourself). See `rodopis/backends/myheritage.md`.
  - `gedcom`: genealogy-agent reads your exported GEDCOM file and writes verified facts with citations to `genealogy/pending-tree-edits.md`; you type them into your genealogy program. See `rodopis/backends/gedcom-local.md`.
  - `files`: no tree program; everything lives in `genealogy/`.
- gedcom_file: genealogy/tree.ged
- tree_name: My family tree

## Output

- output_language: English
  - Members transcribe records in the original language and translate into this language.
- researcher_signature:
  - Your name and contact (postal or e-mail) for signing archive letters. Used only in letter drafts by rod-archivy; empty = the letters keep a gap for you to fill.

## Optional integrations (off by default)

- notion_archives: off
  - `on`: rod-archivy keeps the archive register and request log in two Notion databases instead of `genealogy/archives/`. Fill in the database URLs below.
- notion_institutions_db:
- notion_requests_db:
- gmail_drafts: off
  - `on`: rod-archivy saves archive letters as Gmail drafts (never sends). `off`: letters are files in `genealogy/archives/letters/`.
- image_generator: none
  - The image tool rod-portrety writes its prompt for. rod-portrety never generates the image itself: you (or the lead, if you gave it an image tool) run the prompt and hand the result back for finishing. `none` = any tool you like.

## Portrait badge

- portrait_size: 800
- ring_colour: #E8792B
- signature: none
  - Short text drawn small on the badge, e.g. your initials. `none` for no signature.

## Run limits

- members_at_once: 2
  - How many members genealogy-agent runs at the same time. Each member's own cap (about 40 tool calls) is in its definition.

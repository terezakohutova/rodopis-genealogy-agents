# Archive register and request log

rod-archivy creates `genealogy/archives/institutions.md` and `genealogy/archives/requests.md` from this template when they do not exist. One table row per institution and per request. With `notion_archives: on` in `rodopis.config.md`, the same columns are properties of two Notion databases, linked Institution to Requests.

## genealogy/archives/institutions.md

```
# Archives and institutions

| Institution | Type | Holds (fonds, references, years, places) | Does NOT hold (verified, with date) | How to apply | Fees | Contact (verified address, source) | Notes | Checked on |
|---|---|---|---|---|---|---|---|---|
```

- **Type:** state archive, district archive, city archive, registry office, parish office, museum, memorial, other.
- **How to apply:** e-mail / web form (link) / PDF form as attachment / data box / letter. If it is a form, rod-archivy never writes an e-mail there.
- **Does NOT hold:** only negatives confirmed by the institution or its official guide, each with a date. This column prevents asking the wrong place twice.
- **Contact:** only from the institution's official website or its own e-mail, with the source.

## genealogy/archives/requests.md

```
# Archive requests

| # | Institution | Person (slug, tree ID) | What we ask for | Status | Letter or draft | Sent on | Their ref. | Fee and currency | Paid (date) | Result (what came, saved where) | Next step | Deadline |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

- **Status:** draft / form, data prepared / sent / reply received / waiting for payment / paid / done / nothing held.
- **Sent on:** filled in by the researcher (agents never send).
- **Fee:** only as documented by the institution (e-mail, invoice, official fee list).
- **Deadline:** pick-up, payment deadline, statutory reply period, or the date to check again.
- A request with status sent or waiting counts as done for the person's checklist (`[d]`), see `rodopis/rules.md` section 10.

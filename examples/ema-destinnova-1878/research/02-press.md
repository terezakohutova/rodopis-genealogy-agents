# 02 Press and obituaries 1930 (rod-tisk, blind run)

Fresh agent, given only `.claude/agents/rod-tisk.md` from this repo and the brief "[point 5] press and obituaries, January/February 1930". It researched with WebSearch and WebFetch (Kramerius / Czech Digital Library, ANNO), no browser. The harness counted 44 tool calls; the agent's own estimate below says about 34. Output below unedited (it ran longer than the 600-word target). Every pointer here is a tip: the lead opens the page and reads it before anything is entered.

```
PERSON / TASK: Ema Destinnová (born Emilie Pavlína Kittlová), @I1@. Death reports and obituaries, Jan/Feb 1930, Czech and German press: cause of death, funeral, grave, family.

FINDS:
- Death: high blood pressure, a slow bleed into the brain, died 10.10 pm without waking | Český deník, 30.1.1930, p. 2, uuid:c76e0431-5a56-4247-b7f0-25d5c39e37da | [snippet] | Probable (period press, secondary information)
  quote: "trpěla vygokým krevním tlakem. V důsledku toho nastal pozvolný krevní výron do mo%ku" / "zemřela v nocí v 10 hodin 10 minut"
- Stroke after an X-ray visit to a specialist in Č. Budějovice on Tue 28 Jan; died "after 10 pm" | Národní listy, 30.1.1930, p. (1), uuid:691b8c83-435f-11dd-b505-00145e5790ea | [snippet] | Probable
  quote: "byla pak raněna mrtvici a v noci po 10. hod. zemřela"
- First report, ČTK from Jindřichův Hradec 29 Jan | Národní listy, 29.1.1930, p. (1), uuid:691aa20d-435f-11dd-b505-00145e5790ea | [snippet] | Probable
  quote: "Včera odebrala se česká umělkyně Ema Destinnová v"
- Local paper from Stráž: "mozková mrtvice" (stroke), died in the Budějovice hospital; late effects of an illness about 8 years earlier | Ohlas od Nežárky, 31.1.1930, roč. LX, p. 3, uuid:52281f21-6fe8-4a00-a4b6-a255d89756a1 | [snippet] | Probable
  quote: "Raněna mozkovou mrtvicí zesnula v tamnější nemocnici"
- Ill with sclerosis since the previous year (ČTK 30 Jan) | Dělnická rovnost, 31.1.1930, p. 6, uuid:4dc198b0-4e0e-11e5-8851-005056827e51 | [snippet] | Possible
  quote: "stonala již od předešlého roku na sklerosu"
- Coffin laid out on 30 Jan in the chapel of the general hospital in Budweis, then taken to Prague | Prager Presse, 31.1.1930, p. 10, uuid:8851fe10-a365-11e9-9209-005056827e51 | [snippet] | Probable; same in Prager Tagblatt, 31.1.1930, p. 7 (ANNO_ptb19300131) [snippet]
  quote: "wurde heute in der Kapelle des Allgemeinen Krankenhauses aufgebahrt"
- Funeral plan: Mon 3 Feb, lying in state at the Křižovníci church in the morning, at 2 pm from the National Theatre, burial in Slavín at Vyšehrad | Expres, 31.1.1930, p. 4, uuid:92409540-ea9c-11e2-9439-005056825209; Národní osvobození, 31.1.1930, p. 5, uuid:c8b2b0f0-9bd6-11e7-a093-005056825209; Národní listy, 31.1.1930, p. 2, uuid:691bdab6-435f-11dd-b505-00145e5790ea | [snippet] | Probable
  quote: "Destinnová bude pohřbena do Slavínu na Vyšehradě"
- Funeral report: burial in the Slavín tomb, with "a sister, Mrs Freyová, and her husband" mourning (husband's name garbled by OCR); "Odpočívá v levé ..." [text cut off] | Národní listy, 4.2.1930, p. 2, uuid:691dafa6-435f-11dd-b505-00145e5790ea | [snippet] | Probable
  quote: "sestrou pí- Freyovou a jejím chotěm ndp. Joe Halcbachem"
- Mourners led by "a grief-stricken husband and relatives", ministers including Bechyně, a wreath in the name of the President | Čech, 4.2.1930, p. 2, uuid:659400b0-8b7d-11e6-ae94-005056825209 | [snippet] | Probable
  quote: "dlel zdrcený manžel a příbuzní zesnulé"
- Laid in the Slavín tomb | Lidové noviny, 4.2.1930, p. 3, uuid:1559ebe0-8b88-11dc-bc0f-000d606f5dc6 | [snippet] | Probable
  quote: "bylo uloženo к věčnému spánku v hrobě Slavína"
- Childless | Venkov, 4.2.1930, p. 5, uuid:445a3c20-269f-11e8-b8a6-5ef3fc9ae867 | [snippet] | Possible
  quote: "hrob její, ženy bezdětné"
- Austrian press: Neue Freie Presse, 29.1.1930, p. 21 (ANNO_nfp19300129) | [snippet] | Probable
  quote: "Schlaganfall und wenige Stunden"
- More German titles (snippets, nothing new): Prager Presse 30.1 p. 5; Volksfreund 4.2 p. 4 (funeral); Der Tag 4.2 p. 12; Prager Tagblatt 1.2 p. 4 (Prague city council tribute)
- Conflicts in the press:
  - Birth date: "27. února 1878" (Expres 29.1 p. [1]; Pražské noviny 30.1 p. 4; Moravský večerník 30.1 p. [1]) vs 26 Feb (Lidové noviny 29.1 p. [1])
  - Death date: "29. t. m. večer" (Čech 30.1 p. 3) vs Tuesday 28 Jan (the rest)
  - Cause: "srdeční mrtvice" (heart attack; Pražské noviny, Expres, České slovo) vs bleed into the brain (Český deník, Ohlas)
  - Funeral date: "5. února" (Středostavovské zájmy 1.2 p. 2) vs 3 Feb (the rest)
  - Most reports are copies of the same ČTK news-agency report, so they are not independent sources.

EXCLUDED (other person): Dr Jaroslav Brabec (senator, died of a stroke the same night, in the same columns) | different person. "Halfter" hits in ANNO (nfp 9.2 p. 27, gtb 2.2 p. 8) | unrelated people.

SEARCHED, NOTHING:
- Paid death notice (parte): CDK | Halfter/Halftera/Halfterem/Halfterová/Halfterové | 28.1-20.2.1930, 0 hits
- Husband in the German press: ANNO | Halfter | 28.1-20.2.1930, 7 hits, none about her
- ANNO | Wyschehrad | 1-6.2.1930, 0 hits
- Web | parte Destinnová | nothing

LEADS:
- Sister "pí Freyová" and her husband -> rod-matriky/genealogy-agent: check the Kittl siblings
- "Grabschrift der Sängerin. Von Ema Destinnová" (an epitaph written by her), Prager Presse, 1.2.1930, p. 7, uuid:e1282640-a365-11e9-b601-005056825209 -> lead to read
- Newsreel "Funeral of opera singer Ema Destinnová in Prague", Deglův žurnál, 3.2.1930: https://lindat.mff.cuni.cz/repository/items/01e706ef-3825-4381-8265-7891e13fb23c (its description says the coffin left the National Museum Pantheon; the press says Křižovníci / National Theatre)
- Hospital death register, Č. Budějovice 1930 -> rod-matriky (exact time, cause)

TO OPEN FOR THE LEAD (CDK / DNNT; the OCR API gave 403 or 404):
- Národní listy, 4.2.1930, p. 2: full funeral report, position in Slavín ("v levé ..."), next of kin "v čele s její ..."
- Národní listy, 29.1.1930, p. (1)
- Ohlas od Nežárky, 31.1.1930, p. 3
- Český deník, 30.1.1930, p. 2
- Venkov, 4.2.1930, p. 5
- Večer, 30.1.1930, p. [1]
- Annoshow pages: nfp 29.1 p. 21, ptb 31.1 p. 7

HAND OFF:
- rod-matriky: death register of Č. Budějovice and Vyšehrad burial record (Slavín tomb vs her own grave, cause of death)
- rod-lide-kolem: funeral speakers (Dr Pujman for the National Theatre, P. Grollich?) and the official delegations

NOT DONE / LIMIT:
- Volume and issue numbers not taken from the CDK metadata
- Regional South Bohemian press (Jihočeské listy, Budweiser Zeitung) not checked separately
- Arcanum not tried
- About 34 tool calls
```

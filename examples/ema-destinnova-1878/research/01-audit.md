# 01 Audit at the start of the person (rod-auditor, blind run)

Fresh agent, given only `.claude/agents/rod-auditor.md` from this repo and the brief "start-of-person audit against the fully done checklist". Output below unedited.

```
PERSON: Ema Destinnová (born Emilie Kittlová), @I1@   VERDICT: MISSING 12 POINTS
MET: none
GAPS:
  1. [point 1] No birth or baptism from the original. The 26 Feb 1878 Prague date comes from encyclopedias only. -> rod-matriky: find and read the Prague parish baptism register for Emilie Pavlína Kittlová, Feb 1878 (father Emanuel Kittl). Make a whole-entry crop, a literal transcription and a citation with the house number.
  2. [point 2] No marriage from the original. The 1923 marriage to Josef Halfter is from biographies only. -> rod-matriky: locate the 1923 marriage register entry (parish or civil, probably Stráž nad Nežárkou or Prague). Crop, transcribe and cite it with the house number.
  3. [point 3] No death or burial from the original (cause, place, grave). -> rod-matriky: death register České Budějovice, 28 Jan 1930, giving the cause. Burial and grave record at Vyšehrad cemetery, Prague, with the grave number.
  4. [point 4] No census recorded. -> rod-mista: Prague 1880/1890/1900 (Kittl household), plus 1910 and 1921 (Prague or Stráž nad Nežárkou). Record a negative for each year not found. A census scan goes to rod-matriky to read.
  5. [point 5] No press or obituaries. -> rod-tisk: Kramerius/ANNO for parte and obituaries Jan-Feb 1930, the 1923 marriage notice, and wartime press on her confinement at Stráž. Search every name variant (Destinn, Destinnová, Kittlová, Halfter).
  6. [point 6] Parents, siblings and children not linked with a source. Only the father's name is known, from encyclopedias. -> rod-matriky: take the parents from the baptism entry, then the siblings' baptisms in the same parish. If the branch stays unclear, rod-dna.
  7. [point 7] No house at any address documented: no today's address, no photos. -> rod-mista: house numbers of the birth house, the Prague residences, the Stráž nad Nežárkou chateau and the house of death, with today's addresses (RÚIAN). Then rod-fotodetektiv for today's photos and period photos, and rod-veci for period postcards.
  8. [point 8] Workplaces, school, church, cemetery and institutions not documented then and now (e.g. National Theatre, Berlin Court Opera, Metropolitan Opera, the baptism parish, the Vyšehrad grave). -> rod-lide-kolem: teacher Marie Loewe-Destinn, engagements and colleagues. Church, cemetery and grave as places go to rod-mista.
  9. [point 9] No objects-and-photos layer (`research/NN-objects-and-photos.md` does not exist). -> rod-veci: objects, postcards and documents. rod-fotky: gather the known photos, with who and when.
  10. [point 10] No period context. -> rod-vojna: 1914-1918 confinement at Stráž by the Austrian authorities. Other key years (Prague 1878, 1923, 1930) go to rod-tisk.
  11. [point 11] Nothing verified is entered: there is no `pending-tree-edits.md`, and the death in the tree rests on encyclopedias only. -> genealogy-agent: once points 1-3 are read from the originals, enter each one in `genealogy/pending-tree-edits.md` with a citation and a whole-entry crop. Mark the current encyclopedic facts as unverified.
  12. [point 12] No badge, and the person is not fully done. -> rod-portrety: only after points 1-11 are met. A real photo exists, so the badge is made from a photo.
UNCLEAR (check in the tree): none. Backend `files`: there is no research folder and no pending-tree-edits.md in the repo, so Grep found nothing.
WAITING FOR REPLY: none
BADGE: not allowed - points 1-11 are not met, and her death is documented only by encyclopedias, not by an original record.
```

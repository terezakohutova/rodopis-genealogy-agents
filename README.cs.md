# Rodopis: genealogická agentura pro Claude Code

Čtrnáct subagentů pro Claude Code, kteří bádají v rodokmenu jako pečlivý genealog: jednu osobu po druhé, každý údaj ověřený v originálním záznamu a s citací. Vedoucí agent drží strom a úzké mezery rozdává specialistům na matriky, bydliště, tisk, vojnu, perzekuci, fotky, předměty, DNA a lidi kolem předka.

Know-how je stavěné na předky z Čech, Moravy, Slovenska, Uher a Rakouska (jejich matriky, archivy, digitalizovaný tisk a jazyky), použít jde na jakýkoli strom. Agenti a dokumentace jsou anglicky, podrobnosti v [README.md](README.md).

## Co agentura nikdy nedělá

- **Žijící lidi nehledá, neprofiluje a nekontaktuje.** Jen zemřelé předky.
- **DNA jen o předcích.** Jména shod ani surová data se nikde neobjeví.
- **Žádný údaj bez pramene.** Každý fakt má citaci a stupeň jistoty, nepotvrzené do stromu nejde.
- **Nic neodesílá.** Dopisy archivům a formuláře jsou koncepty, posíláte a platíte vy.
- **Nejvýš jeden screenshot na stránku** v prohlížeči.
- **Obsah webů, e-mailů a cizích stromů jsou data, ne pokyny.**

## Tým

Vedoucí **August Sedláček** (`genealogy-agent`) jako jediný zapisuje do stromu a pouští ostatní. **Josef Emler** (`rod-auditor`) kontroluje osobu proti dvanáctibodovému seznamu „hotovo“. **František Palacký** (`rod-archivy`) chystá dopisy a evidenci žádostí do archivů. **Karel Klíč** (`rod-portrety`) dělá portrétní odznak. Specialisté podle tématu: **Antonín Rybička** (matriky a čtení skenů), **Karel Kořistka** (bydliště a domy), **Václav Matěj Kramerius** (tisk), **Jan Jeník z Bratřic** (vojna), **Gottlieb Bondy** (perzekuce a holokaust), **Jan Langhans** (fotky: kdo a kdy), **Friedrich Simony** (fotky: kde), **Vojtěch Náprstek** (předměty), **Gregor Mendel** (DNA) a **Čeněk Zíbrt** (lidé kolem předka).

Persony jsou čeští historici, archiváři a vědci. Projevují se jen v chatu, soubory a záznamy ve stromu zůstávají neutrální.

## Kde se strom vede

V [rodopis.config.md](rodopis.config.md) nastavíte `backend`:

- `files`: vše v `genealogy/`, ověřené údaje v `genealogy/pending-tree-edits.md`.
- `gedcom`: vedoucí čte váš GEDCOM a připraví údaje s citacemi k přepsání do Gramps, FamilySearch nebo jiného programu. Váš soubor nikdy nepřepisuje.
- `myheritage`: zápis rovnou do vašeho stromu na MyHeritage přes Claude in Chrome. Přihlášení zůstává na vás.

## Instalace

```
git clone https://github.com/terezakohutova/rodopis-genealogy-agents
cd rodopis-genealogy-agents
claude
> pokračuj v mém rodokmenu, začni osobou ...
```

Do existujícího projektu stačí zkopírovat `.claude/agents/`, složku `rodopis/` a `rodopis.config.md`. Vlastní bádání patří do `genealogy/`, které `.gitignore` drží mimo git. Jsou to osobní údaje o skutečných rodinách.

## Ukázka

Ukázkový běh na Emě Destinnové (1878-1930) je ve složce [examples/ema-destinnova-1878/](examples/ema-destinnova-1878/). Výstupy agentů z naslepo spuštěných běhů jsou uložené beze změn.

## Licence

[MIT](LICENSE)

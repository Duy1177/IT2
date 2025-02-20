# Undersøkelse: Har fysiske ferdigheter en sammenheng med mer scoring i basketball?

## Introduksjon
Basketball er en stor interesse for meg, og det har lenge vært en oppfatning om at større og sterkere spillere har en fordel. Høyde gir åpenbare fordeler, men har det en direkte sammenheng med hvor mye en spiller scorer? 

For å undersøke dette har jeg analysert poeng per kamp (**points per game, PPG**) for rookies i NBA. Ved å kun se på rookies får vi et datasett der alle spillerne starter fra samme nivå, og variasjoner i erfaring blir mindre relevante. 

## Mål
Målet med denne analysen er å finne ut om det er en direkte sammenheng mellom spillerens høyde og hvor mange poeng de scorer i gjennomsnitt per kamp.

## Datasett
Det var utfordrende å finne et datasett som inneholdt både statistikk fra kamper og fysiske attributter. Derfor ble to forskjellige datasett kombinert (pandas var veldig hjelpsom her):

- **Rookie-statistikk:** Hentet fra [Basketball Reference](https://www.basketball-reference.com/leagues/NBA_2025_rookies.html) – inneholder poeng per kamp og annen statistikk.
- **Fysiske attributter:** Hentet fra [NBA Combine Stats](https://www.nba.com/stats/draft/combine-anthro?sort=HEIGHT_WO_SHOES&dir=1&SeasonYear=2024) – inneholder høyde (uten sko), vekt og andre fysiske data.

Disse datasettene ble kombinert ved å matche spillerens navn i begge tabellene.

## Krav for å kjøre koden
For å kjøre koden, må følgende Python-biblioteker være installert:

```bash
pip install pandas 

pip install matplotlib

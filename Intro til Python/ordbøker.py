# Lag en ordbok der nøklene er land og verdiene er antall innbyggere. 
# Legg inn informasjon om de fem landene med flest innbyggere i verden.
land_innbyggere = {
    "Kina": 1_411_778_724,    # estimat per 2024
    "India": 1_403_600_000,   # estimat per 2024
    "USA": 335_000_000,       # estimat per 2024
    "Indonesia": 277_000_000, # estimat per 2024
    "Pakistan": 241_500_000   # estimat per 2024
}
 
# Skriv ut en oversikt med navnene til alle landene ved hjelp av en løkke.
for i in land_innbyggere.keys():
    print("Land:", i)
# Skriv ut en oversikt med bare innbyggertallene til alle landene.
for i in land_innbyggere.values():
    print("Innbyggere:", i)
 
# Skriv ut en tekst om hvert land på formen: «X har Y innbyggere».
for noekkel, verdi in land_innbyggere.items():
     print(f"Land:{noekkel}, innbyggere:{verdi}")
     
# Bruk sorted() for å skrive ut lista i oppgave b med landenes navn i alfabetisk rekkefølge. (Hint: sorted(land.keys()))
sortert = sorted(land_innbyggere.keys())
print(f"Test: {sortert}")


# Gå gjennom alle landene og avslutt med en tekst på formen: «X har flest innbyggere. Y har færrest innbyggere.»
flestInnbyggere = max(land_innbyggere, key=land_innbyggere.get)
minstInnbyggere = min(land_innbyggere, key=land_innbyggere.get)

print(f"{flestInnbyggere} har flest innbygger og {minstInnbyggere} har minst innbyggere")


# Ta utgangspunkt i eksemplet ovenfor i disse oppgavene.
sommer_ol = [
  { "årstall": 2004, "vinnertider": { "100 m": 10.93, "200 m": 22.06, "400 m": 49.41 } },
  { "årstall": 2008, "vinnertider": { "100 m": 10.78, "200 m": 21.74, "400 m": 49.62 } },
  { "årstall": 2012, "vinnertider": { "100 m": 10.75, "200 m": 21.88, "400 m": 49.55 } },
  { "årstall": 2016, "vinnertider": { "100 m": 10.71, "200 m": 21.78, "400 m": 49.44 } },
  { "årstall": 2020, "vinnertider": { "100 m": 10.61, "200 m": 21.53, "400 m": 48.36 } }
]


# Skriv ut vinnertiden på 200 m for hvert av årstallene.
for ol in sommer_ol:
    år = ol["årstall"]
    tid200 = ol["vinnertider"]["200 m"]
    print(f"I år {år} er vinner tiden for 200m {tid200}")


# Skriv ut vinnertiden på 400 m for hvert av årstallene.'
for ol in sommer_ol:
    år = ol["årstall"]
    tid400 = ol["vinnertider"]["400 m"]
    print(f"I år {år} er vinner tiden for 400m {tid400}")


# Skriv ut vinnertidene fra OL i 2020.
print(f"Vinnertidene i 2020 er {sommer_ol[4]["vinnertider"]}")


# Skriv ut den dårligste og den beste vinnertiden på 200 m.
tid200m = [ol["vinnertider"]["200 m"] for ol in sommer_ol] 
beste = max(tid200m)
dårligste = min(tid200m)

print(f"Dårligste tiden i 200 m: {dårligste}, Beste tiden i 200 m: {beste}")


# Lag en datastruktur som samler dataene som i tabellen ovenfor.
nySommer_ol= [
    {"100m": {"2004": 10.93, "2008": 10.78, "2012": 10.75, "2016": 10.71, "2020": 10.61}},
    {"200m": {"2004": 22.06, "2008": 21.74, "2012": 21.88, "2016": 21.78, "2020": 21.53}},
    {"400m": {"2004": 49.41, "2008": 49.62, "2012": 49.55, "2016": 49.44, "2020": 48.36}}
]

# Skriv ut vinnertiden på 400 m for hvert av årstallene.
if "400m" in nySommer_ol[2]:
    vinnertider_400m = nySommer_ol[2]["400m"]
    print(f"Vinnertidene for 400 m er {vinnertider_400m}")
    
# Skriv ut vinnertidene fra OL i 2020.
for ol in nySommer_ol:
    for distanse, tid in ol.items():
        print(f"Vinner tiden for {distanse} var {tid["2020"]} sekunder")
        

# Skriv ut den dårligste og den beste vinnertiden på 200 m.
tider200m = None

for distanse in nySommer_ol:
    if "200m" in distanse:
        tider200m = distanse["200m"]
        
beste200m = min(tider200m.values())
dårligste200m = max(tider200m.values())

print(f"Beste tiden i 200m er {beste200m} og dårligste tiden {dårligste200m}")

# Hvilke av de to datastrukturene vil du foretrekke for å løse oppgavene a og b ovenfor?
#Ville brukt den første siden det var mye enklere.

ordbok = {
  "a": [2, 4, 6],
  "b": [1, 3, 5],
  "c": [1, 2, 3],
  "d": [4, 5, 6],
  "e": [7, 8, 9]
}

for i in ordbok.items():
    print(i)
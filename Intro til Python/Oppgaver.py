# # Grunnleggande oppgåve: Lag eit system som handterer innlogging. 
# # Ha eit fokus på korleis du kan sjekke kriterier på best måte (kva er "best"?). 
# # Brukaren må skrive inn brukarnavn og passord, og skal få tydelege feilmeldingar.

# #Mitt forsøk
# # brukerNavn = "Bruker1"
# # passord = "Passord1"

# # logInNavn = input("Brukernavn: ")
# # logInPass = input("Passord: ")

# # if logInNavn != brukerNavn:
# #     print("Brukernavn eller passorder feil")
# # elif logInPass != passord:
# #     print("Brukernavn eller passord er feil")
# # else: print("Du har logget inn!")

# #Fasit
# # innlogga = False

# # brukarnavnFraaDatabase = "Brukar01"
# # passordFraaDatabase = "Passord01"

# # while not innlogga:
# #     # Brukarnavn
# #     brukarnavn = input("Ditt brukarnavn: \n")
# #     if brukarnavn != brukarnavnFraaDatabase:
# #         print("Brukaren eksisterer ikkje.")
# #         break

# #     # Passord
# #     passord = input("Ditt passord: \n")
# #     if passord != passordFraaDatabase:
# #         print("Feil passord.")
# #         break

# #     innlogga = True

# # Oppgåve: Gjennomfør 500 000 stein, saks, papir og tel kor mange gonger dei ulike vala dukkar opp.
# # import random

# # stein = 0
# # saks = 0
# # papir = 0

# # for go in range(500000):
# #     resultat = random.choice(["stein","saks","papir"])
# #     if resultat == "stein":
# #         stein = stein + 1
# #     elif resultat == "saks":
# #         saks = saks + 1
# #     else: papir = papir + 1
    
# # print(f"Stein: {stein}, saks: {saks}, papir: {papir}")
# # print(stein + papir + saks)

# # Oppgåve: Ta utgangspunkt i eksempelet frå boka, som sjekkar om du har skrive inn eit tal (heiltal vha. try-except), 
# # og skriv eigen kode som sjekkar om det er eit positivt tal i tillegg. 
# # Bonus: Gje ein kontrollert tilbakemelding dersom brukaren avbryt programmet med ctrl+c.

# # gyldig = False

# # try:
# #     while not gyldig: #Så lenge den ikke er gyldig kjører koden helt til et gyldig tall skrives
# #         tall = input("Skriv et positivt tall: ")
# #         try:
# #             tall = int(tall)
# #             if tall > 0:
# #                 gyldig = True
# #             else:
# #                 print("Skriv inn et positivt tall")
# #         except ValueError:
# #             print("Du må skrive inn et heltall.")
# # except KeyboardInterrupt:
# #     print("Avbrutt av bruker")


# # Oppgåve: Samanlikn nokre ulike måtar å gjere ting på i eit av dine tidlegare program. 
# # Eksempelvis match-case vs. if-elif-else.
# # import timeit

# # # Versjon 1 (uten input)
# # def versjon1_test(tall):
# #     if tall > 100:
# #         return "Tallet er større enn 100"
# #     elif 0 < tall < 100:
# #         return "Tallet er mindre enn 100"
# #     elif -100 < tall < 0:
# #         return "Tallet er større enn -100"
# #     elif tall < -100:
# #         return "Tallet er mindre enn -100"
# #     else:
# #         return "Tallet er 0"

# # # Versjon 2 (uten input)
# # def versjon2_test(tall):
# #     match tall:
# #         case _ if tall > 100:
# #             return "Tallet er større enn 100"
# #         case _ if 0 < tall < 100:
# #             return "Tallet er mindre enn 100"
# #         case _ if -100 < tall < 0:
# #             return "Tallet er større enn -100"
# #         case _ if tall < -100:
# #             return "Tallet er mindre enn -100"
# #         case _:
# #             return "Tallet er 0"

# # # Testtall
# # tall = 50

# # # Tidtaking
# # tid1 = timeit.timeit(lambda: versjon1_test(tall), number=1000)
# # tid2 = timeit.timeit(lambda: versjon2_test(tall), number=1000)

# # print(f"Versjon1 sin tid {tid1}")
# # print(f"Versjon2 sin tid {tid2}")

# #Oppgåve: Klokke
# #Bruk time-biblioteket og løkker for å lage eit program fungerer som ei slags stoppeklokke."
# # import time

# # timer = 0
# # minutter = 0
# # sekunder = 0

# # try: 
# #     while True:
# #         sekunder = sekunder + 1
# #         if sekunder == 60:
# #             sekunder = 0 
# #             minutter = minutter + 1
# #         if minutter == 60:
# #             minutter = 0
# #             timer = timer + 1
        
# #         print(f"{timer}, {minutter}, {sekunder}")
# #         time.sleep(1)
        
# # except KeyboardInterrupt:
# #     print("Tiden ble stopet")


# eliteserielag = [
#   { "lag": "Lillestrøm", "seriemesterskap": [1976, 1977, 1986, 1989], "norgesmesterskap": [1977, 1978, 1981, 1985, 2007, 2017] },
#   { "lag": "Molde", "seriemesterskap": [2011, 2012, 2014, 2019], "norgesmesterskap": [1994, 2005, 2013, 2014, 2021] },
#   { "lag": "Viking", "seriemesterskap": [1972, 1973, 1974, 1975, 1979, 1982, 1991], "norgesmesterskap": [1979, 1989, 2001, 2019] },
#   { "lag": "Strømsgodset", "seriemesterskap": [1970, 2013], "norgesmesterskap": [1969, 1970, 1973, 1991, 2010] },
#   { "lag": "Aalesund", "seriemesterskap": [], "norgesmesterskap": [2009, 2011] },
#   { "lag": "Rosenborg", "seriemesterskap": [1967, 1969, 1971, 1985, 1988, 1990, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2009, 2010, 2015, 2016, 2017, 2018], "norgesmesterskap": [1964, 1971, 1988, 1990, 1992, 1995, 1999, 2003, 2015, 2016, 2018] },
#   { "lag": "Sarpsborg", "seriemesterskap": [], "norgesmesterskap": [] },
#   { "lag": "Bodø/Glimt", "seriemesterskap": [2020, 2021], "norgesmesterskap": [1975, 1993] },
#   { "lag": "Odd", "seriemesterskap": [], "norgesmesterskap": [2000] },
#   { "lag": "Tromsø", "seriemesterskap": [], "norgesmesterskap": [1986, 1996] },
#   { "lag": "Vålerenga", "seriemesterskap": [1965, 1981, 1983, 1984, 2005], "norgesmesterskap": [1980, 1997, 2002, 2008] },
#   { "lag": "HamKam", "seriemesterskap": [], "norgesmesterskap": [] },
#   { "lag": "Sandefjord", "seriemesterskap": [], "norgesmesterskap": [] },
#   { "lag": "Haugesund", "seriemesterskap": [], "norgesmesterskap": [] },
#   { "lag": "Jerv", "seriemesterskap": [], "norgesmesterskap": [] },
#   { "lag": "Kristiansund", "seriemesterskap": [], "norgesmesterskap": [] }
# ]

# #Bruk datasettet ovenfor og skriv ut


# # en oversikt over lagene som har vunnet minst ett seriemesterskap
# # for i in range(len(eliteserielag)):
# #     if eliteserielag[i]["seriemesterskap"] == []:
# #         print(None)
# #     else:
# #         print(f"{eliteserielag[i]["lag"]} har vunnet minst en gang")
    
# # en oversikt over lagene som har vunnet minst ett norgesmesterskap
# # for i in range(len(eliteserielag)):
# #     if eliteserielag[i]["norgesmesterskap"] == []:
# #         continue
# #     else:
# #         print(f"{eliteserielag[i]["lag"]} har vunnet norgesmesterskap minst en gang")

# # en oversikt over lagene som har vunnet minst ett seriemesterskap og ett norgesmesterskap
# # serieOgNorge = []

# # for lag in eliteserielag:
# #     if len(lag["seriemesterskap"]) and len(lag["norgesmesterskap"]) > 0:
# #         serieOgNorge.append(lag["lag"])

# # print(serieOgNorge)

# # laget som har vunnet serien flest ganger
# # flestGanger = 0

# # for lag in eliteserielag:
# #     if len(lag["seriemesterskap"]) > flestGanger:
# #         flestGanger = len(lag["seriemesterskap"])
# #         besteLag = lag["lag"]
        
# # print(f"{besteLag} har vunnet {flestGanger}")

# # laget som har vunnet norgesmesterskapet flest ganger
# # flestGanger = 0

# # for lag in eliteserielag:
# #     if len(lag["norgesmesterskap"]) > flestGanger:
# #         flestGanger = len(lag["norgesmesterskap"])
# #         besteLag = lag["lag"]
        
# # print(f"{besteLag} har vunnet norgesmesterskap {flestGanger}")

# # laget som vant serien første gang
# tidligste = float("inf")
# besteLag = ""

# for lag in eliteserielag:
#     if len(lag["seriemesterskap"]) > 0 and min(lag["seriemesterskap"]) < tidligste:
#         tidligste = min(lag["seriemesterskap"])
#         besteLag = lag["lag"]

# print(f"{besteLag} og {tidligste}")


# # laget som vant serien sist
# tidligste = 0
# besteLag = ""

# for lag in eliteserielag:
#     if len(lag["seriemesterskap"]) > 0 and max(lag["seriemesterskap"]) > tidligste:
#         tidligste = max(lag["seriemesterskap"])
#         besteLag = lag["lag"]

# print(f"{besteLag} og {tidligste}")


# Datakolleksjonar

# A: Lister og ordbøker (dictionaries)

# Lag ei ordbok som representerer eit lager med produkt. 
# Kvart produkt har eigenskapar/attributt som du kan sjå nærare spesifisert under. 
# Nokre produkt kan ha fleire variantar lagra i ordboka
# – eksempelvis fargar. Nokre produkt kan ha fleire ulike tekniske eigenskapar.

# produkt = {
#   "asus zenbook gh215": {"varenavn": "Asus laptop",
#                          "pris": 9999,
#                          "varelager": 10,
#                          "produktinfo": "En bærbar PC med 15.6 tommer skjerm, 8 GB RAM og 256 GB SSD",
#                          "Tekniske egenskaper":
#                            {
#                            "prosessor": "Intel Core i5-1135G7",
#                            "grafikkort": "Intel Iris Xe Graphics",
#                            "batterikapasitet": "Opptill 8 timer",
#                            "vekt": "1.8 kg"
#                          },
#                          "farger": ["grå", "svart", "blå"]},
#   "samsung galaxy s22 gh67":{"varenavn": "Samsun mobiltelefon",
#                              "pris": 6999,
#                              "varelager": 20,
#                              "produktinfo": "En smarttelefon med 6.7 tommer skjerm, 128 GB lagring og 12 MP kamera",
#                              "Tekniske egenskaper":{
#                                "prosessor": "Qualcomm Snapdragon 888",
#                                "grafikkort": "Adreno 660",
#                                "batterikapasitet": "4500 mAh",
#                                "vekt": "200 g"
#                              },
#                              "farger": ["svart", "hvit", "grønn"]
                            
#   },
#   "apple airpods pro gen 3 (2023)": {"varenavn": "Trådløse hodetelefoner",
#                                      "pris": 2499,
#                                      "varelager": 30,
#                                      "produktinfo": "Trådløse hodetelefoner med aktiv støydemping",
#                                      "Tekniske egenskaper": {
#                                        "batterikapasitet": "Opptil 4.5 timer",
#                                        "vekt": "5.4 g"
#                                      },
#                                      "farger": ["hvit", "grå", "spygrønn"]
#   }
# } 

# userInput = str(input("Skriv inn en vare: ").lower())

# def nyPris(vareId, nypris):
#   if vareId in produkt:
#     produkt[vareId]["pris"] = int(nypris)

# def taVare(vareId):
#     if vareId in produkt:
      
#         print(produkt[vareId])
#     else:
#         print("Varen finnes ikke.")
        
# # Test av funksjonene
# taVare(userInput)  # Skriv ut opprinnelig informasjon om varen

# nypris = input("Skriv inn ny pris for varen: ")
# nyPris(userInput, nypris)  # Oppdater prisen på varen


# taVare(userInput) # Skriv ut oppdatert informasjon om varen


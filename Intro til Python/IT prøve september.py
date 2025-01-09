#Oppgave 1

import random
# forbudtOrd = ["fis", "bæsj", "tis", "rompe"] #Forbudte ord
# tegn = "!#¤%&/(" #Tegnene den ordet skal erstattes med

# def nyOrd(ny): #Legge til nye fy-ord
#     forbudtOrd.append(ny)
    
# def fjernOrd(ordet): #Fjerne eksisterende fy-ord
#      if ordet in forbudtOrd:
#         forbudtOrd.remove(ordet)
    

# def forbudt(string): #Funksjonen sjekker om et forbudt ord er i setningen og bytter den ut med tegn.
#     for ord in forbudtOrd:
#         if ord in string.lower():                             
#             string = string.lower().replace(ord, random.choice(tegn) * len(ord)) 
    
#     return string


# text = "Den som fisen først er var, den er fisens rette far"
# resultat = ' '.join([forbudt(i) for i in text.split()])             
# print(resultat)

#Oppgave 2
land = {
    "Norge": {"hovedstad": "Oslo", "innbyggere": 5_457_000, "naboland": ["sverige", "finnland","russland"]},
    "Sverige": {"hovedstad": "Stockholm", "innbyggere": 10_490_000, "naboland": ["norge", "finnland"]},
    "Malaysia": {"hovedstad": "Kuala Lumpur", "innbyggere": 33_940_000, "naboland": ["thailand", "vietnam","singapore","indonesia"]},
    "Canada": {"hovedstad": "Ottowa", "innbyggere": 38_930_000, "naboland": ["usa", "russland"]}
}

def spørsmål():
    print("Vi er inne i spørsmålsfunksjonen.")
    
    spørsmålsTyper = ["hovedstad", "innbyggere", "naboland"]
    
    poeng = 0
    feilSvar = []
    
    for _ in range(3):
        landet = random.choice(list(land.keys()))
        
        attribute = random.choice(spørsmålsTyper)
        spørsmålsTyper.remove(attribute)
    
        print(f"Attribute = {attribute}")
        
        svar = land[landet][attribute]
        
        print(f"Hva er {attribute} til {landet}?")
        brukerSvar = input()

        if attribute == "innbyggere":
            gyldig = False
            while not gyldig:
                brukerSvar = input("Skriv inn et tall:")
                try:
                    brukerSvar = int(brukerSvar)
                    gyldig = True
                except ValueError:
                    print("Skriv inn et tall")
            if brukerSvar == svar:
                print("Du er jammen god med tall!")
                poeng += 1
            elif brukerSvar <= land[landet]["innbyggere"] * 1.1 and brukerSvar >= land[landet]["innbyggere"] * 0.9:        
                print("Riktig svar!")
                poeng += 1
            else:
                print("Feil svar")
                feilSvar.append(attribute)
        elif attribute == "hovedstad":
            if brukerSvar.lower() == svar.lower():
                print("Riktig svar!")
                poeng += 1
            else: 
                print("Feil svar")
                feilSvar.append(attribute)
        elif attribute == "naboland":
            brukerSvarListe = [land.strip().lower() for land in brukerSvar.split(", ")]
            riktigListe = [land.lower() for land in svar]
            
            riktige_svar = len(set(brukerSvarListe) & set(riktigListe))

            
            print(f"Brukerens svar: {brukerSvarListe}")
            print(f"Riktig svar: {riktigListe}")
            print(f"Riktige svar: {riktige_svar}")
            
            antallNaboland = len(riktigListe)
            
            if antallNaboland == 1 and riktige_svar == 1:
                print("riktig")
                poeng += 1
            elif antallNaboland == 2 and riktige_svar == 2:
                print("riktig")
                poeng += 1
            elif antallNaboland == 3 and riktige_svar >= 2:
                print("riktig")
                poeng += 1
            elif antallNaboland == 4 and riktige_svar >= 3:
                print("riktig")
                poeng += 1
            else: 
                print(f"Feil, riktig svar var {', '.join(svar)}")
                feilSvar.append(attribute)

    
    print(f"Du fikk {poeng}/3 riktige svar. Du fikk feil på {", ".join(feilSvar)}")            
        
    
spørsmål() 
    

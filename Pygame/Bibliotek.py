
class Bok:
    def __init__(self, tittel, forfatter, ISBN, utgivelsesår, sjanger):
        self.tittel = tittel
        self.forfatter = forfatter
        self.ISBN = ISBN
        self.utgivelsesår = utgivelsesår
        self.sjanger = sjanger
        
    def infoOmBok(self):
        print(f"Tittel: {self.tittel}, Forfatter: {self.forfatter}, ISBN: {self.ISBN}, Utgivelsesår: {self.utgivelsesår}")
    
# bok1 = Bok("jbh sitt liv", "jbh", 123123, 2024)

# bok1.infoOmBok()

class Lydbok(Bok):
    def __init__(self, tittel, forfatter, ISBN, utgivelsesår, sjanger, forteller, lengde):
        super().__init__(tittel, forfatter, ISBN, utgivelsesår, sjanger)
        self.forteller = forteller
        self.lengde = lengde
        
    def infoOmBok(self):
        super().infoOmBok()
        print(f"Forteller: {self.forteller}, lengde: {self.lengde} minutter")
        
class Digitalbok(Bok):
    def __init__(self, tittel, forfatter, ISBN, utgivelsesår, sjanger, nedlastningslenke, filStørelse):
        super().__init__(tittel, forfatter, ISBN, utgivelsesår, sjanger)
        self.nedlastningslenke = nedlastningslenke
        self.filStørelse = filStørelse
    
    def infoOmBok(self):
        super().infoOmBok()
        print(f"Nedlastningslenke: {self.nedlastningslenke}, Filstørelse: {self.filStørelse}")

# bok2 = Lydbok("hei", "Forfatter hei", 1234567, 2020, "siri", 30)    

# bok2.infoOmBok()

class Bibliotek:
    def __init__(self):
        self.bøker = {}

        
    def visDict(self):
        return self.bøker
        
    def leggTilBok(self, bok, antall):
        if bok.ISBN in self.bøker:
            self.bøker[bok.ISBN]["antall"] += antall
            print("Boken finnes allerede, antall er updatert")
        else:
            self.bøker[bok.ISBN] = {"bok": bok, "antall": antall, "lånt_ut_teller": 0}
            print("Boken er lagt til!")
            
    def leieBok(self, ISBN):
        if ISBN in self.bøker and self.bøker[ISBN]["antall"] > 0:
            self.bøker[ISBN]["antall"] -= 1
            self.bøker[ISBN]["lånt_ut_teller"] += 1
            return True
        else:
            return False
            
    def leverInn(self, ISBN):
        if ISBN in self.bøker:
            self.bøker[ISBN]["antall"] += 1
            return True
        else:
            return False
    
    def tilgjengelighet(self, ISBN):
        if ISBN in self.bøker:
            return self.bøker[ISBN]["antall"]
        else:
            return 0
    
    def vis_info(self, ISBN):
        if ISBN in self.bøker:
            return self.bøker[ISBN]["bok"].infoOmBok()
        else:
            return "Bok er ikke funnet"
        
    def mestPopulær(self):
        liste = []
        for ISBN, info in self.bøker.items():
            liste.append((info["bok"], info["lånt_ut_teller"]))
        
        liste.sort(key = lambda x: x[1], reverse = True)
        return [(bok.infoOmBok(), teller) for bok, teller in liste]
    
    def hentBøkerSjanger(self, sjanger):
        bøkerMedSjanger = []
        for ISBN, info in self.bøker.items():
            bok = info["bok"]
            if bok.sjanger == sjanger:
                bøkerMedSjanger.append(bok)
        return bøkerMedSjanger
        

        
    def hentBøkerFormat(self, format):
        bøkerMedFormat = []
        for ISBN, info in self.bøker.items():
            bok = info["bok"]
            if isinstance(bok, format):
                bøkerMedFormat.append(bok)
        return bøkerMedFormat
    
                

# Eksempelbruk:
bok1 = Bok("Testbok 1", "Tester 1", 123456, 2024, "Skjønnlitteratur")
bok2 = Lydbok("Lydbok Test", "Tester 2", 123457, 2023, "Fakta", "Siri", 45)
bok3 = Digitalbok("Digital Testbok", "Tester 3", 123458, 2022, "Fantasy", "www.test.com", 50)

# Opprett ett enkelt Bibliotek-objekt
bibliotek = Bibliotek()

# Bruk det samme Bibliotek-objektet for alle operasjoner
bibliotek.leggTilBok(bok1, 3)
bibliotek.leggTilBok(bok2, 2)
bibliotek.leggTilBok(bok3, 5)

fantasy_bøker = bibliotek.hentBøkerSjanger("Fantasy")
for bok in fantasy_bøker:
    bok.infoOmBok()
    
fantasy_bøker = bibliotek.hentBøkerSjanger("Fantasy")
for bok in fantasy_bøker:
    bok.infoOmBok()


# # Lei ut noen bøker for å oppdatere teller
# bibliotek.leieBok(123456)
# bibliotek.leieBok(123456)
# bibliotek.leieBok(123457)

# # Vis informasjon om en bok
# bibliotek.vis_info(123456)

# # Vis tilgjengelighet
# print(bibliotek.tilgjengelighet(123456))

# # Vis hele katalogen
# print(bibliotek.visDict())

# # # Vis mest populære bøker
# print(bibliotek.mestPopulær())

class Bil:
    def __init__(self, registreringsnummer, modell, farge):
        self.registreringsnummer = registreringsnummer
        self.modell = modell
        self.farge = farge
        
    def visInfo(self):
        print(f"Opprettet en {self.farge} {self.modell} med registreringsnummer {self.registreringsnummer}")
        
# testbil = Bil("23fe43", "Tesla", "Rød")
# print(testbil.registreringsnummer)

class Lastebil(Bil):
    def __init__(self, registreringsnummer, modell, farge):
        super().__init__(registreringsnummer, modell, farge)
        
    def antallPlass(self):
        return 2
    
    def avgift(self):
        return 3.0
        
class dateTime:
    def __init__(self, time, minutt):
        self.time = time
        self.minutt = minutt
        
    def visInfo(self):
        return print(f"{self.time}:{self.minutt}")        
    

# dateTime(13,45).visInfo()

class Parkeringshus:
    print("Opprettet parkeringshus med 20 plasser")
    def __init__(self):
        self.biler =  {} #Oppretter et tomt dictionary
        self.plasser = 20
        
    def visDict(self):
        return print(self.biler)
    
    def innkjøring(self, bil, tid):
        if self.plasser > 0:
            if isinstance(bil, Lastebil):
                self.plasser -= bil.antallPlass()
            else: 
                self.plasser -= 1
            self.biler[bil.registreringsnummer] = {"bil": bil, "tid": tid} #Gjør at registreringsnummer blir nøkkel og bilobjekt og tid blir verdi
            print(f"{bil.registreringsnummer} kjørte inn {tid.time}:{tid.minutt}")
            return print("Plasser tilgjengelig: ", self.plasser)
        else:
            return print("Ikke flere plasser tilgjengelig")
    
# phus = Parkeringshus()
# testbil = Bil("23fe43", "Tesla", "Rød")               #Testing av metoder
# tid = dateTime(13, 45)

# phus.innkjøring(testbil,tid)
# phus.visDict()
    
            
    def utkjøring(self, registreringsnummer, tid):
        if registreringsnummer in self.biler:
            tidUt = tid.time * 60 + tid.minutt #Gjør tiden om til minutter
            tidInn = self.biler[registreringsnummer]["tid"].time * 60 + self.biler[registreringsnummer]["tid"].minutt
            parkeringsTid = tidUt - tidInn #Minuser ut med inn for å få forskjellen mellom minutter
            if isinstance(self.biler[registreringsnummer]["bil"], Lastebil):
                avgift = parkeringsTid * self.biler[registreringsnummer]["bil"].avgift()
                self.plasser += self.biler[registreringsnummer]["bil"].antallPlass()
            else: 
                avgift = parkeringsTid * 1.50
                self.plasser += 1
            bilen = self.biler[registreringsnummer]["bil"]
            print(f"{registreringsnummer} {bilen.farge} {bilen.modell} kjørte ut {tid.time}:{tid.minutt}")
            print(f"Parkeringstid: {parkeringsTid} minutter, avgift: {avgift}kr")
            self.biler.pop(registreringsnummer)
        return print("Plasser tilgjengelig: ", self.plasser)
    
    def bilerFarge(self, farge):
        for farger in self.biler.values(): #Den går gjennom og sjekker om biler er lilla, men den stopper etter at den har funnet en lilla.
            if farger["bil"].farge == farge:
                print(f"Parkerte biler som er {farger["bil"].farge}: {farger["bil"].modell} {farger["bil"].registreringsnummer}")
        
            
phus = Parkeringshus()
testbil = Bil("abc123", "Porsche", "lilla")
tid = dateTime(13, 45)
phus.innkjøring(testbil,tid)


testbil2 = Lastebil("1234bac", "BMW", "lilla")
tid = dateTime(14, 00)
phus.innkjøring(testbil2,tid)

phus.bilerFarge("lilla")

tid = dateTime(14, 15)
phus.utkjøring("abc123", tid)

tid = dateTime(14, 20)
phus.utkjøring("1234bac", tid)

#Oppgave 2d Det som er problematisk med et manuelt registrering som oppfyller kravene er at folk kan registrere seg selv inn som en vanlig bil for å unngå de økte avgiftene. 
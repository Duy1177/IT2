class Bil:
    def __init__(self, registreringsnummer, model, farge):
        self.registreringsnummer = registreringsnummer
        self.model = model
        self.farge = farge
        
    def visInfo(self):
        print(f"Opprettet en {self.farge} {self.model} med registreringsnummer {self.registreringsnummer}")
        
# testBil= Bil(123,"tesla", "rød")
# print(testBil.visInfo())

class lasteBil(Bil):
    def __init__(self, registreringsnummer, model, farge):
        super().__init__(registreringsnummer, model, farge)
    
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


class parkeringsHus:
    def __init__(self):
        print("Parkeringshus med 20 plasser opprettet")
        self.biler = {}
        self.plasser = 20
        
    def visInfo(self):
        return print(self.biler)
    
    def innkjøring(self, bil, tid):
        if self.plasser > 0:
            if isinstance(bil, lasteBil):
                self.plasser -= bil.antallPlass()
            else:  
                self.plasser -= 1
            self.biler[bil.registreringsnummer] = {"bil": bil, "tid": tid}
            print(f"{bil.registreringsnummer} kjørte inn {tid.time}:{tid.minutt}")
            print("Plasser tilgjengelig:", self.plasser)
        else: print("Ingen flere plasser")
    
    def utkjøring(self, registreringsnummer, tid):
        if registreringsnummer in self.biler:
            tidUt = tid.time * 60 + tid.minutt
            tidInn = self.biler[registreringsnummer]["tid"].time * 60  + self.biler[registreringsnummer]["tid"].minutt
            parkeringsTid = tidUt - tidInn
            if isinstance(self.biler[registreringsnummer]["bil"], lasteBil):
                avgift = parkeringsTid * self.biler[registreringsnummer]["bil"].avgift()
                self.plasser += self.biler[registreringsnummer]["bil"].antallPlass()
            else:
                avgift = 1.5 * parkeringsTid
                self.plasser += 1
            bilen = self.biler[registreringsnummer]["bil"]
            print(f"{registreringsnummer} {bilen.farge} {bilen.model} kjørte ut {tid.time}:{tid.minutt}")
            print(f"Parkeringstid: {parkeringsTid} minutter, avgift: {avgift}KR")
            print("Plasser:", self.plasser)
            
    def bilerFarge(self,farge):
        for farger in self.biler.values():
            if farger["bil"].farge == farge:
                print(f"Parkerte biler som er {farger["bil"].farge}: {farger["bil"].model} {farger["bil"].registreringsnummer}")


phus = parkeringsHus()
testbil = Bil("123a","tesla","rød")
tid = dateTime(13,45)
phus.innkjøring(testbil,tid)

testbil2 = lasteBil("123b", "BMW", "lilla")
tid = dateTime(14, 00)
phus.innkjøring(testbil2,tid)


tid = dateTime(14,15)
phus.utkjøring("123b", tid)

# phus.bilerFarge("lilla")



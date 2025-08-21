class konto:
    def __init__(self, navn, kontonummer):
        self.navn = navn
        self.kontonummer = kontonummer
        self.saldo = 0
        
    def sett_inn(self, penger):
        self.saldo += penger
        print(f"Du satt inn {penger}.\nNy saldo er {self.saldo}")
    
    def ta_ut(self, penger):
        if penger > self.saldo:
            print(f"Du prøver å ta ut {penger}.\nIkke dekning på konto\nSaldoen er {self.saldo}")
        else: 
            self.saldo -= penger
            print(f"Du tok ut {penger}\nNy saldo er {self.saldo}")
        
    def __str__(self):
        return f"Konto:\n Eier: {self.navn} \n Kontonummer: {self.kontonummer}\n Saldo: {self.saldo}"
        
Kontoen = konto("Hei", "32324424")
Kontoen.sett_inn(43)
print(Kontoen)
Kontoen.ta_ut(30)
print(Kontoen)
class Bok():
    def __init__(self,tittel:str, forfatter:str,):
        self.tittel = tittel
        self.forfatter = forfatter
        self.utlånt = False #Starter som ikke utlånt
        
    def visInfo(self):
        if self.utlånt == False:
            return f"Tittel: {self.tittel}\nForfatter: {self.forfatter}\nStatus: Ikke utlånt"
        else:
            return f"Tittel: {self.tittel}\nForfatter: {self.forfatter}\nStatus: Boken er utlånt"
        
# bok = Bok("Test", "Thanos", "Meg")
# print(bok.visInfo())

class Låner():
    def __init__(self, lånerID:int):
        self.lånerID = lånerID
        self.lånteBøker = []
        
    def lånBok(self, bok):
            if bok.utlånt == False:
                bok.utlånt = True
                self.lånteBøker.append(bok.tittel)
                print(f"{self.lånerID} lånte boken {bok.tittel}")
            else: 
                print(bok.tittel, "er utlånt allerede.")
            
    def leverTilbakeBok(self, bok):
        if bok.utlånt == True and bok.tittel in self.lånteBøker:
            self.lånteBøker.remove(bok.tittel)
            bok.utlånt = False
            print(f"Du leverte tilbake boken {bok.tittel}")
        else: 
            print("Du kan ikke levere inn en bok du ikke har!")

    
bok = Bok("Test", "Thanos")   
bok2 = Bok("Hei", "Thor") 

Finny = Låner(123)
Finny.lånBok(bok)
Finny.lånBok(bok2)

Per = Låner(345)
Per.lånBok(bok)
Per.lånBok(bok2)

Finny.leverTilbakeBok(bok)

# import random

# class Character:
#     def __init__(self, name, level, hp, mana):
#         self.name = name
#         self.level = level
#         self.hp = hp
#         self.mana = mana
        
#     def __str__(self):
#         return f"`\nname: {self.name}, level: {self.level}, hp: {self.hp}, mana: {self.mana}\n" 
    
# helt = Character("Helt", 2, 100, 100)
# print(helt.__str__())

#Oppgave 12 
#Legg til en visInfo()-metode i Rektangel-klassen som vi laget ovenfor. 
#Lag et rektangel og et kvadrat og sjekk at visInfo() kan brukes på begge.

# class Rektangel():
#     def __init__(self, lengde, bredde):
#         self.lengde = lengde
#         self.bredde = bredde
    
#     def areal(self):
#         return self.lengde * self.bredde
    
#     def visInfo(self):
#         print(f"bredden er {self.bredde} og lengden er {self.lengde}")

# class Kvadradt(Rektangel):
#     def __init__(self, sidekant):
#         super().__init__(sidekant,sidekant)
        
#     def visInfo(self):
#         print(f"Sidekanten er {self.lengde}")
        
# rektangel1 = Rektangel(2,3)
# kvadrat1 = Kvadradt(4)

# rektangel1.visInfo()
# kvadrat1.visInfo()

#Oppgave 13
#Lag en klasse for billetter for vernepliktige som arver fra klassen Billett. 
# En vernepliktig får 90 % rabatt på en enkeltbillett. 
# Skriv ut resultatet fra beregnPris() og sjekk at prisen stemmer.

# class Billett():
#   def __init__(self):
#       self.mva = 0.12
#       self.pris = 20

#   def beregnPris(self):
#     return self.pris + (self.pris * self.mva)

# class Vernebiletter(Billett):
#     def __init__(self):
#         super().__init__()
#         self.rabatt = 0.90
        
#     def beregnPris(self):
#         orginalPris =  super().beregnPris()
#         return orginalPris * (1 - self.rabatt)
    
# verneBillet = Vernebiletter()

# print(verneBillet.beregnPris())


#Oppgave 14
#Lag klassen UkeBillett som arver fra Billett. 
# Billetten skal tilsvare syv enkeltbilletter, 
# men den gir en rabatt på 20 %. Skriv ut resultatet fra beregnPris() og sjekk at prisen stemmer.

# class Billett():
#   def __init__(self):
#       self.mva = 0.12
#       self.pris = 20

#   def beregnPris(self):
#     return self.pris + (self.pris * self.mva)

# class UkeBillett(Billett):
#     def __init__(self):
#        super().__init__()
#        self.rabatt = 0.20
    
#     def beregnPris(self):
#         ukePris = super().beregnPris() * 7
#         return ukePris * (1 - self.rabatt)
    
# ukeBillett = UkeBillett()

# print(ukeBillett.beregnPris())

#Oppgave 15
# import random

# class Terning():
#     def __init__(self, antallSider):
#         self.antallSider = antallSider
    
#     def trill(self):
#         return random.randint(1,self.antallSider)
    
# print(Terning(6).trill())

# class JukseTerning(Terning):
#     def __init__(self, antallSider, antallKast):
#         super().__init__(antallSider)
#         self.antallKast = antallKast
        
#     def trill(self):
#         resultat = [super().trill() for _ in range(self.antallKast)]
#         return max(resultat)
    
# jukse_terning = JukseTerning(6,6)

# print(jukse_terning.trill())

#Oppgave 18 og 19
class Planet:
    def __init__(self, navn, solavstand, radius, antallRinger = 0):
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius
        self.antallRinger = antallRinger
        self.maaner = []  # Liste for å holde på måner
        
    def visInfo(self):
        print(f"Planeten {self.navn} har {self.antallRinger} ringer, er {self.solavstand} millioner km unna sola og har radius {self.radius} km.")
        if self.maaner:
            print(f"Den har følgende måner:")
            for maane in self.maaner:
                print(f" - {maane.navn} med radius {maane.radius} km og volum {maane.volum():.2f} km³.")

    def leggTilMaane(self, maane):
        self.maaner.append(maane)

planeter = {}

# Lager og legger til noen Planet-objekter
planeter["Merkur"] = Planet("Merkur", 57.9, 2439.7)
planeter["Venus"] = Planet("Venus", 108.2, 6051.8)
planeter["Jorden"] = Planet("Jorden", 149.6, 6371.0)
planeter["Mars"] = Planet("Mars", 227.9, 3389.5)
planeter["Jupiter"] = Planet("Jupiter", 778.5, 69911, 4)
planeter["Saturn"] = Planet("Saturn", 1434.0, 58232, 7)
planeter["Uranus"] = Planet("Uranus", 2871.0, 25362, 13)
planeter["Neptun"] = Planet("Neptun", 4495.1, 24622, 5)

# for p in planeter.values():
#   p.visInfo()
  
planeter["Jorden"].visInfo()

import math

class Måne():
    def __init__(self, navn, radius):
        self.navn = navn
        self.radius = radius
        
    def volum(self):
        return (4/3)*math.pi*self.radius**3
        
Månen = Måne("Månen", 1737.1)

planeter["Jorden"].leggTilMaane(Månen)

planeter["Jorden"].visInfo()

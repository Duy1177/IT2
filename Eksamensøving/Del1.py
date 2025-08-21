
# def beregn(n):
#     s = 0
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             s += i
#         else: 
#             s -= i
#     return print(s)

# beregn(7)

# #Oppgave 5
# antall = 0

# for tall in range(100,1000):
#     h = tall
#     t = h
#     s = 0
    
#     while h != 0:
#         r = h % 10
#         s = s * 10 + r
#         h = h // 10
    
#     if t == s:
#         antall += 1
    
        
# print(antall)

#Oppgave 6
class batteri:
    def __init__(self, id: str, energikapasitet:float):
        self.id = id
        self.energikapasitet = energikapasitet
        self.energinivå = 0
        
    def ladOpp(self, energi):
        if energi < 0:
            raise ValueError("Kan ikke lade med negativ energi")  
        self.energinivå = min(self.energinivå + energi, self.energikapasitet) 
        
    def brukEnergi(self, energi:float):
        if energi < 0:
            raise ValueError("Kan ikke bruke negativ energi")
        elif energi > self.energinivå:
            raise ValueError("Ikke nok energi")
        self.energinivå -=energi
        
    def visEnerginivå(self):
        return self.energinivå
    
print(112//10)
    
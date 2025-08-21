import random
import pygame

class Person():
    def __init__(self):
        self.status = "frisk"
        self.dagerSmittet = 0
        self.dagerSyk = 0 
        
    def smittet(self):
        if self.status == "frisk":
            self.status = "smittet"
        
    def oppdater(self):
        if self.status == "smittet":
            self.dagerSmittet += 1
            if self.dagerSmittet >= 3:
                self.status = "syk"
                self.dagerSyk = 0
        elif self.status == "syk":
            if random.random() <= 0.01:
                self.status = "død"
            else: 
                self.dagerSyk += 1
                if self.dagerSyk >= 4:
                    self.status = "immun"
                    
    def __str__(self):
        return self.status
    
class Populasjon():
    def __init__(self, bredde, høyde):
        self.bredde = bredde
        self.høyde = høyde
        self.rutenett = [[Person() for _ in range(bredde)] for _ in range(høyde)]
        
    def hentNaboer(self, x,y):
        naboer = []
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.bredde and 0 <= ny < self.høyde:
                naboer.append(self.rutenett[ny][nx])
        return naboer
    
    def overfør_smitte(self):
        for y in range(self.høyde):
            for x in range(self.bredde):
                person = self.rutenett[y][x]
                if person.status == "frisk":
                    naboer = self.hentNaboer(x,y)
                    for nabo in naboer:
                        if nabo.status in ["smittet", "syk"]:
                            if random.random() < 0.3:
                                person.smittet()
                                break
    def oppdater(self):
        for rad in self.rutenett:
            for person in rad:
                person.oppdater()
                
    def initierSmitte(self):
        midtx, midty = self.bredde//2,self.høyde//2
        self.rutenett[midty][midtx].status = "syk"
        
        naboPos = [(-1,0),(1,0),(0,-1),(0,1)]
        for dx, dy in naboPos:
            nx, ny = midtx + dx, midty + dy
        if 0 <= nx < self.bredde and 0 <= ny < self.høyde:
            self.rutenett[ny][nx].status = "smittet"

# # Eksempel på bruk av klassen
# populasjon = Populasjon(10,10)  # 10x10 rutenett
# populasjon.initierSmitte()  # Initialiser smitten

# # Kjør simuleringen
# for dag in range(7):  # Kjør simuleringen i 10 dager
#     print(f"Dag {dag + 1}")
#     populasjon.overfør_smitte()  # Spred smitte
#     populasjon.oppdater()  # Oppdater alle personer
#     for y in range(populasjon.høyde):
#         print(" ".join(str(populasjon.rutenett[y][x]) for x in range(populasjon.bredde)))
#     print()
    
    
def kjørSim():
    pygame.init()
    ruteSize = 20
    bredde, høyde = 30,30
    screen = pygame.display.set_mode((bredde*ruteSize, høyde*ruteSize))
    pygame.display.set_caption("Syk Simulering")

    farge = {
        "frisk": "azure3",
        "smittet": "hotpink3",
        "syk": "red",
        "immun": "gray42",
        "død": "black"
    
    }
    
    populasjon = Populasjon(bredde, høyde)
    populasjon.initierSmitte()
    
    klokke = pygame.time.Clock()
    dag = 0
    
    running = True
    simuler = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if simuler:
            populasjon.overfør_smitte()
            populasjon.oppdater()
            dag += 1
            
            if dag == 10:
                simuler = False
            
            for y in range(høyde):
                for x in range(bredde):
                    status = populasjon.rutenett[y][x].status
                    farger = farge[status]
                    pygame.draw.rect(screen, farger, (x * ruteSize, y*ruteSize, ruteSize - 1, ruteSize-1))
            pygame.display.flip()
            klokke.tick(1)
    pygame.quit()
    
if __name__ == "__main__":
    kjørSim()
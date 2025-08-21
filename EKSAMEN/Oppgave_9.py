import random
import pygame


class tre():
    def __init__(self):
        self.brent = False
        
    def brenn(self):
        if random.random() < 0.03:
            if self.brent == False:
                self.brent = True
    
    def __str__(self):
        return self.brent
        

class Skog():
    def __init__(self, bredde, høyde):
        self.bredde = bredde
        self.høyde = høyde
        if random.random() < 0.3:
            self.rutenett = [[None for _ in range(bredde)] for _ in range(høyde)]
        else:
            self.rutenett = [[tre() for _ in range(bredde)] for _ in range(høyde)]
            
    def naboTre(self, x,y):
        naboer = []
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.bredde and 0 <= ny < self.høyde:
                naboer.append(self.rutenett[ny][nx])
        return naboer
    
    def overfør_brann(self):
        for y in range(self.høyde):
            for x in range(self.bredde):
                tre = self.rutenett[y][x]
                if tre.brent == False:
                    naboer = self.naboTre(x,y)
                    for nabo in naboer:
                        if nabo.brent == False:
                            tre.brenn()
                            break
                        
          
    # def initier_brann(self):
    #     x, y = 
        
#Prøver å lage simulering for å se hvordan det ser ut.   
def kjørSim():
    pygame.init()
    ruteSize = 20
    bredde, høyde = 50,50
    screen = pygame.display.set_mode((bredde*ruteSize, høyde*ruteSize))
    pygame.display.set_caption("Skogbrann")

    farge = {
        False: "green",
        True: "red"
    }
    
    Skog = Skog(bredde, høyde)
        
    klokke = pygame.time.Clock()    
    running = True
    simuler = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if simuler:
            Skog.overfør_brann()

            for y in range(høyde):
                for x in range(bredde):
                    status = Skog.rutenett[y][x].brenn
                    farger = farge[status]
                    pygame.draw.rect(screen, farger, (x * ruteSize, y*ruteSize, ruteSize - 1, ruteSize-1))
            pygame.display.flip()
            klokke.tick(1)
    pygame.quit()
    
if __name__ == "__main__":
    kjørSim()
    
                        
import pygame
import time

WIDTH, HEIGHT = 600,500
FPS = 30

class App():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("KlikkKlikkKlikk")
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.timer = pygame.time.get_ticks()
        self.klikk = 0
        
        
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                self.klikk += 1
    
    def update(self):
        self.all_sprites.update()
                
    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        
    def run(self):
        startTime = time.time()
        runTime = 10
        while self.running:

            self.handleEvents()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
            gåttTid = time.time() - startTime
            if gåttTid > runTime:
                print(f"Spillet er slutt, du klikket {self.klikk} ganger")
                self.running = False
            
            
        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.run()
    

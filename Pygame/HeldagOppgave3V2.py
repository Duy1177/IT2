import pygame
import time
import random

WIDTH, HEIGHT = 600, 500
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
        self.farger = ["red", "green", "blue", "grey", "purple", "white"]
        self.klikk = 0
        self.runde = 1
        self.currentFrage = random.choice(self.farger)
        self.besteTid = float("inf")
        self.round_time = 10
        self.rect_size = (200,100)
        self.rect = pygame.Rect(self.random_position(), self.rect_size)
        self.rect_time = time.time()
         
    def random_position(self):
        x = random.randint(0, WIDTH - self.rect_size[0])
        y = random.randint(0, HEIGHT - self.rect_size[1])
        return(x,y)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.klikk += 1
    
    def update(self):
        self.all_sprites.update()
        currentTime = time.time()
        if currentTime - self.rect_time >= 2:
            self.rect.topleft = self.random_position()
            self.rect_time = currentTime
        
                
    def draw(self):
        self.screen.fill(self.currentFrage)
        pygame.draw.rect(self.screen, "black", self.rect)
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        
    def run(self):
        startTime = time.time()
        while self.running:
            self.handleEvents()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
            gåttTid = time.time() - startTime
            if gåttTid >= self.round_time:
                self.end_round(gåttTid)
                startTime = time.time()
    
        self.end_game()
    
    def end_round(self, current_time):
        print(f"Runde {self.runde} er over, du klikket {self.klikk} ganger")
        if current_time < self.besteTid:
            print("Ny bestetid!")
            self.besteTid = current_time
        else:
            print("Du oppnådde ikke ny bestetid.")
        self.runde += 1
        self.klikk = 0
        self.currentFrage = random.choice(self.farger)
    
    def end_game(self):
        print(f"Bestetid: {self.besteTid:.2f} sekunder")
        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.run()

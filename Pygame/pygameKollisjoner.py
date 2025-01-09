#Smidig 3.4.1
import pygame

WIDTH, HEIGHT = 600,500
FPS = 24

# class Ball(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((50,50))
#         self.rect = self.image.get_rect()
#         pygame.draw.circle(self.image, "yellow", (25,25), 25)
#         pygame.draw.circle(self.image, "red", (25,25), 25, 5)
#         self.rect.x = 0
#         self.rect.y = (HEIGHT - self.rect.height)/2
        
#     def update(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             self.rect.x -= 10
#         elif keys[pygame.K_RIGHT]:
#             self.rect.x +=10
#         self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))


class App():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pygame hus")
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        
        # self.ball = Ball()
        # self.all_sprites.add(self.ball)
        
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         self.ball.rect.x -= 10
            #     elif event.key == pygame.K_RIGHT:
            #         self.ball.rect.x += 10
            if event.type == pygame.MOUSEMOTION:
                self.pos = event.pos
    
    def update(self):
        # self.all_sprites.update()
        pass
                
    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        
        pygame.draw.line(self.screen, "white", (300,250), self.pos, 5)
                
        pygame.display.update()
        
    def run(self):
        while self.running:
            self.handleEvents()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.run()
    

# #Smidig 3.4.1
# import pygame

# WIDTH, HEIGHT = 600,500
# FPS = 24

# class App():
#     def __init__(self):
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
#         pygame.display.set_caption("Pygame hus")
#         self.running = True
#         self.all_sprites = pygame.sprite.Group()
        
#     def handleEvents(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
    
#     def update(self):
#         self.all_sprites.update()
        
#     def draw(self):
#         self.screen.fill("darkblue")
#         self.all_sprites.draw(self.screen)
#         pygame.draw.rect(self.screen, 'darkgreen', (0,350,600,150)) # Gress
#         pygame.draw.rect(self.screen, 'red', (100,200,300,200)) # Hus
#         pygame.draw.rect(self.screen, 'orange', (150,250,50,50)) # Vindu med lys
#         pygame.draw.rect(self.screen, 'black', (150,250,50,50),2) # Vindusramme
#         pygame.draw.line(self.screen, 'black', (175,250),(175,300),2) # Sprosse
#         pygame.draw.line(self.screen, 'black', (150,275),(200,275),2) # Sprosse
#         pygame.draw.rect(self.screen, 'black', (300,250,50,50)) # Mørkt vindu
#         pygame.draw.rect(self.screen, 'chocolate3', (225,300,50,100)) # Dør
#         pygame.draw.polygon(self.screen, 'black', ((75,200),(250,100),(425,200))) # Tak
#         pygame.draw.rect(self.screen, 'black', (300,100,50,100)) # Pipe
#         pygame.draw.circle(self.screen, 'grey', (500,100), 40) # Måne
        
#         pygame.display.update()
        
#     def run(self):
#         while self.running:
#             self.handleEvents()
#             self.update()
#             self.draw()
#             self.clock.tick(FPS)
#         pygame.quit()

# if __name__ == "__main__":
#     app = App()
#     app.run()

#Smidig 4.2.1 KANON
# import pygame

# WIDTH, HEIGHT = 400,600
# FPS = 30

# class Canon(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.bredde = 60
#         self.høyde = 40
#         self.image = pygame.Surface((self.bredde, self.høyde), pygame.SRCALPHA)
#         self.rect = self.image.get_rect()
#         pygame.draw.rect(self.image, "grey", (0, 20, 60, 20))
#         pygame.draw.rect(self.image, "grey", (25, 0, 10, 20))
#         self.rect.bottom = HEIGHT
#         self.rect.centerx = WIDTH // 2
#         self.fart = 5
        
#     def update(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT] and self.rect.left > 0:
#              self.rect.x -= self.fart
#         elif keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
#             self.rect.x += self.fart
            
#     def fireGranat(self):
#         return Granat(self.rect.centerx, self.rect.top)
         
            
# class Granat(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.Surface((10,15))
#         self.image.fill(("red"))
#         self.rect = self.image.get_rect()
#         self.rect.centerx = x
#         self.rect.bottom = y
#         self.fart = -5 #Beveger seg oppover
        
#     def update(self):
#         self.rect.y += self.fart
#         if self.rect.bottom < 0:
#             self.kill()

# class App():
#     def __init__(self):
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
#         pygame.display.set_caption("Pygame kanon")
#         self.running = True
#         self.all_sprites = pygame.sprite.Group()
#         self.granater = pygame.sprite.Group()
        
#         self.canon = Canon()
#         self.all_sprites.add(self.canon)

        
#     def handleEvents(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     granat = self.canon.fireGranat()
#                     self.all_sprites.add(granat)
#                     self.granater.add(granat)

    
#     def update(self):
#         self.all_sprites.update()

#     def draw(self):
#         self.screen.fill("black")
#         self.all_sprites.draw(self.screen)                
#         pygame.display.update()
        
#     def run(self):
#         while self.running:
#             self.handleEvents()
#             self.update()
#             self.draw()
#             self.clock.tick(FPS)
#         pygame.quit()

# if __name__ == "__main__":
#     app = App()
#     app.run()
    
#Smidig 3.4.5
# import pygame
# import random
# FPS = 30
# WIDTH = 300
# HEIGHT = 600

# class Baller(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((20, 20))
#         self.image.fill(random.choice(["red", "blue", "green"]))
#         self.rect = self.image.get_rect()
#         self.rect.top = 0
#         self.rect.left = random.randint(0, WIDTH - self.rect.width)
#         self.speed = [random.choice([-1,1]) * random.randint(3,5), random.randint(3,5)]
        
#     def update(self):
#         self.rect.move_ip(self.speed)
#         if self.rect.left < 0 or self.rect.right > WIDTH:
#             self.speed[0] *= -1
#             self.rect.x = min(max(self.rect.x, 0), WIDTH - self.rect.width)
        
#         if self.rect.top > HEIGHT and self.rect.top < 0:
#             self.kill()
            
# class Pad(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((70, 15))
#         self.image.fill("black")
#         self.rect = self.image.get_rect()
#         pygame.draw.rect(self.image, "white", (0, 0, 70, 10))
#         self.rect.bottom = HEIGHT
#         self.rect.centerx = WIDTH//2
#         self.speed = 7
        
#     def update(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT] and self.rect.left > 0:
#             self.rect.x -= self.speed
#         elif keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
#             self.rect.x += self.speed
        

# class App():
#     def __init__(self):
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
#         pygame.display.set_caption("Multi pong")
#         self.running = True
#         self.all_sprites = pygame.sprite.Group()
#         self.timer = pygame.time.get_ticks()
        
#         self.pad = Pad()
#         self.all_sprites.add(self.pad)
        

#     def handleEvents(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
    
#     def update(self):
#         if pygame.time.get_ticks() - self.timer >= 1000:
#             self.timer = pygame.time.get_ticks()
#             self.all_sprites.add(Baller())
            
#         hits = pygame.sprite.spritecollide(self.pad, self.all_sprites, False)
#         for hit in hits:
#             if isinstance(hit, Baller):
#                 hit.speed[1] *= -1
#                 hit.rect.top = self.pad.rect.top - hit.rect.height
        
#         for spirte in self.all_sprites:
#             if isinstance(spirte, Baller) and spirte.rect.top == HEIGHT:
#                 self.running = False
                
        
#         self.all_sprites.update()
                
#     def draw(self):
#         self.screen.fill("black")
#         self.all_sprites.draw(self.screen)
#         pygame.display.update()
        
#     def run(self):
#         while self.running:
#             self.handleEvents()
#             self.update()
#             self.draw()
#             self.clock.tick(FPS)
#         pygame.quit()

# if __name__ == "__main__":
#     app = App()
#     app.run()

#Smidig 4.2.4
import pygame
import random
WIDTH = 600
HEIGHT = 700
FPS = 30


class Baller(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20,20), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.speed = ([random.choice([-1, 1]) * random.randint(3,5), random.choice([-1,1]) * random.randint(3,5)])
        self.radius = 10
        
    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] *= -1
            self.rect.x = min(max(self.rect.x, 0), WIDTH - self.rect.width)
        elif self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed[1] *= -1
            self.rect.y = min(max(self.rect.y, 0), HEIGHT - self.rect.height)
            
class Rødeballer(Baller):
    def __init__(self):
        super().__init__()
        pygame.draw.circle(self.image, "red", (10,10), 10)
        
    def voks(self, bredde, høyde):
        new_width = self.rect.width + bredde
        new_height = self.rect.height + høyde
        self.image = pygame.Surface((new_width, new_height), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (new_width // 2, new_height // 2), new_width // 2)
        self.rect = self.image.get_rect(center=self.rect.center)

class Grønneballer(Baller):
    def __init__(self, x, y):
        super().__init__()
        pygame.draw.circle(self.image, "green", (10,10), 10)
        self.rect.x = x
        self.rect.y = y        


class App():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Agar.io")
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.røde_baller = pygame.sprite.Group()
        self.grønne_baller = pygame.sprite.Group()

        
        for i in range(10):
            røde_baller = Rødeballer()
            grønne_baller = Grønneballer(random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20))
            self.all_sprites.add(røde_baller)
            self.all_sprites.add(grønne_baller)
            self.røde_baller.add(røde_baller)
            self.grønne_baller.add(grønne_baller)
    
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                grønne_baller = Grønneballer(pos[0],pos[1])
                self.all_sprites.add(grønne_baller)
                self.grønne_baller.add(grønne_baller)

    def update(self):
        collisions = pygame.sprite.groupcollide(
            self.røde_baller,
            self.grønne_baller,
            False,
            True,
            collided
        )
        for røde, grønne_list in collisions.items():
            for grønn in grønne_list:
                røde.voks(grønn.rect.width, grønn.rect.height)
        self.all_sprites.update()
                
    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        
    def run(self):
        while self.running:
            self.handleEvents()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
    
def collided(sprite1, sprite2):
    return pygame.sprite.collide_circle(sprite1,sprite2)

if __name__ == "__main__":
    app = App()
    app.run()

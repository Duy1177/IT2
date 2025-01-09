import pygame 

pygame.init()

font = pygame.font.SysFont("Arial",24)


WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 30


class Striker(pygame.sprite.Sprite):
    def __init__(self, posx, posy, width, height, speed, color):
        super().__init__()
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill((0,0,0))
    text = font.render("Hello Pygame!", True,(255,255,255))
    screen.blit(text, (50, 50))
    
    pygame.display.flip()

pygame.quit()
    
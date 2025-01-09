import pygame
import pygame.mixer
import random
import math
import time

class GameScreen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.hidden_object = HiddenObject(self.screen)

    def draw(self):
        self.screen.fill((0, 0, 0))
        # pygame.draw.circle(self.screen, "red", (self.hidden_object.x, self.hidden_object.y), 35)
        # teikn det skjulte objektet for debugging ...
        pygame.display.flip()
        
    def handle_click(self, pos):
        if self.hidden_object.is_clicked(pos):
            print("Gratulerar, du fant det skjulte objektet!")
            return True
        return False

class HiddenObject:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(0, 600)
        self.y = random.randint(0, 600)
        self.speed = 5
        self.visible = True

    def move(self):
        if self.visible:
            self.x = (self.x + random.choice([-1, 1]) * self.speed) % 600
            self.y = (self.y + random.choice([-1, 1]) * self.speed) % 600

    def play_sound(self, pos):
        distance = math.hypot(self.x - pos[0], self.y - pos[1])
        max_distanse = 300
        volume = max(0, (0.80 - distance/max_distanse))
        pygame.mixer.music.set_volume(volume)
        # Juster lydstyrken etter avstanden til det skjulte objektet ...

    def is_clicked(self, pos):
        return math.hypot(self.x - pos[0], self.y - pos[1]) < 30

def main():
    game_screen = GameScreen()
    running = True
    # Starttidspunkt for spelet ..
    startTime = time.time()
    runTime = 120
    
    #runtime = ... # Lengde på lydsample = tida du har på å finne det skjulte objektet
    
    pygame.mixer.init()
    pygame.mixer.music.load("tone.mp3")
    pygame.mixer.music.play()
    # Ved oppstart av spelet, spel av lydfila tone.mp3 ..

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_screen.handle_click(pygame.mouse.get_pos()):
                    print("Du brukte: ", round(gåttTid, 2), "sekunder")
                    running = False
                # Avslutt spelet og skriv ut kor lang tid det tok å finne det skjulte objektet
            
        
        # # Dersom tida er ute, avslutt spelet ...
        gåttTid = time.time() - startTime
        if gåttTid > runTime:
            pygame.mixer.music.stop()
            # text = "Du er en skam"
            # font = pygame.font.SysFont("Arial", 40)
            # text_surface = font.render(text, True, "green")
            # game_screen.screen.blit(text_surface, (600/2 -100, 600/2 -100)) #Prøvde å få stor tekst på skjermen og gjøre at ballen forsvant
            # pygame.display.update()
            # game_screen.hidden_object.visible = False
            print("Du er en skam!")
            running = False
            
        
        game_screen.hidden_object.move()
        game_screen.hidden_object.play_sound(pygame.mouse.get_pos())
        game_screen.draw()
        game_screen.clock.tick(60)
        
        
    pygame.quit()
if __name__ == "__main__":
    main()
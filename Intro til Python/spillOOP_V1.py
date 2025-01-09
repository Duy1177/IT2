import random

class Character():
    def __init__(self, name, hp):
        self.name = name
        self.hp = random.randint(100,200)
        
    def __str__(self):
        return f"\nNavn: {self.name}, HP: {self.hp}"
    
    def is_alive(self):
        return self.hp > 0
                
helt = Character("Tor", 2000)
helt.hp = 0
print(helt)
print(helt.is_alive())
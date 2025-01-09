import random

class Character():
    def __init__(self, name, weapon):
        self.name = name
        self.hp = random.randint(100,200)
        self.weapon = Weapons(weapon)
        
    def __str__(self):
        return f"\nNavn: {self.name}, HP: {self.hp}"
    
    def is_alive(self):
        return self.hp > 0
    
    def attack(self, fiende, attackType = "default"):
        if self.is_alive():
            damage = self.weapon.attack(attackType)
            fiende.injure(damage)
            return damage
        else: 
            return 0
                
    def injure(self, damage):
        self.hp -= damage
        if self.hp <= 0:  
            self.hp = 0 # For å unngå negative verdier
                        
# helt = Character("Tor", 2000)
# helt.hp = 0
# print(helt)
# print(helt.is_alive())

class Weapons():
    weapons = {
            "sword": {"damage": 15},
            "bow": {"damage": 5},
            "axe": {"damage": 10}
        }
    def __init__(self, weapon):
        weapon = weapon.lower().strip()
        if weapon in Weapons.weapons:
            self.name = self.weapons[weapon]
            self.damage = Weapons.weapons[weapon]["damage"]
        else:
            return ValueError(f"Ugyldig våpen: {weapon}")
        
    def attack(self, attackType = "deafult"):
        if self.weapons == "bow":
            if attackType == "charged":
                return self.damage * 1.5
            else: 
                return self.damage
        if attackType == "heavy":
            return self.damage * 1.75
        elif attackType == "quick":
            return self.damage * 0.75
        else:
            return self.damage
            
Tor = Character("Tor", "sword")
Fiende = Character("Fiende", "bow")


# Skrive ut karakterene
print(f"{Tor}, {Fiende}")

# Tor angriper fienden med forskjellige angrepstyper
damage = Tor.attack(Fiende, "heavy")
print(f"{Tor.name} angrep {Fiende.name} med et heavy angrep og forårsaket {damage} skade.")

# Skrive ut fiendens status etter angrepet
print(f"Etter angrepet: {Fiende}")
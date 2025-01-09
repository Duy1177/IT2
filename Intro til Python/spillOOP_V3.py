import random

class Character():
    def __init__(self, name, weapon):
        self.name = name
        self.hp = random.randint(100, 200)
        self.weapon = Weapons(weapon)
        
    def __str__(self):
        return f"\nNavn: {self.name}, HP: {self.hp}"
    
    def is_alive(self):
        return self.hp > 0
    
    def choose_attack(self):
        print("Velg et angrep")
        attack_list = ["heavy", "quick", "charged"]
        attack_type_dmg = [
            self.weapon.attack("charged"),
            self.weapon.attack("heavy"),
            self.weapon.attack("quick")
        ]
        for i in range(len(attack_list)):
            print(f"\n{i + 1}. {attack_list[i].capitalize()} (Damage: {attack_type_dmg[i]})")
        valg = int(input("Skriv inn nummeret på angrepet du vil bruke: ")) - 1
        attackName = attack_list[valg]
        attackDmg = attack_type_dmg[valg]
        return attackName, attackDmg
    
    def attack(self, fiende, attackType="default"):
        if self.is_alive():
            damage = self.weapon.attack(attackType)
            fiende.injure(damage)
            return damage
        else:
            return 0
                
    def injure(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0  # For å unngå negative verdier

class Weapons():
    weapons = {
        "sword": {"damage": 15},
        "bow": {"damage": 5},
        "axe": {"damage": 10}
    }
    def __init__(self, weapon):
        weapon = weapon.lower().strip()
        if weapon in Weapons.weapons:
            self.name = weapon
            self.damage = Weapons.weapons[weapon]["damage"]
        else:
            raise ValueError(f"Ugyldig våpen: {weapon}")
        
    def attack(self, attackType="default"):
        if attackType == "charged":
            return self.damage * 2
        elif attackType == "heavy":
            return self.damage * 1.75
        elif attackType == "quick":
            return self.damage * 0.75
        else:
            return self.damage

# Opprett en karakter for testing
Tor = Character("Tor", "sword")
Fiende = Character("Fiende", "bow")

print(f"{Tor}, {Fiende}")

attack_name, attack_dmg = Tor.choose_attack()
print(f"Valgt angrep: {attack_name}, Skade: {attack_dmg}")

skade = Fiende.injure(attack_dmg)

print(Fiende)
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
            
class Hero(Character):
    def __init__(self, name, weapon):
        super().__init__(name, weapon)
        
    def choose_attack(self):
        print("Velg et angrep")
        attack_list = [ "charged","heavy", "quick"]
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
    
    def use_potion(self):
        original_hp = self.hp
        while self.hp < original_hp:
            for i in range(100):
                self.hp += i
                
class Enemy(Character):
    def __init__(self, name, weapon):
        super().__init__(name, weapon)
        
    def fiende_attack(self):
        attack_list = ["charged","heavy", "quick"]
        attack_type_dmg = [
            self.weapon.attack("charged"),
            self.weapon.attack("heavy"),
            self.weapon.attack("quick")
        ]
        valg = random.randint(0,2)
        attackName = attack_list[valg]
        attackDmg = attack_type_dmg[valg]
        return attackName, attackDmg 

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
Tor = Hero("Tor", "sword")
Fiende = Enemy("Fiende", "bow")
Fiende2 = Enemy("Fiende 2","bow")
Boss = Enemy("Boss", "axe")

print(f"{Tor}, {Fiende}")

while Tor.is_alive() and Fiende.is_alive and Fiende2.is_alive() and Boss.is_alive():
    real_Hp = Tor.hp
    attack_name, attack_dmg = Tor.choose_attack()
    Fiende.injure(attack_dmg)
    print(f"Valgt angrep: {attack_name}, Skade: {attack_dmg}")
    print(f"Fiende har nå {Fiende.hp} HP")
    if Tor.hp <= real_Hp:
        print("Trykk 4 for å bruke potion, Trykk 5 for å beholde")
        if int(input()) == 4:
            Tor.use_potion()
            print("Du healet til", Tor.hp)
        else: pass
    if not Fiende.is_alive():
        print(Fiende.name," Er beseiert!")
        break
    
    attack_name, attack_dmg = Fiende.fiende_attack()
    Tor.injure(attack_dmg)
    print(f"Fiende valgte angrep: {attack_name}, Skade: {attack_dmg}")
    print(f"Tor har nå {Tor.hp} HP")
    if not Tor.is_alive():
        print(Tor.name," Er beseiert!")
        break

    
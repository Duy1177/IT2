class enhet:
    def __init__(self, name):
        self.name = name
        


class lys(enhet):
    def __init__(self, name, is_on = False, lysStyrke = 0):
        super().__init__(name)
        self.is_on = is_on
        self.lysStyrke = lysStyrke
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.name} er på")
    
    def turn_off(self):
        self.is_on = False
        print(f"{self.name} er av")
        
    def turnOpp(self):
        pass
    def turnDown(self):
        pass
    def status(self):
        if self.is_on == True:
            print("På")
        elif self.is_on == False:
            print("Av" )   

# class termostat:
#     def __init__(self):

#     def temp_opp(self):
        
#     def temp_ned(self):
        
#     def status(self):
    
class smartHus:
    def __init__(self):
        print("Smarthus opprettet")
        self.lys = []
        self.termostat = []
    
    def addLys(self, lys):
        self.lys.append(lys)
        print(f"{lys.name} er lagt til i listen")
        
    def turnOffAll(self):
        for lys in self.lys:
            lys.turn_off()
        print("Alle lys er slått av")
        
hus = smartHus()
lys1 = lys("StueLys")
lys1.turn_on()
hus.addLys(lys1)
lys2 = lys("Kjøkken Lys")
lys2.turn_on()
hus.addLys(lys2)

hus.turnOffAll()
lys1.status()

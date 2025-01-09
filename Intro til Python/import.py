import math
import calendar

r = 12

Areal = round(math.pi*r**2,2) #Finner areal
Omkrets = round(2*math.pi*r,2) #Finner omkrets

print(f"Areal er {Areal} og omkrets er {Omkrets}") 

print(calendar.month(2006,12)) #Kalender

# def pythagoras(a,b):
#      c = a**2+b**2
#      return math.sqrt(c)

# print(f"Svaret er {pythagoras(0,3)}")

# vinkel = 60
# hosliggendekatet = 7

# tilRadianer = math.radians(vinkel)

# hypotenus = hosliggendekatet/math.cos(tilRadianer)

# print(hypotenus)

# ord = "spiser"
# lengde = len(ord)
# nyttOrd = ord[2] + ord[lengde - 3]
# print(nyttOrd)
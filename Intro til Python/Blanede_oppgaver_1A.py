# #Oppgave 1
#a
import math

radius = 31.83
omkrets = 2*math.pi*radius
lengde = 100

print(f"Banelengden er {omkrets+(2*lengde):.2f}m")
#b
fart = 50

m_s = 50 /3.6

print(f"{m_s:.2f} ms")

tiRunder = lengde*10
tidPåRundene = tiRunder/m_s

print(tidPåRundene, "sekunder")
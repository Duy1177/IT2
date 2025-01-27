import csv
import matplotlib.pyplot as plt # pip install matplotlib
from matplotlib.ticker import ScalarFormatter

filnavn = "Korona tilfeller.csv"

arstall = []
tilfeller = []

with open(filnavn, encoding="UTF-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    
    overskrifter = next(filinnhold)
    print(overskrifter)
    
    for rad in filinnhold:
        arstall.append(int(rad[0]))
        tilfeller.append(int(rad[1]))
        
        
# Tegner grafen
plt.plot(arstall, tilfeller) # Utgangspunkt i listene, x- og y-akse
plt.grid()
plt.ylabel("Smittede")
plt.xlabel("År")
# ALTERNATIVT: Bruk ScalarFormatter for å vise reelle tall på y-aksen (iike vitenskapelig notasjon, eks. 1e6)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.get_major_formatter().set_scientific(False)

plt.show()
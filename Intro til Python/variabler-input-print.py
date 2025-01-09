#variabler
tall1 = 5
tall2 = 4
resultat = tall1 + tall2
print("Summen er av",tall1, "og", tall2, "er", resultat, sep=(" "))
print(f"Summen av {tall1} og {tall2} er {resultat}") #formated string

#Oppgave: Gjør det mulig for brukeren å velge hva tall1 og 2 er

tallen = int(input("tall 1:"))
tallto = int(input("tall 2:"))
summen = tallen + tallto
print(f"Summen av tallene er", summen)
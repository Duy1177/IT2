# Lag en liste med fem tall: numbers = […]
number = [1, 2, 3, 4, 5]

# Legg til et element til listen på slutten

number.append(6)


# Legg til et element til listen på en spesifikk indeks
number.insert(2, "nytttall")

# Fjern et element fra listen på en spesifikk indeks
number.remove(2)


# Oppdater et element i listen på en spesifikk indeks
number[4] = "ny4"

# Finn lengden på listen
lengde = len(number)

# Slå opp et element i listen basert på indeksen
if "ny4" in number:
    print("ny4 er i listen")


# Slå opp et element i listen basert på verdien
if 6 in number:
    print("6 er i listen")
    

print(number)
print("Lengden er ", lengde)

# Sammenlign to lister for likhet -- # NB: Kan du gjøre dette vha en løkke?
liste1 = [1,2,3,4,5,6,7]
liste2 = [1,2,3,4,5,6]

like_lister = False

if liste1 == liste2:
    like_lister = True
else:
    for i in range(len(liste1)):
        if liste1 != liste2:
            like_lister = False
            break

if like_lister:
    print("Listene er like")
else: 
    print("listene er ikke like")


# Fjern duplikater fra en liste
liste = [1,2,3,3,4,6,3,7]

liste = list(set(liste))

print("Listen uten duplikater", liste)


# Sorter en liste
tall = [9, 1, 5, 8, 3, 4, 10, 7, 11, 2, 6] 
tall.reverse()
print("Gjør det bare motsatt", tall)
tall.sort()
print("Sortert tall", tall)
tall.sort(reverse=True)
print("Reversed tall og sorted", tall)

#Bruker random og å lage liste 
import random as rd

# Tom liste der vi skal lagre de tilfeldige tallene
tilfeldige_tall = []

# Lager femti tilfeldige tall og legger dem til i lista
for i in range(50):
  tilfeldig = rd.uniform(1, 100)
  tilfeldige_tall.append(tilfeldig)

# Sorterer lista med tilfeldige tall
tilfeldige_tall.sort()

# Skriver ut det første og det siste tallet i lista
print(f"Første (og minste) tall i listen: {tilfeldige_tall[0]}")
print(f"Siste (og største) tall i listen: {tilfeldige_tall[-1]}")

# Oppgåve: Småøvingar, del 2

# Lag lista verdensdeler som inneholder verdensdelenes navn. Skriv ut den første, 
# midterste og siste verdensdelen i lista. 
# Bruk både positive og negative indekser for å skrive ut verdiene.
verdensdeler = ["Nord-Amerika", "Sør-Amerika", "Afrika", "Oseania", "Antarktis"]
print("verdensdeler:",verdensdeler[0], verdensdeler[2],verdensdeler[-1])


#Lag en liste med heltallene fra og med 1 til og med 50. Skriv ut lista for å sjekke at du har fått med de riktige tallene.
ListeMedTallTil50 = []
for i in range(51):
    ListeMedTallTil50.append(i)
    
print(ListeMedTallTil50)
#Lag en liste med de første 100 positive oddetallene. Skriv ut lista for å sjekke at du har fått med de riktige tallene.
listeOddetall = []
for i in range(1,101,2):
    listeOddetall.append(i)
    
print(listeOddetall)

#Lag en liste som inneholder de første 20 kvadrattallene. Kvadrattall er tall opphøyd i annen, for eksempel 22, 32, osv.
listeKvadrat = []
for i in range(1,21):
    i = i**2
    listeKvadrat.append(i)
print("ListeKvadrat:",listeKvadrat)

# #Lag en liste som inneholder de første 15 kubikktallene. Kubikktall er tall opphøyd i tredje, for eksempel 23, 33, osv.
# listeKubikk = []
# for i in range(1,16):
#     i = i**3
#     listeKubikk.append(i)
# print("ListeKubikk:",listeKubikk)

#Finn ut hva funksjonene min() , max() og sum() gjør. Bruk dem på lister som du har laget i oppgavene ovenfor (lister med tall).

listeKubikk = []
for i in range(1,16):
    i = i**3
    listeKubikk.append(i)
print("ListeKubikk:",listeKubikk)

minTall = min(listeKubikk)
print("Minste tallet i listen:", minTall)

maxTall = max(listeKubikk)
print("største tallet i listen:", maxTall)

sumTall = sum(listeKubikk)
print("summen av listen:", sumTall)

#Manuell sortering
def jens_sort(Tallene):
    tallKopi = Tallene[:]
    tallSortert = []

    for _ in Tallene:
        minst = min(tallKopi)
        tallSortert.append(minst)
        tallKopi.remove(minst)
    
    return tallSortert



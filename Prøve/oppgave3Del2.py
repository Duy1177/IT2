import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sikkerhet-full.csv", delimiter=";", skipinitialspace=True)
# print(df.head())

attackType = df["Attack Type"].value_counts() #Leser unik values

attackListe = attackType.index.tolist()#Gjør om til liste"
attackAntall = attackType.values.tolist()

for attack in attackListe:
    print(f"Attack type i form av {attack} finnes")

# print(attackAntall)
attackAntall.sort(reverse=True)
print(f"DDos utgjør {(attackAntall[0]/sum(attackAntall))*100}% av totalen") #Finner prosent

plt.bar(attackListe, attackAntall, color=["darkblue", "red"])#lager graf
plt.xlabel("Attack type")
plt.ylabel("Attack antall")
plt.title("Attack / type")
plt.show()
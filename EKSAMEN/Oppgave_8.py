import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("friluftsaktiviteter.csv", delimiter=";")
# for _,verdier in df.iterrows():
#     indeks = verdier.value_counts()
#     listen = indeks.index.to_list()
#     print(listen)
# for i in range(len(listen)):
# antall = df.groupby("friluftslivsaktivitet").sum()
# print(antall.value_counts())

df.set_index("friluftslivsaktivitet", inplace=True)
df = df.apply(pd.to_numeric, errors="coerce")

summert = df.sum(axis=1)

# print(summert)

fylke = input("Velg et fylke: ")
matchende_kolonner = [kol for kol in df.columns if fylke.lower() in kol.lower()]

if matchende_kolonner:
    valgt_kolonne = matchende_kolonner[0]  # Bruk første treff
    aktivitetstall = df[valgt_kolonne].sort_values()
    aktivitetstall["%"] = df[valgt_kolonne]/df.[va]
    print(aktivitetstall)

    
    
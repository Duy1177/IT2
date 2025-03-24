import pandas as pd

df = pd.read_csv("sikkerhet-full.csv", delimiter=";", skipinitialspace=True)
# print(df.head())


protokoler = df["Protocol"].value_counts() #Teller hvor mange unike verdier det er

protocols = protokoler.index.tolist() #Gjør protokolene om til en liste
for protocol in protocols:
    print(f"{protocol} er brukt {protokoler.get(protocol,0)} ganger") #Finner antallet som hører til protocol og printer den ut
    


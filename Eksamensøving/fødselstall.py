import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Datasett_fodselstall.csv", delimiter="\t")

# print(df.iloc[0])

# befolkningsutvikling = {}

# årstall = df["år"]
# årstallList = årstall.values.tolist()
# innflytning = df["Innflyttinger"]
# innflytningList = innflytning.values.tolist()
# utflytning = df["Utflyttinger"]
# utflytningList = utflytning.values.tolist()

# befolkningsutvikling["fødselstall"] = årstallList
# befolkningsutvikling["Innflyttinger"] = innflytningList
# befolkningsutvikling["Utflyttinger"] = utflytningList

# print(befolkningsutvikling)

df_visning = df[["år", "Levendefødte i alt", "Innflyttinger", "Utflyttinger"]]
df_visning.columns = ["år","fødselstall", "innflyttninger", "utflyttninger"]


df_visning["fødselstall"] = pd.to_numeric(df_visning["fødselstall"],errors="coerce" )
df_visning["innflyttninger"] = pd.to_numeric(df_visning["innflyttninger"],errors="coerce").fillna(0)
df_visning["utflyttninger"] = pd.to_numeric(df_visning["utflyttninger"],errors="coerce").fillna(0)
 
    
df_visning["netto folkevekst"] = ( df_visning["fødselstall"] + df_visning["innflyttninger"] -df_visning["utflyttninger"])
    
# print(df_visning)

start = int(input("Skriv et starts-årstall fra 1945-2024 "))
slutt = int(input("Skriv et slutt-årstall fra 1945-2024 "))

if start >=1945 and slutt <=2024:
    df_periode = df_visning[(df_visning["år"]>= start) & (df_visning["år"]<= slutt)]

plt.plot(df_periode["år"], df_periode["netto folkevekst"], marker = "o", linestyle ="-")
plt.title(f"netto folkevekst fra {start} - {slutt}")
plt.xlabel("år")
plt.ylabel("nettovekst")
plt.grid()
plt.show()

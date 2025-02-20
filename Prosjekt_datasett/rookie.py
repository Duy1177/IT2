import pandas as pd
import matplotlib.pyplot as plt

# Importer CSV-filer
stats_df = pd.read_csv('NBA_Rookie_stats.csv', header = 1)
physical_df = pd.read_csv('NBA_Rookie_physical.csv')

# print(stats_df)
# print(physical_df)

# Endre "PLAYER" til "Player" i physical_df
physical_df = physical_df.rename(columns={"PLAYER": "Player"})

# Merge de to csv filene, "on='Player'" betyr at vi kobler på spillerens navn. "how='inner'" sikrer at vi kun tar med spillere som finnes i begge filer. 
merged_df = pd.merge(stats_df, physical_df, on = "Player", how = "inner")

# Konverter PTS.1(points per game) til numerisk verdi, ignorer feil
merged_df["PTS.1"] = pd.to_numeric(merged_df["PTS.1"], errors="coerce")

#Funksjon for å gjøre ft til inches
def ft_to_inches(height):
    try:
        feet, inches = height.split("' ")
        feet = int(feet)
        inches = float(inches.strip("''"))
        return feet * 12 + inches
    except:
        return None

#Bruker funksjonen for å lage en ny kolonne med høyde i inches
merged_df["HEIGHT INCHES"] = merged_df["HEIGHT W/O SHOES"].apply(ft_to_inches)
#Fjerner rader hvor Height inches er NaN
merged_df = merged_df.dropna(subset=["HEIGHT INCHES"])


ShorterPlayers = []
TallerPlayers = []
Bigs = []

#Bruker itterows for å iterere gjennom radene og plassere de i riktig array. _ er der for å ignorere indeksen og bare bruke raden sin data
for _,player in merged_df.iterrows():
    if player["HEIGHT INCHES"] <= 76: #6'4 eller under
        ShorterPlayers.append(player["Player"])
    elif 77 <= player["HEIGHT INCHES"] <= 81: #6'5 - 6'9
        TallerPlayers.append(player["Player"])
    else: #6'10 og høyere
        Bigs.append(player["Player"])

# print("Shorter Players (≤6'4''):", ShorterPlayers)
# print("Taller Players (6'5''–6'9''):", TallerPlayers)
# print("Bigs (≥6'10''):", Bigs)

PPG_Small = []
PPG_Taller = []
PPG_Bigs = []


#Append spilleren sine points per game hvis spilleren er inne i arrayet
for indeks, player in merged_df.iterrows():
    if player["Player"] in ShorterPlayers:
        PPG_Small.append(player["PTS.1"])
    elif player["Player"] in TallerPlayers:
        PPG_Taller.append(player["PTS.1"])
    else: 
        PPG_Bigs.append(player["PTS.1"])
        
Avg_small = sum(PPG_Small)/len(PPG_Small)
Avg_taller = sum(PPG_Taller)/len(PPG_Taller)
Avg_bigs = sum(PPG_Bigs)/len(PPG_Bigs)

labels = ["PPG 6'4 and under", "PPG 6'5-6'9", "PPG 6'10 and taller"]
values = [Avg_small, Avg_taller, Avg_bigs]

plt.bar(labels, values)
plt.title("Average PPG for height")
plt.xlabel("Height")
plt.ylabel("PPG")
plt.show()

# # Sorter etter poeng per kamp (PTS.1) i synkende rekkefølge
# top_scorer = merged_df.sort_values(by="PTS.1", ascending=False).iloc[1]

# print("Spilleren med høyest PPG er:", top_scorer["Player"], "med", top_scorer["PTS.1"], "poeng per kamp.")



#Kilder https://www.basketball-reference.com/leagues/NBA_2025_rookies.html 
#https://www.nba.com/stats/draft/combine-anthro?sort=HEIGHT_WO_SHOES&dir=1&SeasonYear=2024
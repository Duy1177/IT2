import csv

# Møter problemer med å hoppe første rad i "NBA_Rookie_stats.csv", og med å merge de to csv-filene sammen

with open("NBA_Rookie_stats.csv", mode="r", encoding="utf-8") as file:
    data = csv.reader(file)
    next(data, None)
    rows = list(data)    # Leser resten av dataene
    print(rows[1])
    


with open("NBA_Rookie_physical.csv", mode="r", encoding="utf-8") as file:
    data = csv.reader(file)
    header = next(data)  # Leser inn header-raden
    print(header)
    

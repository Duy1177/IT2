#a) 
# Lag et program som presenterer de tre mest brukte startlokasjonene og de tre minst 
# brukte startlokasjonene. Presentasjonen skal også vise antall turer fra disse startlokasjonene.

# import pandas as pd

# df = pd.read_csv("05.csv")

# locationCounts = df["start_station_name"].value_counts()

# Top3 = locationCounts.nlargest(3)
# Bott3 = locationCounts.nsmallest(3)

# print(f"De tre mest brukte startlokasjonene: ")
# for location, count in Top3.items():
#     print(f"{location}: {count} turer")
    

# print(f"\nDe tre minst brukte startlokasjonene: ")
# for location, count in Bott3.items():
#     print(f"{location}: {count} turer")
    
#Manuell måte
import csv

with open("05.csv", "r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    next(reader)
    data = list(reader)
    
startLocations = []

for row in data:
    startLocation = row[4]
    
    startLocations.append(startLocation)
    
locationCounts = {}
for location in startLocations:
    if location in locationCounts:
        locationCounts[location] += 1
    else: 
        locationCounts[location] = 1
        
sorted_locations = sorted(locationCounts.items(), key=lambda item: item[1]) #?
    
top3 = sorted_locations[-3:]
bott3 = sorted[:3]

print("De tre mest brukte startlokasjonene:")
for location, count in reversed(top3):
    print(f"{location}: {count} turer")

print("\nDe tre minst brukte startlokasjonene:")
for location, count in bott3:
    print(f"{location}: {count} turer")
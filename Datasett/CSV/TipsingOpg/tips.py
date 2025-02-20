import pandas as pd

df = pd.read_csv("tips.csv")

print(df.head())

# dinner = 0
# dinnerCount = df["time"]

# for dinners in dinnerCount:
#     if dinners == "Dinner":
#         dinner +=1
#     else: None
# print(dinner)

# antallMåltid = df["time"].sum()
# print("Antall måltid: ", antallMåltid)
antallmåltid = df["time"].count()
antallDinner = (df["time"] == "Dinner").sum()
antallLunch = (df["time"] == "Lunch").sum()

print("Antall måltid: ", antallmåltid)
print("Antall dinner:", antallDinner)
print("Antall lunch:", antallLunch)
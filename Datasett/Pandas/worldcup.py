import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("world_cups.csv")
# print(df.head())

# print("Total world cups:", df['Year'].nunique()+1)

totalGoals = df["Goals Scored"].sum()
MostGoals = df.groupby("Year")["Goals Scored"].sum().sort_values(ascending=False).head(5)
print(MostGoals)
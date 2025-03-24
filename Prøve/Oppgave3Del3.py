import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sikkerhet-full.csv", delimiter=";", skipinitialspace=True)
# print(df["Device Information"])

operativeSystem = df["Device Information"]
operativeSystem.tolist()
# print(operativeSystem[0])

Windows = 0
Macintosh = 0
for device in operativeSystem:
    if "Windows" in device:
        Windows += 1

print(Windows)

for device in operativeSystem:
    if "Macintosh" in device:
        Macintosh += 1
print(Macintosh)

# eksempel = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0);"
# if "Windows" in eksempel:
#     print(1)
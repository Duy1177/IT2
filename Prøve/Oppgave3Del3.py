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
    if "Macintosh" in device:
        Macintosh += 1

print(Windows)
print(Macintosh)

devices = ["Windows", "Macintosh"]
attacked = [Windows, Macintosh]

plt.bar(devices, attacked, color=["darkblue", "red"])
plt.xlabel("Device")
plt.ylabel("Attacks")
plt.title("Attacks per device")
plt.show()
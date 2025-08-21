# import math
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         area = math.pi*self.radius**2
#         return round(area,2)
    
#     def perimiter(self):
#         return 2*math.pi*self.radius
    
# Sirkel =Circle(3)
# print(Sirkel.area())
# print(Sirkel.perimiter())

#BIlde
# import PIL
# import PIL.Image

# image = PIL.Image.open("image.png")
# image.thumbnail((1000,1000))
# # image.resize(())
# image.save("image-thumbnail.png")
# image.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bilSalg.csv", delimiter=";")

# verider = df["Bilmerke"].value_counts()
# bilMerker = verider.keys().to_list()
# bilMerker.sort()

# antall = {merke: 0 for merke in bilMerker}


# for _,bil in df.iterrows():
#     merke = bil["Bilmerke"]
#     antall[merke] += int(bil["Antall"])
            
# print(antall)

#
df["Antall"] = pd.to_numeric(df["Antall"], errors="coerce")
antall = df.groupby("Bilmerke")["Antall"].sum()
antall = antall.sort_values(ascending=True)

plt.bar(antall.index, antall.values)
plt.xlabel("merke")
plt.ylabel("antall")
plt.show()

start = int(input("Skriv start fra 2010-2015"))
slutt = int(input("Skriv slutt fra 2010-2015"))
if start >=2010 and slutt <=2015:
    df_periode = df[(df["År"]>= start) & (df["År"]<= slutt)]
    
antall = df_periode.groupby("Bilmerke")["Antall"].sum()
antall = antall.sort_values(ascending=True)
antall = antall.sort_values(ascending=True)
print(antall)

# plt.bar(antall.index, antall.values)
# plt.xlabel("merke")
# plt.ylabel("antall")
# plt.show()

# class Spiller():
#     def __init__(self):
#         self.tilstand = "Uskadet"
#         self.angrepet = False
#         self.dagerSkadet = 0
#         self.dagerAlvorligSkadet = 0
#         self.gangerHelbredet = 0
        
#     def attacked(self):
#         self.angrepet = True
        
#     def skadet(self):
#         if self.angrepet == True and self.tilstand =="Uskadet":
#             self.tilstand = "skadet"
        
#     def helbredet(self):
#         if self.tilstand in ["Skadet", "Alvorlig Skadet"]:
#             self.gangerHelbredet += 1
#             self.dagerSkadet = 0
#             self.dagerAlvorligSkadet = 0
        
#         if self.gangerHelbredet >= 3:
#             self.tilstand = "Helbredet med bonus"
#         else:
#             self.tilstand = "Uskadet"
                    
#     def oppdater(self):
#         if self.tilstand == "skadet":
#             self.dagerSkadet += 1
#             if self.dagerSkadet >= 2:
#                 self.tilstand = "Alvorlig skadet"
#                 self.dagerAlvorligSkadet = 0
#         elif self.tilstand == "Alvorlig skadet":
#             self.dagerAlvorligSkadet +=1
#             if self.dagerAlvorligSkadet >= 2:
#                 self.tilstand ="død"
#         else: pass
                
# spiller = Spiller()
# spiller.attacked()
# for dag in range(5):
#     spiller.oppdater()
#     spiller.skadet()
#     print(f"Dag {dag+1}: {spiller.tilstand}")

# import random

# class Figur():
#     def __init__(self,energi):
#         self.energi = energi
        
#     def overførEnergi(self,mengde):
#         if self.energi >= mengde:
#             self.energi -= mengde
#             return mengde
#         return 0 

print("hei \n n")
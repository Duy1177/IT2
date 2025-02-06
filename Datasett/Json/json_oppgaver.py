import json

#Oppgave 2.8.1
# filnavn = "C:\Github\IT2\Datasett\Json\p_2_8_1.json"

# with open(filnavn, encoding="utf-8") as fil:
#     data = json.load(fil)

# print(data)

# navn = data[1]["navn"]
# vekt = data[1]["vekt"]

# print(f"{navn} veier {vekt}kg")

# for obj in data:
#     for nøkkel, verdi in obj.items():
#         print(f"{nøkkel}: {verdi}")
#     print()
    
#Oppgave 2.8.2
# filnavn = "C:\Github\IT2\Datasett\Json\p_2_8_2.json"

# with open(filnavn, "r", encoding="utf-8") as fil:
#     data = json.load(fil)

# personer = []

# while True:
#     navn = input("Skriv et navn: ")
#     if navn =="": 
#         break
    
#     alder = input("Skriv alder: ")
#     if alder.isnumeric():
#         alder = int(alder)
#         personer.append({"navn": navn, "alder": alder})
#     elif alder == "": 
#         break
    
# data.extend(personer)
    
# with open(filnavn, "w", encoding="utf-8") as fil:
#     json.dump(data, fil, ensure_ascii=False, indent=3)

# print("Data er lagt til")

#Oppgave 2.8.3
filnavn = "C:\Github\IT2\Datasett\Json\p_2_8_3.json"

with open(filnavn, "r", encoding="utf-8") as fil:
    data = json.load(fil)
    
# print(data)
    
# print("\nBilmerker: ")
# for obj in data.keys():
#     print(obj)
    
# #B 
# print("Utvalgt Ford")
# for k,v in data["Ford"][1].items():
#     print(k,": ", v)
    
#C 
for n,v in data.items():
    print(n)
    for k in v:
        for n2,v2 in k.items():
            print(f"{n2}: {v2}")
    print()        

def farge(farge:str)->None:
    for n,v in data.items(): # merker
        for e in v:         # liste med modeller
            if e['farge'].lower()==farge.lower():
                print('\n' + n)
                for n2,v2 in e.items(): 
                    print(f'  {n2:6}: {v2}')
                
farge("Rød")
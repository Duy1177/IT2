# #valgsetninger
# alder = int(input("Skriv inn alder:"))

# # if alder >= 16 and alder <18: 
# #     print("Du kan ta mopedførekort")
# # elif alder >= 18:
# #     print("Du kan ta bilførekort")
# # elif alder > 110:
# #     print("Ugyldig alder")
# # else: 
# #     print("Du kan ikke få førekort")
    
# if alder > 110:
#     print("Ugyldig alder")
# elif alder >=18:
#     print("Du kan ta førekort for bil og moped")
# elif alder >=16:
#     print("Du kan ta førekort for moped")
# else:
#     print("Du kan ikke få førekrot")
    
# #Lete etter "noe" i en string
# interesse = "Chips og VuRderinGsarbeid"
# if "vurdering" in interesse.lower(): #Gjør om til små bokstaver
#     print("Min venn")
# else:
#     print("...")

tall = float(input("Skriv inn et tall: "))

if tall > 0:
    if tall > 100:
        print("Tallet er større enn 100")
    elif tall < 100:
        print("Tallet er minde enn 100")
elif tall < 0:
    if tall > -100:
        print("Tallet er større enn -100")
    elif tall < 100:
        print("Tallet er mindre enn -100")
else:
    print("Tallet er 0")
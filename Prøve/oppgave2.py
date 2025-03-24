import tkinter as tk

temp = 0

def opp(): #Endrer global variabel opp
    global temp  
    temp += 0.5  
    melding = f"Temperatur:\n {temp}"
    temperatur.configure(text=melding)  
    
def ned(): #Endrer global variabel ned
    global temp  
    temp -= 0.5  
    melding = f"Temperatur:\n {temp}"
    temperatur.configure(text=melding)
    
def sett(): #Printer ut temp i label
    global temp
    melding = f"Temperaturen er satt til {temp}°C"
    resultat.configure(text=melding)

root = tk.Tk()

AvPå = tk.Button(root, text="Av/På") #Lager knapp
AvPå.grid(row=0, column=0, rowspan=5, sticky="NS", padx=5, pady=5)

temperatur = tk.Label(root, text=f"Temperatur:\n {temp}", width=10, height=5,  relief="solid", font=("Arial",18)) #Temperatur label
temperatur.grid(row=1, column=1, padx=8, pady=8)

tempOpp = tk.Button(root, text="↑", command=opp, width=5) #Knapp for temperatur opp, og bruker funksjonen opp
tempOpp.grid(row=0, column=2, padx=5, pady=5)

SettTemp = tk.Button(root, text="Sett", height=2, width=5, command= sett) #Knapp for å sette temp
SettTemp.grid(row=1, column=2, rowspan=3, sticky="NS",padx=5, pady=5)

tempNed = tk.Button(root, text="↓", command=ned, width=5) #Knapp for temp ned
tempNed.grid(row=4, column=2, padx=5, pady=5)

resultat = tk.Label(bg='white', text="", borderwidth=2, relief='sunken') #Setter temp på slutten
resultat.grid(row=5,column=0,columnspan=4, sticky="EW", padx=6,pady=6)

root.mainloop()

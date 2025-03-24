import tkinter as tk
import datetime

def convert():
    try:
        km = float(entry1.get())
        fart = float(entry2.get())
    except ValueError:
        melding = "Skriv et heltall eller desimaltall"
        resultat.config(text=melding)
    else: 
        fart_KMt = fart * 1.852
        flytid = km/fart_KMt
        tid = datetime.timedelta(hours=flytid)
        tid = str(tid).split(":")
        melding = f"Time\r: {tid[0]}, Minutter: {tid[1]}, Sekunder: {tid[2]:.2}"
        resultat.config(text=melding)
    
root = tk.Tk()
root.title("Flytid")

overskrift = tk.Label(root, text="Flytider", font="Arial")
overskrift.grid(row=0, column=1, padx=5,pady=5)

label1 = tk.Label(root,text="Avstand i km: ", font="Arial")
label1.grid(row=1,column=1,padx=10,pady=5)

label2 = tk.Label(root,text="Fart i knop: ", font="Arial")
label2.grid(row=2,column=1,padx=10,pady=5)


entry1 = tk.Entry(root, width=10, font="Arial")
entry1.grid(row=1, column=2, padx=5, pady=5)

entry2 = tk.Entry(root, width=10, font="Arial")
entry2.grid(row=2, column=2, padx=5, pady=5)

knapp = tk.Button(root, text="Beregn flytid", command=convert)
knapp.grid(row=3, column=1, columnspan=2, sticky='EW', padx=5)

resultat = tk.Label(bg='white', borderwidth=2, relief='sunken')
resultat.grid(row=4,column=1,columnspan=2, sticky="EW")


root.mainloop()
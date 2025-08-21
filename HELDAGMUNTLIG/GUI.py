import tkinter as tk

root = tk.Tk()

status = False
lys = 100


def avpå():
    global status
    status = not status
    if status:
        melding = "Status: PÅ"
        lysStyrke.configure(text=f"{100}%")

    else: 
        melding = "Status: AV"
        lysStyrke.configure(text=f"{0}%")
    lysStatus.configure(text=melding)

def nedLys():
    global lys
    if lys > 0:
        lys -= 5
        lysStyrke.configure(text=f"{lys}%")
        
def oppLys():
    global lys
    if lys < 100:
        lys += 5
        lysStyrke.configure(text=f"{lys}%")
    
AvPåLys = tk.Button(root, text="Av/På",command=avpå)
AvPåLys.grid(row=0,column=1,padx=5,pady=5)

lysStatus = tk.Label(root, text="Status: AV",relief="solid")
lysStatus.grid(row=1,column=1,columnspan=1,padx=5,pady=5, sticky="EW")

lysStyrke = tk.Label(root, text=f"{lys}%", relief="solid")
lysStyrke.grid(row=2,column=0,columnspan=3, padx=5, pady=5, sticky="EW")

lysNed = tk.Button(root, text="<-", width=10, command=nedLys)
lysNed.grid(row=3,column=0 ,padx=5, pady=5,sticky="EW")

lysOpp = tk.Button(root, text="->",width=10,command=oppLys)
lysOpp.grid(row=3, column=2,padx=5,pady=5,sticky="WE")

root.mainloop()
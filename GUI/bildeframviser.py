import tkinter as tk
from PIL import Image, ImageTk

def vis_bilde():
    bilde = Image.open(bilder[bilde_index])
    bilde = bilde.resize((400,400), Image.Resampling.LANCZOS)
    bilde_tk = ImageTk.PhotoImage(bilde)
    bilde_label.config(image=bilde_tk)
    bilde_label.image = bilde_tk
    
def forrige():
    global bilde_index
    bilde_index -= 1
    if bilde_index < 0:
        bilde_index = len(bilder) - 1
    vis_bilde()
    
def neste():
    global bilde_index
    bilde_index += 1
    if bilde_index >= len(bilder):
        bilde_index = 0
    vis_bilde()

root = tk.Tk()
root.title("Bildeframviser")
root.geometry("600x600")

overskrift = tk.Label(root, text="Bilde leser", font=("Times new roman", 25))
overskrift.grid(row=0, column=0, columnspan= 2,pady = 10)

bilder = ["Bilde1.jpg", "Bilde2.jpg", "Bilde3.jpg"]
bilde_index = 0

bilde = Image.open(bilder[bilde_index])
bilde = bilde.resize((400, 400), Image.Resampling.LANCZOS)
bilde_tk = ImageTk.PhotoImage(bilde)
bilde_label = tk.Label(root, image=bilde_tk)
bilde_label.grid(row=1, column=1, columnspan=2, pady=10, padx=15, sticky="ew")

forrigeKnapp = tk.Button(root,text="Forrige bilde",command=forrige)
forrigeKnapp.grid(row=2, column=0, pady=10)

nesteKnapp = tk.Button(root, text="Neste", command=neste)
nesteKnapp.grid(row=2, column=2,pady=10)

root.mainloop()
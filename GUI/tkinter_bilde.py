import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

def skriv_ut(): 
    hilsen.configure(text=f"Hallo {navn.get()}",)

root = tk.Tk()
# root["bg"] = "pink"


default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size= 20)

root.title("Inndata/Utdata")

bilde = Image.open("C:\Github\IT2\GUI\image.png")
bilde = bilde.resize((200,200), Image.Resampling.LANCZOS)
bilde = ImageTk.PhotoImage(bilde)
tk.Label(root, image=bilde).pack()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

navn = tk.Entry(frame, width=15, font=("Arial 20"))
navn.insert(0, "Hva heter du? ")
navn.pack()

tk.Button(frame, text="Les navn", command=skriv_ut, width=10).pack()

hilsen = tk.Label(root)
hilsen.pack()

root.mainloop()


import tkinter as tk
from tkinter import ttk

data = [["aerobics", "bordtennis", "fotball", "golf", "jogging"],[814,236,510, 244, 666]]

root = tk.Tk()
root.geometry("400x600")

frame = tk.Frame(root)
frame.grid(row=1,column=0, rowspan=1, padx=5,pady=5)


label1 = tk.Label(frame,text="Velg aktivitet: ").grid(row=0,column=0, padx=5, pady=5)

valgtAktivitet = tk.StringVar()
combobox = ttk.Combobox(frame, textvariable=valgtAktivitet, values=data[0], state="readonly", width=15)
combobox.grid(row=0, column=1, columnspan=2,padx=5,pady=5)
combobox.current(0)
combobox.config(height=5)

root.mainloop()

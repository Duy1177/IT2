import tkinter as tk

def til_binært():
    try:
        tall_verdi = int(tall.get())  # Hent verdien fra inntastingsfeltet og konverter til heltall
    except ValueError:
        binært.config(text=f"Ugyldig inndata: '{tall.get()}' er ikke et heltall")
    else:
        binært.config(text=f"{tall_verdi} i binært er {tall_verdi:b}")

root = tk.Tk()
root.title("Tall til binæretall")
root.resizable(0,0)

frame = tk.Frame(root, padx=10, pady=10)
frame.grid(row=1, column=1, padx=5, pady=5)

tall = tk.Entry(frame, width=10, font=("Arial", 20))
tall.insert(0, "Skriv et tall")
tall.grid(row=1, column=1, padx=5, pady=5)

knapp = tk.Button(frame, text="Omgjør til binært", command=til_binært)
knapp.grid(row=2, column=1, padx=5, pady=5)

binært = tk.Label(root, font=("Arial", 15))
binært.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()

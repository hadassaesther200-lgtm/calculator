
# ...existing  code...
import tkinter as tk
from tkinter import messagebox
import calculator

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Erreur", "Entrez des nombres valides.")
        return

    op = operator_var.get()
    try:
        if op == "+":
            res = calculator.add(a, b)
        elif op == "-":
            res = calculator.subtract(a, b)
        elif op == "*":
            res = calculator.multiply(a, b)
        elif op == "/":
            res = calculator.divide(a, b)
        elif op == "//":
            res = calculator.int_divide(a, b)
        elif op == "%":
            res = calculator.modulo(a, b)
        else:
            messagebox.showerror("Erreur", "Opérateur inconnu.")
            return
    except ZeroDivisionError:
        messagebox.showerror("Erreur", "Division par zéro.")
        return

    result_var.set(str(res))

def main():
    global entry_a, entry_b, operator_var, result_var

    root = tk.Tk()
    root.title("Mini calculatrice")
 

    tk.Label(root, text="Nombre A:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_a = tk.Entry(root)
    entry_a.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Nombre B:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_b = tk.Entry(root)
    entry_b.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Opérateur:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    operator_var = tk.StringVar(value="+")
    tk.OptionMenu(root, operator_var, "+", "-", "*", "/", "//", "%").grid(row=2, column=1, padx=5, pady=5, sticky="w")

    tk.Button(root, text="Calculer", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

    result_var = tk.StringVar(value="")
    tk.Label(root, text="Résultat:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    tk.Label(root, textvariable=result_var).grid(row=4, column=1, padx=5, pady=5, sticky="w")

    tk.Button(root, text="Quitter", command=root.destroy).grid(row=5, column=0, columnspan=2, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
# ...existing code...
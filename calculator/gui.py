import tkinter as tk
from tkinter import messagebox
from .calculator import CalculatorEngine
from .constants import *

class CalculatriceApp(tk.Tk):
    """
    Classe principale de l'interface graphique de la calculatrice.
    """
    
    def __init__(self):
        super().__init__()
        self.calculator = CalculatorEngine()
        self.expression = ""
        self.setup_ui()
    
    def setup_ui(self):
        """Configure l'interface utilisateur."""
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_GEOMETRY)
        self.create_widgets()
        self.setup_layout()
    
    def create_widgets(self):
        """Crée tous les widgets de l'interface."""
        # Zone d'affichage
        self.var_resultat = tk.StringVar()
        self.ecran = tk.Entry(
            self,
            textvariable=self.var_resultat,
            font=FONT,
            bd=10,
            insertwidth=2,
            width=20,
            borderwidth=4,
            justify="right"
        )
        
        # Création des boutons
        self.buttons = {}
        for button_config in BUTTONS_LAYOUT:
            text = button_config[0]
            if text == '=':
                cmd = self.calculer
            elif text == 'C':
                cmd = self.effacer
            elif text in '+-*/':
                cmd = lambda x=text: self.ajouter_operateur(x)
            elif text == '.':
                cmd = self.ajouter_virgule
            else:
                cmd = lambda x=text: self.ajouter_chiffre(x)
            
            btn = tk.Button(
                self,
                text=text,
                padx=BUTTON_PADX,
                pady=BUTTON_PADY,
                command=cmd
            )
            
            # Stocker la référence du bouton
            self.buttons[text] = (btn, button_config[1:])
    
    def setup_layout(self):
        """Configure la disposition des widgets."""
        # Positionner la zone d'affichage
        self.ecran.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Positionner les boutons
        for text, (btn, config) in self.buttons.items():
            if len(config) == 4:  # Bouton qui prend plusieurs colonnes
                row, col, rowspan, colspan = config
                btn.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew")
            else:
                row, col = config
                btn.grid(row=row, column=col)
        
        # Configuration du redimensionnement
        for i in range(6):  # 6 lignes
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):  # 4 colonnes
            self.grid_columnconfigure(i, weight=1)
    
    # Méthodes de gestion des événements
    def ajouter_chiffre(self, chiffre):
        """Ajoute un chiffre à l'expression en cours."""
        self.expression += str(chiffre)
        self.var_resultat.set(self.expression)
    
    def ajouter_operateur(self, operateur):
        """Ajoute un opérateur à l'expression."""
        if self.expression and self.expression[-1] not in "+-*/":
            self.expression += operateur
            self.var_resultat.set(self.expression)
    
    def ajouter_virgule(self):
        """Ajoute une virgule décimale."""
        if self.expression and self.expression[-1] not in ".":
            self.expression += "."
            self.var_resultat.set(self.expression)
    
    def effacer(self):
        """Réinitialise la calculatrice."""
        self.expression = ""
        self.var_resultat.set("")
    
    def calculer(self):
        """Évalue l'expression et affiche le résultat."""
        if not self.expression:
            return
            
        try:
            result = self.calculator.evaluate(self.expression)
            self.var_resultat.set(result)
            self.expression = result
        except ZeroDivisionError:
            messagebox.showerror("Erreur", ERROR_DIVISION_BY_ZERO)
            self.effacer()
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))
            self.effacer()
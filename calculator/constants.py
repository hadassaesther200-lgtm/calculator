# Configuration de la fenêtre
WINDOW_TITLE = "Calculatrice"
WINDOW_GEOMETRY = "300x400"

# Configuration de la police
FONT = ('Arial', 16)

# Configuration des boutons
BUTTON_PADX = 20
BUTTON_PADY = 20

# Disposition des boutons
BUTTONS_LAYOUT = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0, 1, 4)  # Le dernier paramètre indique le nombre de colonnes à couvrir
]

# Messages d'erreur
ERROR_INVALID_EXPRESSION = "Expression invalide"
ERROR_DIVISION_BY_ZERO = "Division par zéro"
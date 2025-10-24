
def add(a: float, b: float) -> float:
    """Retourne a + b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Retourne a - b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Retourne a * b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Retourne a / b. Lève ZeroDivisionError si b == 0."""
    if b == 0:
        raise ZeroDivisionError("Division par zéro")
    return a / b

def int_divide(a: float, b: float) -> float:
    """Retourne a // b (division entière)."""
    if b == 0:
        raise ZeroDivisionError("Division par zéro")
    return a // b

def modulo(a: float, b: float) -> float:
    """Retourne a % b."""
    if b == 0:
        raise ZeroDivisionError("Division par zéro")
    return a % b
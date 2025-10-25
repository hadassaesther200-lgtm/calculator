class CalculatorEngine:
    """Gère la logique métier des calculs"""
    
    @staticmethod
    def evaluate(expression):
        """
        Évalue une expression mathématique.
        
        Args:
            expression (str): Expression mathématique à évaluer
            
        Returns:
            str: Le résultat du calcul
            
        Raises:
            Exception: Si l'expression est invalide
        """
        try:
            return str(eval(expression, {"__builtins__": None}, {}))
        except Exception as e:
            raise ValueError("Expression invalide") from e
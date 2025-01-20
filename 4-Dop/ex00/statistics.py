# statistics.py

import sys
from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    # Limite l'affichage des traces d'erreur
    sys.tracebacklimit = 0

    try:
        # Vérifie si args est vide ou ne contient pas de nombres
        if not args or not all(isinstance(x, (int, float)) for x in args):
            raise ValueError("ERROR")

        # Trie les arguments pour faciliter les calculs
        sorted_args = sorted(args)
        n = len(sorted_args)

        # Calcul de la moyenne
        mean = sum(sorted_args) / n

        # Calcul de la médiane
        if n % 2 == 1:
            median = sorted_args[n // 2]
        else:
            median = (sorted_args[n // 2 - 1] + sorted_args[n // 2]) / 2

        # Calcul des quartiles (Q1 et Q3)
        def get_quartile(data, percentile):
            index = (len(data) - 1) * percentile / 100
            lower = data[int(index)]
            upper = data[int(index) + 1]
            return lower + (upper - lower) * (index - int(index))

        quartile = [
            get_quartile(sorted_args, 25),
            get_quartile(sorted_args, 75),
        ]

        # Calcul de la variance
        variance = sum((x - mean) ** 2 for x in sorted_args) / n

        # Calcul de l'écart-type (sans utiliser sqrt)
        def sqrt_manual(x):
            # Méthode de Newton pour calculer la racine carrée
            if x == 0:
                return 0
            guess = x / 2
            while True:
                new_guess = (guess + x / guess) / 2
                if abs(new_guess - guess) < 1e-10:
                    return new_guess
                guess = new_guess

        std = sqrt_manual(variance)

        # Affiche les statistiques demandées dans kwargs
        for _, value in kwargs.items():
            if value == "mean":
                print(f"mean : {mean}")
            elif value == "median":
                print(f"median : {median}")
            elif value == "quartile":
                print(f"quartile : {quartile}")
            elif value == "std":
                print(f"std : {std}")
            elif value == "var":
                print(f"var : {variance}")

    except Exception:
        # Affiche "ERROR" pour chaque clé dans kwargs en cas d'erreur
        for _ in kwargs:
            print("ERROR")

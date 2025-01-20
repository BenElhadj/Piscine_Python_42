# callLimit.py


def callLimit(limit: int):
    """
    Décorateur qui limite le nombre d'appels d'une fonction.
    """

    def callLimiter(function):
        """
        Closure qui enveloppe la fonction et compte le nombre d'appels.
        """
        count = 0  # Compteur d'appels

        def limit_function(*args, **kwargs):
            """
            Fonction qui vérifie si la limite d'appels est atteinte.
            """
            nonlocal count  # Permet de modifier `count` de la fonction parente
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function.__name__} call too many times")

        return limit_function

    return callLimiter

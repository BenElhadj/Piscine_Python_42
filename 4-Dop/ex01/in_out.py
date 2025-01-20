# in_out.py


def square(x: int | float) -> int | float:
    """
    Retourne le carré de x.
    """
    return x**2


def pow(x: int | float) -> int | float:
    """
    Retourne x élevé à la puissance de lui-même (x^x).
    """
    return x**x


def outer(x: int | float, function) -> object:
    """
    Retourne une closure qui applique
    `function` à `x`
    et garde une trace du nombre d'appels.
    """
    count = 0

    def inner() -> float:
        """
        Applique `function` à `x` et retourne le résultat.
        Incrémente le compteur d'appels à chaque invocation.
        """
        nonlocal count  # Permet de modifier `count` de la fonction parente
        result = function(x)
        count += 1
        return result

    return inner

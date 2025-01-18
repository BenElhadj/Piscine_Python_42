# array2D.py

import sys


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array (list of lists) and return the truncated version.

    Args:
        family (list): A 2D array (list of lists).
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.

    Returns:
        list: The truncated 2D array.

    Raises:
        TypeError: If family is not a list or contains non-list elements.
        ValueError: If the 2D array is irregular (rows of different lengths).
        IndexError: If the start or end indices are out of bounds.
    """
    try:
        # Vérifier que family est une liste
        if not isinstance(family, list):
            raise TypeError("TypeError: family must be a list.")

        # Vérifier que chaque élément de family est une liste
        if not all(isinstance(row, list) for row in family):
            raise TypeError("TypeError: family must be a list of lists.")

        # Vérifier que toutes les lignes ont la même longueur
        if len(family) > 0:
            row_length = len(family[0])
            if not all(len(row) == row_length for row in family):
                raise ValueError(
                    "ValueError: The 2D array must be regular \
(all rows must have the same length)."
                )

        # Vérifier que les indices de slicing sont valides
        if start < 0 or end > len(family):
            raise IndexError(
                "IndexError: Invalid slicing indices:\
start and end must be within bounds."
            )

        # Afficher la forme originale du tableau
        original_shape = (len(family), len(family[0]) if family else 0)
        print(f"My shape is : {original_shape}")

        # Tronquer le tableau en utilisant le slicing
        truncated_family = family[start:end]

        # Afficher la nouvelle forme du tableau
        new_shape = (
            len(truncated_family),
            len(truncated_family[0]) if truncated_family else 0,
        )
        print(f"My new shape is : {new_shape}")

        return truncated_family

    except (TypeError, ValueError, IndexError):
        # Désactiver le traceback pour afficher uniquement le message d'erreur
        sys.tracebacklimit = 0
        raise  # Relancer l'exception pour qu'elle soit propagée


def main():
    """
    Main function to test the slice_me function.
    """
    family = [[1.80, 78.4], ["Hi", 102.7], [2.10, 98.5], [1.68, 75.2]]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()

# array2D.py

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
    """
    # Vérifier que family est une liste
    if not isinstance(family, list):
        raise TypeError("family doit être une liste.")
    
    # Vérifier que chaque élément de family est une liste
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family doit être une liste de listes.")
    
    # Vérifier que toutes les lignes ont la même longueur (tableau régulier)
    if len(family) > 0:
        row_length = len(family[0])
        if not all(len(row) == row_length for row in family):
            raise ValueError("Le tableau 2D doit être régulier (toutes les lignes doivent avoir la même longueur).")
    
    # Afficher la forme originale du tableau
    original_shape = (len(family), len(family[0]) if family else 0)
    print(f"My shape is : {original_shape}")
    
    # Tronquer le tableau en utilisant le slicing
    truncated_family = family[start:end]
    
    # Afficher la nouvelle forme du tableau
    new_shape = (len(truncated_family), len(truncated_family[0]) if truncated_family else 0)
    print(f"My new shape is : {new_shape}")
    
    return truncated_family

def main():
    """
    Main function to test the slice_me function.
    """
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.68, 75.2]
    ]

    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
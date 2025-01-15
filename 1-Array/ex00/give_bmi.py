# give_bmi.py

import sys


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[float]:
    """
    Calculate the BMI (Body Mass Index) for given heights and weights.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[float]: List of BMI values.

    Raises:
        ValueError: If the height and weight lists are not of
        the same size or if they are empty.
        TypeError: If the elements of height or weight are not int or float.
    """
    try:
        if len(height) == 0 or len(weight) == 0:
            raise ValueError(
                "ValueError: height and weight lists cannot be empty."
            )

        if len(height) != len(weight):
            raise ValueError(
                "ValueError: height and weight lists must be of the same size."
            )

        if not all(isinstance(h, (int, float)) for h in height):
            raise TypeError("TypeError: height elements must be int or float.")
        if not all(isinstance(w, (int, float)) for w in weight):
            raise TypeError("TypeError: weight elements must be int or float.")

        bmi_list = []
        for h, w in zip(height, weight):
            bmi = w / (h**2)
            bmi_list.append(bmi)

        return bmi_list
    except (ValueError, TypeError):
        # Désactiver le traceback pour afficher uniquement le message d'erreur
        sys.tracebacklimit = 0
        raise  # Relancer l'exception pour qu'elle soit propagée


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to BMI values and return a list of booleans
    indicating if each BMI is above the limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): The limit to compare BMI values against.

    Returns:
        list[bool]: List of booleans (True if BMI > limit, False otherwise).

    Raises:
        TypeError: If the elements of bmi are not int or float.
    """
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("TypeError: bmi elements must be int or float.")

    return [b > limit for b in bmi]


def main():
    """
    Main function to test the give_bmi and apply_limit functions.
    """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

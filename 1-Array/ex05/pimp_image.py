# pimp_image.py

import sys
import numpy as np
from matplotlib import pyplot as plt  # type: ignore
from load_image import ft_load


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert the colors of the image.

    Args:
        array (np.ndarray): The image as a NumPy array.

    Returns:
        np.ndarray: The image with inverted colors.
    """
    # Utilisation des opérateurs autorisés : =, +, -, *
    inverted_array = 255 - array
    # Afficher les images transformées
    display_image(array, "Original Image")
    display_image(inverted_array, "Inverted Image")
    return inverted_array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Apply a red filter to the image.

    Args:
        array (np.ndarray): The image as a NumPy array.

    Returns:
        np.ndarray: The image with a red filter.
    """
    # Utilisation des opérateurs autorisés : =, *
    red_array = array.copy()
    red_array[:, :, 1] = red_array[:, :, 1] * 0
    red_array[:, :, 2] = red_array[:, :, 2] * 0
    # Afficher l'image transformée
    display_image(red_array, "Red Filter")
    return red_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Apply a green filter to the image.

    Args:
        array (np.ndarray): The image as a NumPy array.

    Returns:
        np.ndarray: The image with a green filter.
    """
    # Utilisation des opérateurs autorisés : =, -
    green_array = array.copy()
    green_array[:, :, 0] = green_array[:, :, 0] - green_array[:, :, 0]
    green_array[:, :, 2] = green_array[:, :, 2] - green_array[:, :, 2]
    # Afficher l'image transformée
    display_image(green_array, "Green Filter")
    return green_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Apply a blue filter to the image.

    Args:
        array (np.ndarray): The image as a NumPy array.

    Returns:
        np.ndarray: The image with a blue filter.
    """
    # Utilisation des opérateurs autorisés : =
    blue_array = array.copy()
    blue_array[:, :, 0] = 0
    blue_array[:, :, 1] = 0
    # Afficher l'image transformée
    display_image(blue_array, "Blue Filter")
    return blue_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert the image to grayscale.

    Args:
        array (np.ndarray): The image as a NumPy array.

    Returns:
        np.ndarray: The grayscale image.
    """
    # Utilisation des opérateurs autorisés : =, /
    # Calcul de la moyenne manuellement (R + G + B) / 3

    # grey_array = (
    #     array[:, :, 0] / 3 + array[:, :, 1] / 3 + array[:, :, 2] / 3
    # )  # Utilisation de / et =

    # grey_array = np.sum(array[:, :, :3] / 3, axis=2)
    # grey_array = np.add(np.add(array[:, :, 0] / 3, array[:, :, 1] / 3),
    #                     array[:, :, 2] / 3)

    grey_array = array[:, :, 0] / 1.33
    grey_array = array[:, :, 1] / 1.33
    grey_array = array[:, :, 2] / 1.33

    # Créer un tableau vide pour stocker l'image en gris avec 3 canaux
    grey_image = np.zeros_like(array)

    # Répéter la valeur du gris sur les 3 canaux manuellement
    grey_image[:, :, 0] = grey_array  # Canal rouge
    grey_image[:, :, 1] = grey_array  # Canal vert
    grey_image[:, :, 2] = grey_array  # Canal bleu

    # Afficher l'image transformée
    display_image(grey_image, "Grayscale Image")
    return grey_image


def display_image(array: np.ndarray, title: str):
    """
    Display the image with a title.

    Args:
        array (np.ndarray): The image to display.
        title (str): The title of the image.
    """
    # Afficher l'image
    plt.imshow(array)
    plt.title(title)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()


def main():
    """
    Main function to load the image, apply filters, and display the results.
    """
    try:
        # Charger l'image
        array = ft_load("landscape.jpg")
        # Appliquer les filtres
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)

    except Exception as e:
        sys.tracebacklimit = 0
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

# pimp_image.py

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
    inverted_array = 255 - array
    # Normaliser
    inverted_array = np.clip(inverted_array, 0, 255).astype(np.uint8)
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
    red_array = array.copy()
    red_array[:, :, 1] = 0  # Supprimer le vert
    red_array[:, :, 2] = 0  # Supprimer le bleu
    # Normaliser
    red_array = np.clip(red_array, 0, 255).astype(np.uint8)
    # Afficher l'images transformée
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
    green_array = array.copy()
    green_array[:, :, 0] = 0  # Supprimer le rouge
    green_array[:, :, 2] = 0  # Supprimer le bleu
    # Normaliser
    green_array = np.clip(green_array, 0, 255).astype(np.uint8)
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
    blue_array = array.copy()
    blue_array[:, :, 0] = 0  # Supprimer le rouge
    blue_array[:, :, 1] = 0  # Supprimer le vert
    # Normaliser
    blue_array = np.clip(blue_array, 0, 255).astype(np.uint8)
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
    grey_array = np.mean(array, axis=2, keepdims=True)
    grey_array = np.repeat(grey_array, 3, axis=2)
    # Normaliser
    grey_array = np.clip(grey_array, 0, 255).astype(np.uint8)
    # Afficher l'image transformée
    display_image(grey_array, "Grayscale Image")
    return grey_array


def display_image(array: np.ndarray, title: str):
    """
    Display the image with a title.

    Args:
        array (np.ndarray): The image to display.
        title (str): The title of the image.
    """
    # Normaliser pour les flottants
    if array.dtype != np.uint8:
        array = np.clip(array, 0, 1.0)
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
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

# pimp_image.py

import numpy as np
from matplotlib import pyplot as plt # type: ignore
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
    return grey_array

def display_image(array: np.ndarray, title: str):
    """
    Display the image with a title.

    Args:
        array (np.ndarray): The image to display.
        title (str): The title of the image.
    """
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
        inverted_array = ft_invert(array)
        red_array = ft_red(array)
        green_array = ft_green(array)
        blue_array = ft_blue(array)
        grey_array = ft_grey(array)
        
        # Afficher les images transformées
        display_image(array, "Original Image")
        display_image(inverted_array, "Inverted Image")
        display_image(red_array, "Red Filter")
        display_image(green_array, "Green Filter")
        display_image(blue_array, "Blue Filter")
        display_image(grey_array, "Grayscale Image")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
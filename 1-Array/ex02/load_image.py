# load_image.py

import sys
import numpy as np
from matplotlib import pyplot as plt  # type: ignore


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified path and return it as a NumPy array.

    Args:
        path (str): The path to the image file.

    Returns:
        np.ndarray: The image as a NumPy array.

    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the image format is not supported or
        the image is corrupted.
    """
    try:
        # Charger l'image avec matplotlib
        image = plt.imread(path)

        # Afficher le contenu des pixels
        print(f"The shape of image is: {image.shape}")
        print(image)

        return image
    except (FileNotFoundError, Exception):
        sys.tracebacklimit = 0
        raise


def main():
    """
    Main function to test the ft_load function.
    """
    try:
        # Charger l'image
        ft_load("landscape.jpg")
    except Exception as e:
        sys.tracebacklimit = 0
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

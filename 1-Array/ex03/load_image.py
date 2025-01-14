# load_image.py

import numpy as np
from matplotlib import pyplot as plt


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified path and return it as a NumPy array.

    Args:
        path (str): The path to the image file.

    Returns:
        np.ndarray: The image as a NumPy array.

    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the image format is not supported.
    """
    try:
        # Charger l'image avec matplotlib
        image = plt.imread(path)
        print(f"The shape of image is: {image.shape}")
        print(image)
        return image
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{path}' does not exist.")
    except Exception as e:
        raise ValueError(f"Error: Unable to load the image. {e}")

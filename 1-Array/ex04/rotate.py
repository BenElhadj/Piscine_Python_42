# rotate.py

import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def crop_image(image: np.ndarray, size: int) -> np.ndarray:
    """
    Crop a square part from the center of the image.

    Args:
        image (np.ndarray): The image as a NumPy array.
        size (int): The size of the square to crop.

    Returns:
        np.ndarray: The cropped image.

    Raises:
        ValueError: If the image is too small to be cropped.
    """
    height, width, _ = image.shape
    if size > min(height, width):
        err = "The image is too small to be cropped to the specified size."
        raise ValueError(f"Error: {err}")

    start_x = (width - size) // 2
    start_y = (height - size) // 2
    cropped_image = image[start_y: start_y + size, start_x: start_x + size]
    return cropped_image


def rotate_image(image: np.ndarray) -> np.ndarray:
    """
    Rotate the image 90 degrees counterclockwise and apply a mirror effect.

    Args:
        image (np.ndarray): The image as a NumPy array.

    Returns:
        np.ndarray: The rotated and mirrored image.
    """
    # Rotation manuelle de 90 degrés dans le sens inverse de la montre
    rotated_image = np.zeros(
        (image.shape[1], image.shape[0], image.shape[2]), dtype=image.dtype
    )
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rotated_image[image.shape[1] - j - 1, i] = image[i, j]

    # Appliquer un effet miroir (symétrie horizontale)
    mirrored_image = rotated_image[::-1, :, :]

    return mirrored_image, rotated_image


def display_image(image: np.ndarray, title: str):
    """
    Display the image with a title.

    Args:
        image (np.ndarray): The image to display.
        title (str): The title of the image.
    """
    plt.imshow(image)
    plt.title(title)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()


def main():
    """
    Main function to load the image, crop it, rotate it, and display it.
    """
    try:
        # Charger l'image
        image = ft_load("animal.jpeg")

        # Couper une partie carrée de l'image
        cropped_image = crop_image(image, 400)
        print(f"New shape after cropping: {cropped_image.shape}")
        print(cropped_image)

        # Effectuer la rotation et l'effet miroir
        # mirrored_image, rotated_image = rotate_image(cropped_image)
        _, rotated_image = rotate_image(cropped_image)
        print(f"New shape after rotating: {rotated_image.shape}")
        print(rotated_image)

        # Afficher l'image transformée
        # display_image(mirrored_image, "mirrored Image")
        display_image(rotated_image, "Rotated and Mirrored Image")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

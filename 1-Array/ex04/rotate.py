# rotate.py

import numpy as np
from matplotlib import pyplot as plt # type: ignore
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
        raise ValueError("Error: The image is too small to be cropped to the specified size.")
    
    start_x = (width - size) // 2
    start_y = (height - size) // 2
    cropped_image = image[start_y:start_y + size, start_x:start_x + size]
    return cropped_image

def transpose_image(image: np.ndarray) -> np.ndarray:
    """
    Transpose the image (swap rows and columns).

    Args:
        image (np.ndarray): The image as a NumPy array.

    Returns:
        np.ndarray: The transposed image.
    """
    transposed_image = np.transpose(image, (1, 0, 2))
    return transposed_image

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
    Main function to load the image, crop it, transpose it, and display it.
    """
    try:
        # Charger l'image
        image = ft_load("animal.jpeg")
        
        # Couper une partie carrée de l'image
        cropped_image = crop_image(image, 400)
        print(f"New shape after cropping: {cropped_image.shape}")
        print(cropped_image)
        
        # Transposer l'image
        transposed_image = transpose_image(cropped_image)
        print(f"New shape after transposing: {transposed_image.shape}")
        print(transposed_image)
        
        # Afficher l'image transposée
        display_image(transposed_image, "Transposed Image")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
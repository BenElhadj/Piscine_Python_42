# zoom.py

import numpy as np
from matplotlib import pyplot as plt # type: ignore
from load_image import ft_load

def zoom_image(image: np.ndarray, zoom_area: tuple) -> np.ndarray:
    """
    Zoom on a specific area of the image.

    Args:
        image (np.ndarray): The image as a NumPy array.
        zoom_area (tuple): The area to zoom (start_x, start_y, end_x, end_y).

    Returns:
        np.ndarray: The zoomed image.
    """
    start_x, start_y, end_x, end_y = zoom_area
    zoomed_image = image[start_y:end_y, start_x:end_x]
    print(f"New shape after slicing: {zoomed_image.shape}")
    print(zoomed_image)
    return zoomed_image

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
    Main function to load the image, zoom on a specific area, and display it.
    """
    try:
        # Charger l'image
        image = ft_load("animal.jpeg")
        
        # Définir la zone à zoomer (par exemple, un carré au centre de l'image)
        height, width, _ = image.shape
        start_x = width // 4
        start_y = height // 4
        end_x = start_x + 400
        end_y = start_y + 400
        zoom_area = (start_x, start_y, end_x, end_y)
        
        # Effectuer le zoom
        zoomed_image = zoom_image(image, zoom_area)
        
        # Afficher l'image zoomée
        display_image(zoomed_image, "Zoomed Image")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
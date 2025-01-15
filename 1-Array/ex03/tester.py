# tester.py

from load_image import ft_load
from zoom import zoom_image

# Test normal
print("_" * 50, "\nTest normal:")
try:
    image = ft_load("animal.jpeg")
    zoom_area = (256, 192, 656, 592)  # Exemple de zone de zoom
    zoomed_image = zoom_image(image, zoom_area)
except Exception as e:
    print(e)

# Test avec un chemin incorrect
print("_" * 50, "\nTest avec un chemin incorrect:")
try:
    image = ft_load("nonexistent.jpeg")
    zoom_area = (256, 192, 656, 592)
    zoomed_image = zoom_image(image, zoom_area)
except Exception as e:
    print(e)

# Test avec une zone de zoom invalide
print("_" * 50, "\nTest avec une zone de zoom invalide:")
try:
    image = ft_load("animal.jpeg")
    zoom_area = (1000, 1000, 2000, 2000)  # Zone de zoom invalide
    zoomed_image = zoom_image(image, zoom_area)
except Exception as e:
    print(e)

"""
    python .\tester.py
    __________________________________________________
    Test normal:
    The shape of image is: (768, 1024, 3)
    [[[120 111 132]
    [139 130 151]
    [155 146 167]
    ...
    ...
    [120 156  94]
    [119 154  90]
    [118 153  89]]]
    New shape after slicing: (400, 400, 1) or (400, 400)
    [[[148]
    [170]
    [179]
    ...
    ...
    [ 13]
    [ 12]
    [ 14]]]
    __________________________________________________
    Test avec un chemin incorrect:
    FileNotFoundError: The file 'nonexistent.jpeg' does not exist.
    __________________________________________________
    Test avec une zone de zoom invalide:
    The shape of image is: (768, 1024, 3)
    [[[120 111 132]
    [139 130 151]
    [155 146 167]
    ...
    ...
    [120 156  94]
    [119 154  90]
    [118 153  89]]]
    ValueError: Invalid zoom area.
"""

# tesster.py

from load_image import ft_load
from rotate import rotate_image, crop_image

# Test normal
print("_" * 50, "\nTest normal")
try:
    image = ft_load("animal.jpeg")
    cropped_image = crop_image(image, 400)
    rotated_image = rotate_image(
        cropped_image
    )  # Maintenant, rotated_image est une seule image
    print(f"New shape after rotating: {rotated_image.shape}")
    print(rotated_image)
except Exception as e:
    print(e)

# Test avec un chemin incorrect
print("_" * 50, "\nTest avec un chemin incorrect")
try:
    image = ft_load("nonexistent.jpeg")
    cropped_image = crop_image(image, 400)
    rotated_image = rotate_image(cropped_image)
    print(f"New shape after rotating: {rotated_image.shape}")
    print(rotated_image)
except Exception as e:
    print(e)

# Test avec une image trop petite
print("_" * 50, "\nTest avec une image trop petite")
try:
    image = ft_load("small_image.jpeg")
    cropped_image = crop_image(image, 400)
    rotated_image = rotate_image(cropped_image)
    print(f"New shape after rotating: {rotated_image.shape}")
    print(rotated_image)
except Exception as e:
    print(e)

"""
    python tester.py
    __________________________________________________
    Test normal
    The shape of image is: (768, 1024, 3)
    [[[120 111 132]
    [139 130 151]
    [155 146 167]
    ...
    ...
    [120 156  94]
    [119 154  90]
    [118 153  89]]]
    New shape after rotating: (400, 400, 3)
    [[[ 89  79  88]
    [ 84  74  82]
    [109  98 106]
    ...
    ...
    [ 73  95  56]
    [ 70  92  53]
    [ 65  86  47]]]
    __________________________________________________
    Test avec un chemin incorrect
    FileNotFoundError: The file 'nonexistent.jpeg' does not exist.
    __________________________________________________
    Test avec une image trop petite
    The shape of image is: (34, 26, 3)
    [[[ 72  61  59]
    [155 143 143]
    [152 142 143]
    ...
    ...
    [ 96 138  56]
    [102 141  60]
    [102 141  58]]]
    ValueError: The image is too small to be cropped to the specified size.
"""

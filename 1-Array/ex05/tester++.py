# tester.py

from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

# Test normal
print("_" * 50, "\nTest normal")
try:
    array = ft_load("landscape.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
except Exception as e:
    print(e)

# Test avec un chemin incorrect
print("_" * 50, "\nTest avec un chemin incorrect")
try:
    array = ft_load("nonexistent.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
except Exception as e:
    print(e)

# Test avec une image corrompue
print("_" * 50, "\nTest avec une image corrompue")
try:
    array = ft_load("corrupted.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
except Exception as e:
    print(e)

"""
    python tester.py
    __________________________________________________
    Test normal
    The shape of image is: (257, 450, 3)
    [[[19 42 83]
    [23 42 84]
    [28 43 84]
    ...
    ...
    [ 0  0  0]
    [ 1  1  1]
    [ 1  1  1]]]
    __________________________________________________
    Test avec un chemin incorrect
    FileNotFoundError: The file 'nonexistent.jpg' does not exist.
    __________________________________________________
    Test avec une image corrompue
    ValueError: Unable to load the image.
        cannot identify image file 'corrupted.jpg'
"""

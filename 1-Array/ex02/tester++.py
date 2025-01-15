# tester.py

from load_image import ft_load

# Test normal
print("_" * 50, "\nTest normal:")
try:
    print(ft_load("landscape.jpg"))
except Exception as e:
    print(e)

# Test avec un chemin incorrect
print("_" * 50, "\nTest avec un chemin incorrect:")
try:
    print(ft_load("nonexistent.jpg"))
except Exception as e:
    print(e)

# Test avec une image corrompue
print("_" * 50, "\nTest avec une image corrompue:")
try:
    print(ft_load("corrupted.jpg"))
except Exception as e:
    print(e)

"""
    python tester++.py
    __________________________________________________
    Test normal:
    The shape of image is: (257, 450, 3)
    [[[19 42 83]
    [23 42 84]
    [28 43 84]
    ...
    [69 42 51]
    [68 41 46]
    [68 41 46]]

    [[20 43 84]
    [24 43 85]
    [28 43 84]
    ...
    ...
    [ 0  0  0]
    [ 1  1  1]
    [ 1  1  1]]]
    __________________________________________________
    Test avec un chemin incorrect:
    FileNotFoundError: The file 'nonexistent.jpg' does not exist.
    __________________________________________________
    Test avec une image corrompue:
    ValueError: Unable to load the image. cannot identify image file
    'corrupted.jpg'
"""

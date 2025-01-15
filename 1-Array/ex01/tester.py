from array2D import slice_me

family = [[2.10, 78.45], [4.15, 6.70], [2.10, 98.5], [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

"""
    $> python tester.py
    My shape is : (4, 2)
    My new shape is : (2, 2)
    [[2.1, 78.45], [4.15, 6.7]]
    My shape is : (4, 2)
    My new shape is : (1, 2)
    [[4.15, 6.7]]
"""

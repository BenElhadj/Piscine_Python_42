# tester++.py

from array2D import slice_me

# Test normal
print("Test normal\n______________________________")
family = [[2.10, 78.45], [4.15, 6.70], [2.10, 98.5], [1.88, 75.2]]

try:
    print(slice_me(family, 0, 2))
except Exception as e:
    print(e)

try:
    print(slice_me(family, 1, -2))
except Exception as e:
    print(e)

# Test avec un tableau irrégulier
print("_" * 50, "\nTest avec un tableau irrégulier")
irregular_family = [[2.10, 78.45], [4.15], [2.10, 98.5], [1.88, 75.2]]
try:
    print(slice_me(irregular_family, 0, 2))
except Exception as e:
    print(e)

# Test avec un type incorrect pour family
print("_" * 50, "\nTest avec un type incorrect pour family")
not_a_list = "not a list"
try:
    print(slice_me(not_a_list, 0, 2))
except Exception as e:
    print(e)

# Test avec des éléments non-listes dans family
print("_" * 50, "\nTest avec des éléments non-listes dans family")
not_a_list_of_lists = [[2.10, 78.45], "not a list", [2.10, 98.5], [1.88, 75.2]]
try:
    print(slice_me(not_a_list_of_lists, 0, 2))
except Exception as e:
    print(e)

# Test avec des indices de slicing invalides
print("_" * 50, "\nTest avec des indices de slicing invalides")
family = [[2.10, 78.45], [4.15, 6.70], [2.10, 98.5], [1.88, 75.2]]
try:
    print(slice_me(family, 10, 20))  # Indices hors limites
except Exception as e:
    print(e)


"""
    python tester++.py
    Test normal
    ______________________________
    My shape is : (4, 2)
    My new shape is : (2, 2)
    [[2.1, 78.45], [4.15, 6.7]]
    My shape is : (4, 2)
    My new shape is : (1, 2)
    [[4.15, 6.7]]
    __________________________________________________
    Test avec un tableau irrégulier
    ValueError:The 2D array must be regular(all rows must have the same length)
    __________________________________________________
    Test avec un type incorrect pour family
    TypeError: family must be a list.
    __________________________________________________
    Test avec des éléments non-listes dans family
    TypeError: family must be a list of lists.
    __________________________________________________
    Test avec des indices de slicing invalides
    IndexError: Invalid slicing indices:start and end must be within bounds.
"""

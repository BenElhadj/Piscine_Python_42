# tester++.py

from give_bmi import give_bmi, apply_limit

# Test normal
print("_" * 50, "\nTest normal:")
height = [1.71, 1.65, 1.73, 1.95, 1.63]
weight = [65.3, 58.4, 63.4, 94.5, 72.9]

try:
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
except Exception as e:
    print(e)

# Test avec des listes de tailles différentes
print("_" * 50, "\nTest avec des listes de tailles différentes:")
height = [1.71, 1.65]
weight = [65.3, 58.4, 63.4]
try:
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
except Exception as e:
    print(e)

# Test avec des chaînes de caractères dans les listes
print("_" * 50, "\nTest avec des chaînes de caractères dans les listes:")
height = [1.71, "1.65"]
weight = [65.3, 58.4]
try:
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
except Exception as e:
    print(e)


# Test avec des listes vides
print("_" * 50, "\nTest avec des listes vides:")
height = []
weight = []
try:
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
except Exception as e:
    print(e)


# Test avec des éléments non numériques dans bmi
print("_" * 50, "\nTest avec des éléments non numériques dans bmi:")
try:
    bmi = [22.33, "21.45"]
    print(apply_limit(bmi, 26))
except Exception as e:
    print(e)


"""
    python tester++.py
    __________________________________________________
    Test normal:
    [22.33165760404911, 21.45087235996327, 21.183467539844298,
    24.85207100591716, 27.43799164439761] <class 'list'>
    [False, False, False, False, True]
    __________________________________________________
    Test avec des listes de tailles différentes:
    ValueError: height and weight lists must be of the same size.
    __________________________________________________
    Test avec des chaînes de caractères dans les listes:
    TypeError: height elements must be int or float.
    __________________________________________________
    Test avec des listes vides:
    ValueError: height and weight lists cannot be empty.
    __________________________________________________
    Test avec des éléments non numériques dans bmi:
    TypeError: bmi elements must be int or float.
"""

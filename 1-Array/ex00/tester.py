# tester++.py

from give_bmi import give_bmi, apply_limit

height = [1.71, 1.65, 1.73, 1.95, 1.63]
weight = [65.3, 58.4, 63.4, 94.5, 72.9]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

"""
    $> python tester.py
    [22.33165760404911, 21.45087235996327, 21.183467539844298,
    24.85207100591716, 27.43799164439761] <class 'list'>
    [False, False, False, False, True]
"""

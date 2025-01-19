# tester.py

from ft_calculator import calculator

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5  # [5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5  # [0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5  # [5.0, 10.0, 15.0]
v3 / 5  # [1.0, 2.0, 3.0]

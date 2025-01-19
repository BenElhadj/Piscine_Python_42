# ft_calculator.py
# import sys

# sys.tracebacklimit = 0


class calculator:
    """
    Class for calculator:
    Class representing a calculator for vector operations.
    """

    def __init__(self, vector):
        """
        Constructor for calculator:
        Initialize a calculator with a vector.
        """
        self.vector = vector

    def __add__(self, scalar):
        """
        Method for calculator:
        Add a scalar to each element of the vector.
        """
        result = [x + scalar for x in self.vector]
        print(result)
        return calculator(result)

    def __mul__(self, scalar):
        """
        Method for calculator:
        Multiply each element of the vector by a scalar.
        """
        result = [x * scalar for x in self.vector]
        print(result)
        return calculator(result)

    def __sub__(self, scalar):
        """
        Method for calculator:
        Subtract a scalar from each element of the vector.
        """
        result = [x - scalar for x in self.vector]
        print(result)
        return calculator(result)

    def __truediv__(self, scalar):
        """
        Method for calculator:
        Divide each element of the vector by a scalar.
        """
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = [x / scalar for x in self.vector]
        print(result)
        return calculator(result)

    def __str__(self):
        """
        Method for calculator:
        Return a string representation of the vector.
        """
        return str(self.vector)

    def __repr__(self):
        """
        Method for calculator:
        Return a formal string representation of the vector.
        """
        return self.__str__()

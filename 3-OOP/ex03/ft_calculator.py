# ft_calculator.py


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
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)

    def __mul__(self, scalar):
        """
        Method for calculator:
        Multiply each element of the vector by a scalar.
        """
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)

    def __sub__(self, scalar):
        """
        Method for calculator:
        Subtract a scalar from each element of the vector.
        """
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)

    def __truediv__(self, scalar):
        """
        Method for calculator:
        Divide each element of the vector by a scalar.
        """
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)

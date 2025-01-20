# ft_calculator.py


class calculator:
    """
    Class for calculator:
    Class representing a calculator for vector operations.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Method for calculator:
        Calculate the dot product of two vectors.
        """
        result = sum(float(x * y) for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Method for calculator: Add two vectors element-wise."""
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Method for calculator:
        Subtract two vectors element-wise.
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")

# S1E7.py

from S1E9 import Character


class Baratheon(Character):
    """Class for Baratheon: Class representing a Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Baratheon: Initialize a Baratheon family."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Method for Baratheon: Kill the Baratheon family."""
        self.is_alive = False

    def __str__(self):
        """
        Method for Baratheon:
        Return a string representation of the Baratheon family.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Method for Baratheon:
        Return a formal string representation of the Baratheon family.
        """
        return self.__str__()


class Lannister(Character):
    """Class for Lannister: Class representing a Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Lannister: Initialize a Lannister family."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Method for Lannister: Kill the Lannister family."""
        self.is_alive = False

    def __str__(self):
        """
        Method for Lannister:
        Return a string representation of the Lannister family.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Method for Lannister:
        Return a formal string representation of the Lannister family.
        """
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Method for Lannister: Create a Lannister family."""
        return cls(first_name, is_alive)

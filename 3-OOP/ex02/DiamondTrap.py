# DiamondTrap.py

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class for King: Class representing a King family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for King: Initialize a King family."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    @property
    def eyes(self):
        """Getter for eyes: Get the eye color of the King."""
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        """Setter for eyes: Set the eye color of the King."""
        self._eyes = value

    @property
    def hairs(self):
        """Getter for hairs: Get the hair color of the King."""
        return self._hairs

    @hairs.setter
    def hairs(self, value):
        """Setter for hairs: Set the hair color of the King."""
        self._hairs = value

    def set_eyes(self, color):
        """Method for King: Set the eye color of the King."""
        self.eyes = color

    def set_hairs(self, color):
        """Method for King: Set the hair color of the King."""
        self.hairs = color

    def get_eyes(self):
        """Method for King: Get the eye color of the King."""
        return self.eyes

    def get_hairs(self):
        """Method for King: Get the hair color of the King."""
        return self.hairs

    def __str__(self):
        """
        Method for King:
        Return a string representation of the King family.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Method for King:
        Return a formal string representation of the King family.
        """
        return self.__str__()

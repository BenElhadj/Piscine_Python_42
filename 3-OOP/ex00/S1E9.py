# S1E9.py

import sys
from abc import ABC, abstractmethod

sys.tracebacklimit = 0

class Character(ABC):
    """Abstract class representing a character."""
    
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character: Initialize a character with a first name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Method for Character: Kill the character by setting is_alive to False."""
        pass

class Stark(Character):
    """Class for Stark: Representing a Stark character."""
    
    def __init__(self, first_name, is_alive=True):
        """Constructor for Stark: Initialize a Stark character."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Method for Stark: Kill the Stark character."""
        self.is_alive = False
        
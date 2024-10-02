#!/usr/bin/python3

"""
This module defines a class `Square` that represents a square.
"""


class Square:
    """A class that defines a square by a private instance atrribute."""
    """Attributes : __size (int): size of the square."""
    """Methods: __init__(self, size): innitializes the square."""
    def __init__(self, size):
        """Initializes the square instance."""
        """Args: Size(int): The Szie of the square."""
        self.__size = size

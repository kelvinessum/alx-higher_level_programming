#!/usr/bin/python3
"""
This module defines a class `Square` that represents a square.
"""


class Square:
        """
    A class that defines a square by a private instance attribute `size`.

    Attributes:
        __size (int): The size of the square, which is a private attribute.

    Methods:
        __init__(self, size): Initializes the square with the given size.
    """

            def __init__(self, size):
                        """
        Initializes the square instance with a given size.

        Args:
            size (int): The size of the square (no type or value verification).
        """
                                self.__size = size

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
        __init__(self, size=0): Initializes the square with the given size, with
                                validation for type and value.
    """

            def __init__(self, size=0):
                        """
        Initializes the square instance with a given size.

        Args:
            size (int, optional): The size of the square. Must be an integer greater than
                                  or equal to 0. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
                                if not isinstance(size, int):
                                                raise TypeError("size must be an integer")
                                                    if size < 0:
                                                                    raise ValueError("size must be >= 0")

                                                                        self.__size = size  # Private instance attribute
                                                                        

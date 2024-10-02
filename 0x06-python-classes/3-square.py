#!/usr/bin/python3
"""
This module defines a class `Square` that represents a square.
"""


class Square:
        """
    A class that defines a square by a private instance attribute `size` and
    includes a method to calculate its area.

    Attributes:
        __size (int): The size of the square, which is a private attribute.

    Methods:
        __init__(self, size=0): Initializes the square with the given size.
        area(self): Returns the area of the square.
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

                                                                        self.__size = size

                                                                            def area(self):
                                                                                        """
        Returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
                                                                                                return self.__size ** 2
                                                                                            
#!/usr/bin/python3
"""
This module defines a class `Square` that represents a square with a size and position.
"""


class Square:
        """
    A class that defines a square with private instance attributes `size` and `position`
    and includes methods for calculating the area and printing the square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square (tuple of two positive integers).

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes the square with a given size and position.
        area(self): Returns the area of the square.
        size(self): Getter for size.
        size(self, value): Setter for size with validation.
        position(self): Getter for position.
        position(self, value): Setter for position with validation.
        my_print(self): Prints the square using the `#` character, respecting position.
    """

            def __init__(self, size=0, position=(0, 0)):
                        """
        Initializes the square instance with a given size and position.

        Args:
            size (int, optional): The size of the square. Must be an integer greater than or equal to 0.
                                  Defaults to 0.
            position (tuple, optional): The position of the square. Must be a tuple of 2 positive integers.
                                        Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or if position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
                                self.size = size  # Use the setter for size validation
                                        self.position = position  # Use the setter for position validation

                                            @property
                                                def size(self):
                                                            """
        Getter method for the size of the square.

        Returns:
            int: The size of the square.
        """
                                                                    return self.__size

                                                                    @size.setter
                                                                        def size(self, value):
                                                                                    """
        Setter method for the size of the square with validation.

        Args:
            value (int): The size of the square. Must be an integer greater than or equal to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
                                                                                            if not isinstance(value, int):
                                                                                                            raise TypeError("size must be an integer")
                                                                                                                if value < 0:
                                                                                                                                raise ValueError("size must be >= 0")
                                                                                                                                    self.__size = value

                                                                                                                                        @property
                                                                                                                                            def position(self):
                                                                                                                                                        """
        Getter method for the position of the square.

        Returns:
            tuple: The position of the square.
        """
                                                                                                                                                                return self.__position

                                                                                                                                                                @position.setter
                                                                                                                                                                    def position(self, value):
                                                                                                                                                                                """
        Setter method for the position of the square with validation.

        Args:
            value (tuple): The position of the square. Must be a tuple of 2 positive integers.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
                                                                                                                                                                                        if (not isinstance(value, tuple) or len(value) != 2 or
                                                                                                                                                                                                            not all(isinstance(num, int) and num >= 0 for num in value)):
                                                                                                                                                                                                        raise TypeError("position must be a tuple of 2 positive integers")
                                                                                                                                                                                                            self.__position = value

                                                                                                                                                                                                                def area(self):
                                                                                                                                                                                                                            """
        Returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
                                                                                                                                                                                                                                    return self.__size ** 2

                                                                                                                                                                                                                                    def my_print(self):
                                                                                                                                                                                                                                                """
        Prints the square with the `#` character. If the size is 0, prints an empty line.
        Takes the position into account by printing spaces for horizontal and vertical offset.
        """
                                                                                                                                                                                                                                                        if self.__size == 0:
                                                                                                                                                                                                                                                                        print("")
                                                                                                                                                                                                                                                                                    return

                                                                                                                                                                                                                                                                                        # Print vertical position (newlines)
                                                                                                                                                                                                                                                                                                print("\n" * self.__position[1], end="")

                                                                                                                                                                                                                                                                                                        # Print the square with horizontal position (spaces)
                                                                                                                                                                                                                                                                                                                for _ in range(self.__size):
                                                                                                                                                                                                                                                                                                                                print(" " * self.__position[0] + "#" * self.__size)
                                                                                                                                                                                                                                                                                                                                

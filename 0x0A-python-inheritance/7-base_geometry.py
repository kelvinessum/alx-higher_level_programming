#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an area method.
"""


class BaseGeometry:
    """
    A class representing BaseGeometry.
    """
    def area(self):
        """
        Raises an Exception indicating the area method is not implemented.
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Validates that the provided value is a positive integer.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

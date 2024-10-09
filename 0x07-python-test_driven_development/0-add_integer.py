#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""

def add_integer(a, b=98):
    """Add two integers."""
    """Add two integers."""
    """b (int, float, optional): The second number. Defaults to 98."""
    """Raises:
        TypeError: If a or b is not an integer or float."""
    """Raises:
        TypeError: If a or b is not an integer or float."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

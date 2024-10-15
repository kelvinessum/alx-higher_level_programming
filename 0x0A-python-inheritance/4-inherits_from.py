#!/usr/bin/python3
"""
This module defines a function that checks if an object inherits from a class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    from the specified class (a_class),.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

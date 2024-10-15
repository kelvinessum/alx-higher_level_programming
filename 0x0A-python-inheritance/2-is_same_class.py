#!/usr/bin/python3
"""
This module is function to check if an object is an instance of a class.
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) == a_class

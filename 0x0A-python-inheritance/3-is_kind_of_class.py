#!/usr/bin/python3
"""
This module defines a function to check if an instance
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of, or if obj is an instance of a class
    that inherited from a_class."""
    """Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False

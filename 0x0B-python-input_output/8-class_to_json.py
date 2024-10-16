#!/usr/bin/python3
"""
Function that returns the dictionary description for JSON serialization
of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary with the object's attributes.
    """
    return obj.__dict__

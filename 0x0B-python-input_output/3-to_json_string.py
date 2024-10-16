#!/usr/bin/python3
"""
This module defines a function to return the JSON representation of an object.
"""


import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized into a JSON string.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)

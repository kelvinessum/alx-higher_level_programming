#!/usr/bin/python3
"""
This module defines a function to return a Python object from a JSON string.
"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized into a Python object.

    Returns:
        object: The Python object corresponding to the JSON string.
    """
    return json.loads(my_str)

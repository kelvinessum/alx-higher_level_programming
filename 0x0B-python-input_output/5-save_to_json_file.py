#!/usr/bin/python3
"""
This module defines a function to write an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to be serialized into JSON.
        filename (str): The name of the file to which the JSON
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

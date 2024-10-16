#!/usr/bin/python3
"""
This module defines a function to load an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a 'JSON file'.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        The Python object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

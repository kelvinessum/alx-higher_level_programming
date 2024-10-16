#!/usr/bin/python3
"""
This module defines a function to write a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of char.
    Args:
        filename (str): The name of the file.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

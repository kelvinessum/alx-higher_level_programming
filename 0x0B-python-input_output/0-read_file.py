#!/usr/bin/python3
"""This module defines a function to read and print a text file."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout.Args:
        filename (str): The name of the file to read."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

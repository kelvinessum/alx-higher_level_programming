#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
It contains a method to print the list elements in ascending order.
"""


class MyList(list):
    """
    A subclass of list that implements a method to print the list in sorted order.
    """
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """
        Prints the list elements in ascending order (sorted).
        Assumes all elements are of type int.
        """
        print(sorted(self))

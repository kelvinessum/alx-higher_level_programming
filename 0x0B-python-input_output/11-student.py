#!/usr/bin/python3
"""
Defines a class Student with public instance attributes
and a method to retrieve its dictionary representation.
"""


class Student:
    """
    A class that defines a student by first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__

        if not isinstance(attrs, list):
            return self.__dict__

        filtered_attrs = {
            key: value
            for key, value in self.__dict__.items()
            if key in attrs
        }

        return filtered_attrs

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance wit

        Args:
            json (dict): A dictionary containing new values for attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)

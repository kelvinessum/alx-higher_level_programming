#!/usr/bin/python3


class Base:
    """Base class to manage 'id' attribute for all future classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class.

        Args:
            id (int): Optional id value. If provided, it is assigned.
                      Otherwise, a unique id is generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

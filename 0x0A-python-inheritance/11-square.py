#!/usr/bin/python3
"""Module has the implementation of `Square` class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from class `Rectangle`"""
    def __init__(self, size):
        """Init the values"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Prints description of the `Rectangle`"""
        sent = "[Square] {}/{}".format(self.__size, self.__size)
        return sent

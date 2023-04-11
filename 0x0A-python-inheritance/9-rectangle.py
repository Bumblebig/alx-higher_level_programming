#!/usr/bin/python3
"""has a class that inherits from `BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Init rectangle values"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates area of the geometry"""
        return self.__width * self.__height

    def __str__(self):
        """Prints description of the `Rectangle`"""
        sent = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return sent

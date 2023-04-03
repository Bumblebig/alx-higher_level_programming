#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ initializes the object """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ returns the value of the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ defines the width """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns the value of the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ defines the height """
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter of a rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height


    def __str__(self):
        """ returns the rectangle with # """
        val = ""
        if self.width == 0 or self.height == 0:
            return val

        for i in range(self.height):
            val += '#' * self.width + "\n"
        return val[:-1]


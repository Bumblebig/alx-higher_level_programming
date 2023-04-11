#!/usr/bin/python3
"""has a `BaseGeometry` class"""


class BaseGeometry:
    """empty BaseGeometry class"""

    def area(self):
        """Calculates area of the geometry"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates `value`"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

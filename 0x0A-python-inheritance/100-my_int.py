#!/usr/bin/python3
"""includes a class `MyInt` which inherits from `int`"""


class MyInt(int):
    """Inherits from int base class"""
    def __init__(self, value):
        """Init value"""
        self.value = value

    def __ne__(self, x):
        """not equal to"""
        if self.value is x:
            return True

    def __eq__(self, x):
        """equal to"""
        return not self.__ne__(x)

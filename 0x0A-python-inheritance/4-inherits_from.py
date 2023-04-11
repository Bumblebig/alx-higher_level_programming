#!/usr/bin/python3
"""single method"""


def inherits_from(obj, a_class):
    """check whether object is instance of a class inherited
        from directly or indirectly"""

    return (issubclass(type(obj), a_class)) and type(obj) != a_class

#!/usr/bin/python3
"""includes a new attribute to an object if possible"""


def add_attribute(obj, attr, value):
    """function that includes a new attribute to
    an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

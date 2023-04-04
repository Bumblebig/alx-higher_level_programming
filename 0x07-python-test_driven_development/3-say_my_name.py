#!/usr/bin/python3

def say_my_name(first_name, last_name):
    """prints first_name and last_name in a formattted string"""

    # checks whether first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # checks whether last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # returns formatted string
    string = "My name is {} {}".format(first_name, last_name)
    print(string)

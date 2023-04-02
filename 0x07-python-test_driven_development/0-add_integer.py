#!/usr/bin/python3
'''A function that adds two integer together'''

def add_integer(a, b=98):
    ''' Returns the sum of the integer and throws error if value not integer type'''

    try:
        a + b
    except (TypeError, ValueError):
        if not isinstance(a,(int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b,(int, float)):
            raise TypeError("b must be an integer")
    return int(a) + int(b)

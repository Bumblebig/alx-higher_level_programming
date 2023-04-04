#!/usr/bin/python3

def print_square(size):
    """Prints a square with the # character"""

    # checks whether size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # checks if size is not less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # checks whether size is an integer and greater than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # print the square
    str = ""
    for i in range(0, size):
        for el in range(0, size):
            str += "#"
        print(str)
        str = ""


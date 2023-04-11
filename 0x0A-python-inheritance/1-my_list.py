#!/usr/bin/python3

class MyList(list):
    """extends the list base class"""

    def print_sorted(self):
        """Prints a sorted list"""

        print(sorted(self))

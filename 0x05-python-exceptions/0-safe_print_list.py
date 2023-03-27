#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for num in range(x):
            print(f"{my_list[i]} \n")
            i += 1
    except (ValueError, TypeError, IndexError):
        pass

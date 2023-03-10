#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = []
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        for x in range(len(my_list)):
            if x == idx:
                copy.append(element)
            else:
                copy.append(my_list[x])
        return copy

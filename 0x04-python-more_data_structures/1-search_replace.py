#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    i = 0
    for item in my_list:
        if item == search:
            item[i] = replace
        i += 1
    return new_list

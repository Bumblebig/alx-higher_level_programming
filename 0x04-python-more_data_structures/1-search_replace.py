#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    i = 0
    for item in my_list:
        new_list.append(item)
        if item == search:
            new_list[i] = search
        i += 1
    return new_list

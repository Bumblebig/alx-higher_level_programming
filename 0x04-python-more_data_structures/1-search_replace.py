#!/usr/bin/python
def search_replace(my_list, search, replace):
    i = 0
    for item in my_list:
        if item == search:
            my_list[i] = replace
    i += 1

#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = []  
    for item in set_1:
        if item in set_2 and item in set_1:
            new_set.append(item)
    return set(new_set) 

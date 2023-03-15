#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for item in set_1:
        if item not in set_1 and item not in set_2:
            new_set.append(item)    
    return set(new_set)

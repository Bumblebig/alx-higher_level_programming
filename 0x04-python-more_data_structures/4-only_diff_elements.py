#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for item in set_1:
        if item in set_1 and item in set_2:
            item = item
        else:
            new_set.append(item)
    return set(new_set)

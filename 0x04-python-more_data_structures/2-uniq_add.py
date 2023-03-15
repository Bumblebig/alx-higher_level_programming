#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    x = 0
    for i in my_list:
        if i not in new_list:
            x += i
            new_list.append(i)
    return x

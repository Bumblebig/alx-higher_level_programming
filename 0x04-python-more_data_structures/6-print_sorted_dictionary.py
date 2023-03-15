#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = {}
    dic_list = []
    
    for key in a_dictionary.keys():
        dic_list.append(key)

    dic_list.sort()

    for item in dic_list:
        new_dic[item] = a_dictionary[item]

    a_dictionary = new_dic
    return a_dictionary

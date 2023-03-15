#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = 0
    keyVal = ''
    message = "Best score: "
    if a_dictionary:
        for key, val in a_dictionary.keys():
            if val > best_key:
                best_key = val
                keyVal = key
        print(f"{message}{keyVal}")
    else:
        print(f"{message}{None}")

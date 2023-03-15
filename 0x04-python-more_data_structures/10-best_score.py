#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = 0
    message = "Best score: "
    if a_dictionary:
        for val in a_dictionary.values():
            if val > best_key:
                best_key = val
        print(f"{message}{best_key}")
    else:
        print(f"{message}{None}")

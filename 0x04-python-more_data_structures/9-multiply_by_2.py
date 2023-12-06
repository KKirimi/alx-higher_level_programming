#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for k, val in list(new_dictionary.items()):
        new_dictionary[k] = val * 2
    return new_dictionary

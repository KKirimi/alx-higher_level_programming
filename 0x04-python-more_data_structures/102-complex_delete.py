#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, num in sorted(a_dictionary.items()):
        if num == value:
            del a_dictionary[k]
    return a_dictionary

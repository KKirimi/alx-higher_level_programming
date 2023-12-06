#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k, value in sorted(a_dictionary.items()):
        print(k, value, sep=': ')

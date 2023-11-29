#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        final_num = (-number % 10)
    elif number >= 0:
        final_num = number % 10
    print("{:d}".format(final_num), end="")
    return final_num

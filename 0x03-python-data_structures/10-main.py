#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

k = 0
while k < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[k], "is" if list_result[k] else "is not"))
    k += 1

#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
k_list = delete_at(my_list, idx)
print(k_list)
print(my_list)

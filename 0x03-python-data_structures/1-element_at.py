#!/usr/bin/python3

my_list = [1, 2, 3, 4, 5]
idx = 3

def element_at(my_list, idx):
    return (my_list[idx] if 0 <= idx < len(my_list) else None)

print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

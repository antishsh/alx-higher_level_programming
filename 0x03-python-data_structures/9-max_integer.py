#!/usr/bin/python3
def max_integer(miy_list=[]):
    if not my_list:
        return
    max_val = 0
    for i in my_list:
        if i > max_val:
            max_val = i
    return max_val

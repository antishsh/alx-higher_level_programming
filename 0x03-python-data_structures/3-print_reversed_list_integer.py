#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    total = len(my_list) - 1
    while total >= 0:
        print("{:d}".format(my_list[total]))
        print()
        total -= 1

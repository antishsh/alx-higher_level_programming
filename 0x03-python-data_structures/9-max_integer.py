#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    i = len(my_list) - 1
    while i > 1:
        j = 0
        while j < i:
            if my_list[j] > my_list[j+1]:
                number = my_list[j]
            else:
                number = my_list[j+1]
            j += 1
        i -= 1
    return number

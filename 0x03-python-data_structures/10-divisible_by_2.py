#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    multiplesOf2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiplesOf2.append(True)
        else:
            multiplesOf2.append(False)

    return (multiplesOf2)

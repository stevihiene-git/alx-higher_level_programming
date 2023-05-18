#!/usr/bin/python3

def number_keys(a_dictionary):
    tot_num = 0
    list_keys = list(a_dictionary.keys())

    for m in list_keys:
        tot_num += 1

    return (tot_num)

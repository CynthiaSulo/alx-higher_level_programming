#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return a_dictionary
    else:
        for key in sorted(a_dictionary):
            print("{}: {}".format(key, a_dictionary[key]))

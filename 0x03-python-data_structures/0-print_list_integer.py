#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for numbers in my_list:
        if isinstance(numbers, int) or isinstance(numbers, float):
            print("{}".format(numbers))

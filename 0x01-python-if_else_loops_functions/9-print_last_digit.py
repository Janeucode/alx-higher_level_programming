#!/usr/bin/python3
def def print_last_digit(number):
    number = str(number)
    if number:
        last_d = number[-1]
        print('{}'.format(last_d))
    else:
        print('the input is empty')

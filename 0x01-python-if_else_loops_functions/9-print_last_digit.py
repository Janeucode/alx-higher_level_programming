#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    if number:
        last_d = number[-1]
        print('{}'.format(last_d), end='')
    else:
        print('the input is empty')

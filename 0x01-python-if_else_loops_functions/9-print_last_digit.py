#!/usr/bin/python3
def print_last_digit(number):
    last_d = abs(number) % 10
    print(last_d, end='')

    if number < 0:
        print(last_d, end='')

    last_d = number % 10
    return last_d

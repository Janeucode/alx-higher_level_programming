#!/usr/bin/python3
for tens_digit in range(10):
    for units_digit in range(tens_digit + 1, 10):
        print("{:02d}".format(10 * tens_digit + units_digit), end=', ' if units_digit < 9 else '\n')

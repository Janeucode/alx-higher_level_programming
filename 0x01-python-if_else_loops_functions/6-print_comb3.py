#!/usr/bin/python3
for tens_digit in range(10):
    for units_digit in range(tens_digit + 1, 10):
        separator = ', ' if (tens_digit, units_digit) != (8, 9) else '\n'
        print("{:02d}".format(10 * tens_digit + units_digit), end=separator)

#!/usr/bin/python3
for number in range(99):
    if number < 16 :
        print(f"{number} = {hex(number)[:3]}\n", end='')
    else:
        print(f"{number} = {hex(number)[:4]}\n", end='')

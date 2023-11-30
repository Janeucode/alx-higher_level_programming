#!/usr/bin/python3
def uppercase(instr):
    result = ''
    for char in instr:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += uppercase_char
        else:
            result += char
    print('{}'.format(result))
    return result

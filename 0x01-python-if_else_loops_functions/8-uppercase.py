#!/usr/bin/python3
def uppercase(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += uppercase_char
        else:
            result += char
    print('{}'.format(result))


str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = uppercase(str)
print(str)

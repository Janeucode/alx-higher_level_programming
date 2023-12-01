#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    result = sum(map(int, argv[1:]))
    print(result)

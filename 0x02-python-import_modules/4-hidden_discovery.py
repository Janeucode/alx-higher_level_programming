#!/usr/bin/python3
import dis
import types
import hidden_4

if __name__ == "__main__":
    for name, value in vars(hidden_4).items():
        if not name.startswith('__') and isinstance(value, types.FunctionType):
            print(name)

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure tuples have at least 2 elements, padding with zeros if needed
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)

    # Perform addition of corresponding elements
    result_tuple = (a[0] + b[0], a[1] + b[1])

    return result_tuple

# Example usage:
tuple_a = (1, 2)
tuple_b = (3, 4)

result = add_tuple(tuple_a, tuple_b)
print("Result:", result)

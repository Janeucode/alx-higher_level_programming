#!/usr/bin/python3
str_text = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
start_index = str_text.find("object-oriented programming with Python")
substring = str_text[start_index:start_index + len("object-oriented programming with Python")]
print(substring)

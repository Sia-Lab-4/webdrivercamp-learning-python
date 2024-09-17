#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""

def remove_char(some_string):
    result = ""
    for char in some_string:
        if char != "a" and char != "A":
            result += char
    print(result)

remove_char(string)


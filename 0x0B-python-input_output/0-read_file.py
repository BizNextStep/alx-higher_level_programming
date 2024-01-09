#!/usr/bin/python3
"""
    function that reads a text file (UTF8)
    and prints it to stdout:
"""

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')

# Test the function
read_file("my_file_0.txt")


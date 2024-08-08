#!/usr/bin/python3
"""
Defines a function to read and print the contents of a UTF-8 text file.
"""


def read_file(filename=""):
    """
    Read a UTF-8 text file and print its contents to stdout.

    Parameters:
    filename (str): The path to the file to read. Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')

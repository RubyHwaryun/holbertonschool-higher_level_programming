#!/usr/bin/python3
"""
This module defines a function to append a string to a UTF-8 text file
and return the number of characters appended.
"""


def append_write(filename="", text=""):
    """
    Append a string to a UTF-8 text file and return the number of characters.

    Parameters:
    filename (str): The path to the file to append to.
    text (str): The text to append to the file. Defaults to an empty string.

    Returns:
    int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_appended = file.write(text)
    return num_chars_appended


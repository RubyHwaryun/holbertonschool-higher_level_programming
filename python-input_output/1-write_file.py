#!/usr/bin/python3
"""
This module defines a function to write a string to a UTF-8 text file
and return the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Write a string to a UTF-8 text file and return the number of characters written.

    Parameters:
    filename (str): The path to the file to write to. Defaults to an empty string.
    text (str): The text to write to the file. Defaults to an empty string.

    Returns:
    int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written

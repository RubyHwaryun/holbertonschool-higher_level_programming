#!/usr/bin/python3
"""
A function that appends a string at the end of a text file (UTF8).
"""


def append_write(filename="", text=""):
    """
    Parameters:
    filename (str): The path to the file to write to.
    text (str): The text to write to the file. Defaults to an empty string.

    Returns:
    int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
	num_chars_appended = file.write(text)
    return num_chars_appended

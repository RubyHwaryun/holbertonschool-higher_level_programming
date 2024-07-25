#!/usr/bin/python3

"""
Module: file_operations

This module provides functions for file operations, such as reading and writing files.

Functions:
- read_file(filename=""): Reads the content of the specified file and returns it as a string.
"""

def read_file(filename=""):
    """
    Reads the content of the specified file and returns it as a string.

    Parameters:
    filename (str): Optional. The name of the file to read. Defaults to reading 'my_file'.

    Returns:
    str: The content of the file as a string.

    Raises:
    IOError: If the file cannot be opened or if there is an input/output error while reading.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()

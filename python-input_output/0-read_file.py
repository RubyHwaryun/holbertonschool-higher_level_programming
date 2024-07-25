#!/usr/bin/python3

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
    with open('my_file', encoding="utf-8") as f:
	read_data = f.read()

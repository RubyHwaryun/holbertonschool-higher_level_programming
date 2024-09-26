#!/usr/bin/python3
"""
Write a function that loads a list of dictionaries from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Load a list of dictionaries from a JSON file.

    Parameters:
    filename (str): The path to the JSON file to be loaded.

    Returns:
    list: A list of dictionaries representing the data loaded from the file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)

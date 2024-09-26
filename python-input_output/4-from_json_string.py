#!/usr/bin/python3
"""
Write a function that returns an object
"""

import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Parameters:
    my_str (str): The JSON string to be converted to a Python object.

    Returns:
    any: A Python object representing the JSON string.
    """
    return json.loads(my_str)

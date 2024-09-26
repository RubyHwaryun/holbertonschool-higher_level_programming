#!/usr/bin/python3

"""
Write a function that returns the JSON representation
"""

import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON string.

    Parameters:
    my_obj (any): The Python object to be converted to JSON format.

    Returns:
    str: A JSON formatted string representing the input object.
    """
    return json.dumps(my_obj)

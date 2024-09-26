#!/usr/bin/python3
"""
Write a function that returns the dictionary description with simple data structure.
"""


def class_to_json(obj):
    """
    Convert an object to a JSON string.
    """
    return json.dumps(obj, default=lambda o: o.__dict__)

#!/usr/bin/python3

"""
Write a function that saves a list of dictionaries in a JSON file.
"""

import json


def save_to_json_file(my_list, file_path):
    """
    Save a list of dictionaries to a JSON file.
    
    Parameters:
    my_list (list): A list of dictionaries to be saved.
    file_path (str): The path to the JSON file where the data will be saved.
    """
    with open(file_path, 'w') as file:
        json.dump(my_list, file)

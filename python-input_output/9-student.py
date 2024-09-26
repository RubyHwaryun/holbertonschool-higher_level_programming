#!/usr/bin/python3
"""
Writes a class Student that defines a student.
"""

class Student:
    """
    Defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the student object to a JSON string.

        Returns:
            str: The JSON string representation of the student.
        """
        return json.dumps(self.__dict__)

#!/usr/bin/python3
"""
    Function that writes an Object to a text file,
    using a JSON representation:

"""


import json


def save_to_json_file(my_obj, filename):
    """ saves a json object into a file """
    with open(filename, mode="w", encoding='utf-8') as file:
        json.dump(my_obj, file)

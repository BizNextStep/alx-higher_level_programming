#!/usr/bin/python3
"""
    function that creates an Object from a “JSON file”:

"""


import json


def load_from_json_file(filename):
    """ creates a pythonobject from json file """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)

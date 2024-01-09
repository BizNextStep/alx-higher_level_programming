#!/usr/bin/python3
"""
    Script that adds all arguments to a Python list,
    and then save them to a file:

"""

import sys
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"

try:
    # Load existing list from the file
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, create an empty list
    my_list = []

# Add the arguments to the list
my_list.extend(args)

# Save the updated list to the file
save_to_json_file(my_list, filename)

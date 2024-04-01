#!/usr/bin/python3
"""
Displays the body of the response from a URL and
prints an error message if the HTTP status code is greater than or equal to 400.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)


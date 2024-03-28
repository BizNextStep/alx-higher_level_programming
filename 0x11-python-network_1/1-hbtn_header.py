#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

def get_request_id(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    headers = response.info()

    # Check if the 'X-Request-Id' header is present
    if 'X-Request-Id' in headers:
        request_id = headers['X-Request-Id']
        print(f"The value of X-Request-Id is: {request_id}")
    else:
        print("X-Request-Id header not found in the response.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_request_id(url)


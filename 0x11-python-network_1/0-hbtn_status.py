#!/usr/bin/python3
"""
Fetches the status of https://alx-intranet.hbtn.io/status using urllib.

"""
import urllib.request

def fetch_status(url):
    """
    Fetches the status of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        dict: A dictionary containing information about the response.

    """
    with urllib.request.urlopen(url) as response:
        data = response.read()

    return {
        "type": type(data),
        "content": data,
        "utf8 content": data.decode('utf-8')
    }

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    status_info = fetch_status(url)

    print("Body response:")
    for key, value in status_info.items():
        print("\t- {}: {}".format(key, value))


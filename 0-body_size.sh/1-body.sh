#!/bin/bash
# Sends a GET request to the URL and displays the body of the response
curl -sL "$1" -w "%{http_code}" -o /dev/null | grep -q "200" && curl -sL "$1"

#!/bin/bash
# # Send a DELETE request to the URL and display the body of the response
curl -sL "$1" -w "%{http_code}" -o /dev/null | grep -q "200" && curl -sL "$1"

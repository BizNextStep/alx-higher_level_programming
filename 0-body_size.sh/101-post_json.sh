#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument,
# and displays the body of the response
if [ ! -f "$2" ]; then
    echo "File not found: $2"
    exit 1
fi

if ! jq . "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

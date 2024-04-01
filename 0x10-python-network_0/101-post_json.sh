#!/bin/bash

jq -e . "$2" >/dev/null 2>&1 && curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1" && echo "" || echo "Not a valid JSON"

#!/bin/bash
# Displays the HTTP methods accepted by the server
curl -s -I -X OPTIONS "$1" | grep -i "Allow:" | cut -d' ' -f2-

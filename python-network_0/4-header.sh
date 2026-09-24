#!/bin/bash
# Sends a GET request to a URL with the header X-School-User-Id set to 98 and displays the body
curl -s -H "X-School-User-Id: 98" "$1"

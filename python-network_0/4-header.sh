#!/bin/bash
# Sends a GET request to a URL with the header X-HolbertonSchool-User-Id set to 98 and displays the body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"

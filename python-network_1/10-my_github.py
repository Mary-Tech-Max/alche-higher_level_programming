#!/usr/bin/python3
"""Uses the GitHub API with Basic Auth to display the user's id."""
import requests
import sys

if __name__ == "__main__":
    auth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))

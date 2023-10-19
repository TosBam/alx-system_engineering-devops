#!/usr/bin/python3
import requests
import sys
"""
This function read into reddit api and fetch the number of sunscribers
"""

def number_of_subscribers(subreddit):

    url = "https://www.reddit.com/dev/api/"
    headers = {
            "User-Agent": "0x16-api_advanced/1.0.0 (by /u/dmetero)"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            subscribers_count = data['data']['subscribers']
            return subscribers_count
        except KeyError:
            return 0
    else:
        return 0

#!/usr/bin/python5
"""
This function read into reddit api and fetch the number of sunscribers
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/dmetero)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs

#!/usr/bin/python3
"""number_sub module"""
import requests


def number_of_subscribers(subreddit):
    """function that returns total subscribers in subreddit"""

    headers = {"User-Agent": 'MyPythonScript/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        subcribe = res.json().get("data").get("subscribers")
        return subcribe
    return 0

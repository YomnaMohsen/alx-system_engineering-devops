#!/usr/bin/python3
"""number_sub module"""
import requests


def top_ten(subreddit):
    """lists top_ten titles"""
    headers = {"User-Agent": 'MyPythonCCode/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        top_ten = res.json().get("data").get("children")
        if not top_ten:
            print("None")
        else:
            for top in top_ten:
                print(top.get("data").get("title"))
    else:
        print("None")

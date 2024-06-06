#!/usr/bin/python3
"""list articles module"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """lists titles using pagination"""

    headers = {"User-Agent": 'Yomna is fine'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    query_param = {"after": after}

    res = requests.get(url, params=query_param, headers=headers,
                       allow_redirects=False)
    if res.status_code == 200:
        after_that = res.json().get("data").get("after")

        if after_that is not None:
            after = after_that
            recurse(subreddit, hot_list, after)
        articles = res.json().get("data").get("children")
        for p in articles:
            hot_list.append(p.get("data").get("title"))
            return hot_list
    else:    
        return None

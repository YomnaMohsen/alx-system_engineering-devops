#!/usr/bin/python3
"""list articles module"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """lists titles using pagination"""
    headers = {"User-Agent": 'MyPythonscript/2.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    query_param = {"after": after, "count": count}

    res = requests.get(url, headers=headers, params=query_param,
                       allow_redirects=False)

    if res.status_code == 404:
        return None
    page = res.json().get("data")
    after = page.get("after")
    count += page.get("dist")

    for p in page.get("children"):
        hot_list.append(p.get("data").get("title"))

    if after is not None:
        recurse(subreddit, hot_list, after, count)
    return hot_list

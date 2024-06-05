#!/usr/bin/python3
"""list articles module"""
import requests


def recurse(subreddit, hot_list=[], page=1, limit=100):
    """lists titles using pagination"""
    if len(hot_list) > limit:
        return hot_list
    
    headers = {"User-Agent": 'Mozilla'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    query_param = {"page": page}

    res = requests.get(url, params=query_param, headers=headers)

    if res.status_code == 404:
        return None
    
    artc = res.json()
    
    if "data" in artc and "children" in artc["data"]:
        articles = artc.get("data").get("children")

    for p in articles:
        hot_list.append(p.get("data").get("title"))

    if "data" in artc and "after" in artc["data"]:
        page += 1
        recurse(subreddit, hot_list, page)
    return hot_list

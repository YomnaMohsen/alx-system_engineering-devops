#!/usr/bin/python3
"""list articles module alphatically"""
import requests


def count_words(subreddit, word_list, after=""):
    """print count of given words"""

    headers = {"User-Agent": 'Yomna is cool'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    query_param = {"after": after}

    res = requests.get(url, params=query_param, headers=headers,
                       allow_redirects=False)
    if res.status_code == 200:
        after_that = res.json().get("data").get("after")
        if after_that is not None:
            after = after_that
            count_words(subreddit, word_list, after)
        articles = res.json().get("data").get("children")
        for p in articles:
            p.get("data").get("title").lower.split("")
            
    
    else:
        print ("")    
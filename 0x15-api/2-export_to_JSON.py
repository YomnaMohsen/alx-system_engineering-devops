#!/usr/bin/python3
""" Python script to export data in the JSON format."""

if __name__ == "__main__":
    import requests
    import sys
    import json
    try:
        id = int(sys.argv[1])
    except TypeError:
        exit()
    url = "https://jsonplaceholder.typicode.com/"
    res = requests.get(url+"/users/{}".format(id))
    if res.json() == {}:
        exit()
    u_name = (res.json().get("username"))
    url = url+"/users/{}/todos".format(id)
    res = requests.get(url)
    task_dict = {}
    list_dict = []
    for u_dict in res.json():
        list_dict.append({"task": u_dict.get("title"),
                         "completed": u_dict.get("completed"),
                          "username": u_name})

    task_dict[f"{id}"] = list_dict
    with open(f"{id}.json", "w", encoding="utf-8") as f:
        json.dump(task_dict, f)

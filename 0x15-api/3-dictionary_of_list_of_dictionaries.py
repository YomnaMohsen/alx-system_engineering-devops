#!/usr/bin/python3
""" Python script to export data in the JSON format."""

if __name__ == "__main__":
    import requests
    import sys
    import json
    filename = "todo_all_employees.json"
    url = "https://jsonplaceholder.typicode.com"
    task_dict = {}
    for u_id in range (1, 11):
        res = requests.get(url+"/users/{}".format(u_id))
        if res.json() == {}:
            exit()
        u_name = (res.json().get("username"))

        res = requests.get(url+"/users/{}/todos".format(u_id))
        list_dict = []
        for u_dict in res.json():
            list_dict.append({"username": u_name,
                              "task": u_dict.get("title"),
                              "completed": u_dict.get("completed"),
                              })

        task_dict[f"{u_id}"] = list_dict
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(task_dict, f)

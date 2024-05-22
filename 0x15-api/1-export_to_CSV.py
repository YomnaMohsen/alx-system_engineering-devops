#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and export to csv."""

if __name__ == "__main__":
    import requests
    import sys
    import csv
    try:
        id = int(sys.argv[1])
    except TypeError:
        exit()
    url = "https://jsonplaceholder.typicode.com/"
    res = requests.get(url+"/users/{}".format(id))
    if res.json() == {}:
        exit()
    name = (res.json().get("name"))
    url = url+"/users/{}/todos".format(id)
    res = requests.get(url)
    task_csv = []
    for u_dict in res.json():
        task_csv.append(u_dict)
    with open('USER_ID.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME",
                        "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in task_csv:
            writer.writerow([id, name, task.get("completed"),
                            task.get("title")])

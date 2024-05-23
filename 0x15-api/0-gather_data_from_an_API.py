#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    import sys
    try:
        id = int(sys.argv[1])
    except TypeError:
        exit()
    t_tasks = 0
    d_tasks = 0
    url = "https://jsonplaceholder.typicode.com"
    res = requests.get(url+"/users/{}".format(id))
    if res.json() == {}:
        exit()
    name = (res.json().get("name"))
    url = url+"/users/{}/todos".format(id)
    res = requests.get(url)
    task_title = []
    for u_dict in res.json():
        t_tasks += 1
        if (u_dict.get("completed")):
            d_tasks += 1
            task_title.append(u_dict.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, d_tasks, t_tasks))
    for task in task_title:
        print("\t {}".format(task))

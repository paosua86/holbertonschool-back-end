#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export
data in the JSON format."""


if __name__ == "__main__":

    import json
    import requests

    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    data_user = requests.get("https://jsonplaceholder.typicode.com/users"
                             ).json()

    dict = {}
    for user in data_user:
        username = user['username']
        task_list = []
        for task in todos:
            if task['userId'] == user['id']:
                dict_1 = {}
                dict_1['username'] = username
                dict_1['task'] = task['title']
                dict_1['completed'] = task['completed']
                task_list.append(dict_1)
        dict[user['id']] = task_list

    with open("todo_all_employees.json", 'w') as f:
        json.dump(dict, f)

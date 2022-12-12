#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the CSV format."""


if __name__ == "__main__":

    import json
    import requests
    from sys import argv

    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(argv[1])).json()
    data_user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(argv[1])).json()
    task_done_list = []
    with open('{}.json'.format(argv[1]), 'w') as f:
        for todo in todos:
            task_done_list.append({"task": todo['title'],
                                  "completed": todo['completed'],
                                   "username": data_user['username']})
        f.write(json.dumps({data_user['id']: task_done_list}))

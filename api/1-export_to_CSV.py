#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the CSV format."""


if __name__ == "__main__":

    import csv
    import requests
    from sys import argv

    # without .json() data comes divided
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(argv[1])).json()
    data_user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(argv[1])).json()

    with open('{}.cvs'.format(argv[1]), 'w') as f:
        thewriter = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)

        for todo in todos:
            row = [data_user['id'], data_user['username'],
                   todo['completed'], todo['title']]
            thewriter.writerow(row)

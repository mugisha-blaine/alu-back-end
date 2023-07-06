#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    response = requests.get(user)
    todos = response.json()
    print("Employee {} is done with tasks".format(todos.get('name')), end="")

    todoss = '{}todos?userId={}'.format(url, sys.argv[1])
    response = requests.get(todos)
    tasks = response.json()
    completed = []
    for task in tasks:
        if task.get('completed') is True:
            completed.append(task)

    print("({}/{}):".format(len(completed), len(tasks)))
    for task in completed:
        print("\t {}".format(task.get("title")))

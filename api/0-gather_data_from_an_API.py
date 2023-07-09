#!/usr/bin/python3
"""Script that uses API to get information about employee """
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    employee = '{}users/{}'.format(url, sys.argv[1])
    response = requests.get(employee)
    nom = response.json()
    print("Employee {} is done with tasks".format(nom.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    response = requests.get(todos)
    tasks = response.json()
    done = []
    for task in tasks:
        if task.get('completed') is True:
            done.append(task)

    print("({}/{}):".format(len(done), len(tasks)))
    for task in done:
        print("\t {}".format(task.get("title")))i

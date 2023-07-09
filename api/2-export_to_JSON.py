#!/usr/bin/python3
""" Script that uses API to get information about employee """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    employee = '{}users/{}'.format(url, userid)
    response = requests.get(user)
    nom = response.json()
    name = nom.get('username')

    todos = '{}todos?userId={}'.format(url, userid)
    response = requests.get(todos)
    tasks = response.json()
    done = []
    for task in tasks:
        dict_todo = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        done.append(dict_todo)

    done_task = {str(userid): done}
    filename = '{}.json'.format(userid)
    with open(filename, mode='w') as f:
        json.dump(done_task, f)

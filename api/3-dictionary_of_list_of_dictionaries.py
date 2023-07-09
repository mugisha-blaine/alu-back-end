#!/usr/bin/python3
""" Script that uses API to get information about employee """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    employee = '{}users'.format(url)
    response = requests.get(user)
    nom = response.json()
    todo_task = {}
    for user in nom:
        name = user.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(url, userid)
        response = requests.get(todos)
        tasks = response.json()
        done = []
        for task in tasks:
            dict_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            done.append(dict_task)

        todo_task[str(userid)] = done
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(done, f)

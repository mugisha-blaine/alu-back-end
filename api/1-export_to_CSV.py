#!/usr/bin/python3
""" Script that uses API to get information about employee """
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    employee = '{}users/{}'.format(url, userid)
    response = requests.get(employee)
    nom = response.json()
    name = nom.get('username')

    todos = '{}todos?userId={}'.format(url, userid)
    response = requests.get(todos)
    tasks = response.json()
    done = []
    for task in tasks:
        done.append([userid,
                     name,
                     task.get('completed'),
                     task.get('title')])

    filename = '{}.csv'.format(userid)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in done:
            employee_writer.writerow(task)i

#!/usr/bin/python3
''' 
   Script that use rest API to get information about employee
'''
import csv
import json
import requests


if __name__ == "__main__":
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')


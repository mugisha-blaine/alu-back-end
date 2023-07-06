#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


if __name__ == "__main__":
    
    def get_employee_todo_progress(employee_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    if response.status_code == 200:
        todos = response.json()

        completed_tasks = [todo for todo in todos if todo['completed']]

        employee_name = todos[0]['username']
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todos)

        print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")

        for task in completed_tasks:
            print(f"\t{task['title']}")

    else:
        print(f"Failed to retrieve TODO list for employee {employee_id}.")

employee_id = int(input("Enter the employee ID: "))
get_employee_todo_progress(employee_id)

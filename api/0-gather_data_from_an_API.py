#!/usr/bin/python3
"""script that returns information about his/her TODO list progress. """
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    # Make a GET request to the API endpoint
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()

        
        completed_tasks = [todo for todo in todos if todo['completed']]

        employee_name = todos[0]['username']
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todos)

        # Display progress information
        print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")

        # Display completed tasks
        for task in completed_tasks:
            print(f"\t{task['title']}")

    else:
        print(f"Failed to retrieve TODO list for employee {employee_id}.")

# Provide the employee ID as a command-line argument
employee_id = int(input("Enter the employee ID: "))
get_employee_todo_progress(employee_id)

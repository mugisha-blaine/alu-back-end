#!/usr/bin/python3
''' 
   Script that use rest API to get information about employee
'''


import csv
import requests
import sys


if __name__ == "__main__":
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    if response.status_code == 200:
        todos = response.json()

        """Extract relevant information for each task"""
        task_data = []
        for task in todos:
            task_data.append([
                task['userId'],
                task['username'],
                str(task['completed']),
                task['title']
            ])

        """Define the CSV file name"""
        file_name = f"{employee_id}.csv"

        """Write the task data to the CSV file"""
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(task_data)

        print(f"TODO list exported to {file_name} successfully.")

    else:
        print(f"Failed to retrieve TODO list for employee {employee_id}.")
   

#!/usr/bin/python3
"""
This module fetches and displays TODO list progress for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    employee_Id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/user/{}".format(base_url, employee_Id)
    user_response = requests.get(user_url)
    user_data = user_response.json()

    employee_name = user_data.get('name')

    todos_url = "{}/todos".format(base_url)
    todos_response = requests.get(todos_url, params={'userId': employee_Id})
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo.get('completed')]
    number_of_done_tasks = len(done_tasks)

    print("Employee () is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))

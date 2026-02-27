#!/usr/bin/python3
"""
Gather TODO list progress for a given employee using a REST API.
"""

import sys
import requests

if __name__ == '__main__':
    # Get employee ID as integer
    user_id = int(sys.argv[1])

    # URLs for user info and todos
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(user_id)

    # Fetch data from API
    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    # Safely get employee name
    employee_name = user_info.get("name")

    # Filter completed tasks using .get()
    task_completed = list(filter(lambda obj: obj.get("completed"), todos_info))

    # Count tasks
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    # Print summary exactly as ALU expects
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_number_of_tasks
    ))

    # Print all completed tasks with 1 tab + 1 space
    for task in task_completed:
        print("\t " + task.get("title"))

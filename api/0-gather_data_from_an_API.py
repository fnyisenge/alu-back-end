#!/usr/bin/python3
"""
Gather TODO list progress for a given employee using a REST API.
"""

import sys
import requests


if __name__ == "__main__":
    # Get the employee ID from command-line arguments
    employee_id = int(sys.argv[1])

    # URLs for user info and todos
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
        employee_id
    )

    # Fetch data from API
    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    # Extract employee name safely
    employee_name = user_info.get("name")

    # Filter completed tasks using .get() for safety
    task_completed = list(filter(lambda task: task.get("completed"), todos_info))

    # Count tasks
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    # Print the summary line exactly as ALU expects
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done_tasks, total_number_of_tasks
        )
    )

    # Print each completed task correctly formatted: 1 tab + 1 space
    for task in task_completed:
        print("\t " + task.get("title"))

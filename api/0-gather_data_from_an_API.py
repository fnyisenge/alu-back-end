#!/usr/bin/python3
"""
Gather TODO list progress for a given employee using a REST API.
"""

import sys

import requests

if __name__ == '__main__':
    user_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        user_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
        user_id
    )

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    employee_name = user_info.get("name")
    task_completed = list(filter(lambda obj: obj.get("completed"), todos_info))

    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_number_of_tasks
    ))

    for task in task_completed:
        print("\t " + task.get("title"))

#!/usr/bin/python3
"""
Export all employees' TODO lists to JSON file.
"""

import json
import requests


if __name__ == "__main__":
    # URLs
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users and todos
    users_info = requests.get(users_url).json()
    todos_info = requests.get(todos_url).json()

    # Build dictionary keyed by user_id
    all_data = {}

    # Create a mapping of user_id -> username for faster lookup
    user_map = {user["id"]: user["username"] for user in users_info}

    for task in todos_info:
        user_id = str(task["userId"])
        task_dict = {
            "username": user_map.get(task["userId"]),
            "task": task["title"],
            "completed": task["completed"]
        }
        if user_id not in all_data:
            all_data[user_id] = []
        all_data[user_id].append(task_dict)

    # Write to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)

#!/usr/bin/python3
"""
Export employee TODO list to JSON file using a REST API.
"""

import json
import sys

import requests


if __name__ == "__main__":
    # Get employee ID from command-line
    user_id = int(sys.argv[1])

    # URLs for user info and todos
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        user_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
        user_id
    )

    # Fetch data from API
    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    # Get username safely
    username = user_info.get("username")

    # Prepare JSON data in ALU format
    json_data = {str(user_id): []}

    for task in todos_info:
        json_data[str(user_id)].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    # Write JSON data to file named USER_ID.json
    filename = "{}.json".format(user_id)
    with open(filename, mode="w") as json_file:
        json.dump(json_data, json_file)

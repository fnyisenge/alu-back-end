#!/usr/bin/python3
"""
Export employee TODO list to CSV file using a REST API.
"""

import csv
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

    # Create CSV file named USER_ID.csv
    filename = "{}.csv".format(user_id)
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos_info:
            # Write row: USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

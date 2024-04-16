#!/usr/bin/python3
"""
This script gets data from a todo list through
a REST API protocol and presents useful info,
into a JSON file with all employees.
"""
import json
import requests


def get_todo_data():
    """ Gets data from url and makes that data into JSON. """
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"/users/"

    response1 = requests.get(url + user_url)
    users = response1.json()

    """ Pasing data"""
    data = {}
    for user in users:
        response2 = requests.get(
            url + user_url + str(user['id']) + "/todos"
        )
        todos = response2.json()
        list_data = []
        for todo in todos:
            task_data = {
                "username": user['username'],
                "task": todo['title'],
                "completed": todo['completed'],
                }
            list_data.append(task_data)
        data[user['id']] = list_data

    """ Export data to JSON """
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    get_todo_data()

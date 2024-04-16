#!/usr/bin/python3
"""
This script gets data from a todo list through
a REST API protocol and presents useful info.
"""
import json
import requests
import sys


def get_todo_data(emp_ID):
    """ Gets data from url and makes that data into JSON. """
    url = "https://jsonplaceholder.typicode.com"
    user_url = url + "/users/" + emp_ID
    todo_url = url + "/users/" + emp_ID + "/todos"
    response1 = requests.get(user_url)
    user = json.loads(response1.text)
    response2 = requests.get(todo_url)
    todos = json.loads(response2.text)

    """ Parses data. """
    list_data = []
    for todo in todos:
        task_data = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user['username']
            }
        list_data.append(task_data)
    data = {emp_ID: list_data}

    """ Export data to JSON """
    with open('{}.json'.format(emp_ID), 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    get_todo_data(sys.argv[1])

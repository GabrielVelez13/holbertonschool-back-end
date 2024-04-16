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
    comp = 0
    totalTodos = len(todos)
    completed_titles = []
    for todo in todos:
        if todo['completed']:
            comp += 1
            completed_titles.append(todo["title"])

    """ Prints data. """
    print("Employee {} is done with tasks({}/{}):".format(
        user["name"],
        comp,
        totalTodos
    ))
    for titles in completed_titles:
        print("\t " + titles)


if __name__ == "__main__":
    get_todo_data(sys.argv[1])

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
    user_url = url + f"/users/{emp_ID}"
    todo_url = url + f"/users/{emp_ID}/todos"
    response1 = requests.get(user_url)
    user = json.loads(response1.text)
    response2 = requests.get(todo_url)
    todos = json.loads(response2.text)

    """ Parses data. """
    complete = 0
    total_todos = len(todos)
    completed_titles = []
    for todo in todos:
        if todo['completed']:
            complete += 1
            completed_titles.append(todo["title"])

    """ Prints data. """
    print(f"Employee {user["name"]} is done with tasks({complete}/{total_todos}):")
    for titles in completed_titles:
        print(f"\t {titles}")

if __name__ == "__main__":
    get_todo_data(sys.argv[1])
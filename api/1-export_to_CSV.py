#!/usr/bin/python3
"""
This script gets data from a todo list through
a REST API protocol and presents useful info.
"""
import csv
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
    rows = []
    for todo in todos:
        row = [emp_ID, user["username"], todo["completed"], todo['title']]
        rows.append(row)

    """ Puts data into a CSV file. """
    with open('{}.csv'.format(emp_ID), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        csvwriter.writerows(rows)


if __name__ == "__main__":
    get_todo_data(sys.argv[1])

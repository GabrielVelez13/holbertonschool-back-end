#!/usr/bin/python3
import requests

url = "https://jsonplaceholder.typicode.com"
emp_ID = 1
user_url = url + f"/users/{emp_ID}"
todo_url = url + f"/users/{emp_ID}/todos"

response1 = requests.get(user_url)
user = response1.json()
print(user["name"])

response2 = requests.get(todo_url)
todos = response2.json()

complete = 0
total_todos = len(todos)
completed_titles = []
for todo in todos:
    if todo['completed']:
        complete += 1
        completed_titles.append(todo["title"])


print(f"Employee {user["name"]} is done with tasks({complete}/{total_todos}):")
for titles in completed_titles:
    print(f"\t {titles}")
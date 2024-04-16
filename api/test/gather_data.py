#!/usr/bin/python3
import requests

url = "https://jsonplaceholder.typicode.com"
user_url = f"/users/"
todo_url = url + f"/todos"

response1 = requests.get(todo_url)
todos = response1.json()

print(todos)

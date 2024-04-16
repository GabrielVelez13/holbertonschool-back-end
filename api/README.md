Steps to API call:

	1. Import requests
		- This is a python module for the HTTP library
	2. Use the requests.get('URL') method with a to get a response.
		 - Responses can be access using the .status_code method.
			- 200 means the connection was successful.
			- 400 means client did something wrong
			- 500 means server isn't responding
		- URLs should be written in full with the appropriate paths to where the data is. Each API is different.
	3. Change that response to a JSON file to better use the data.
		- .encoding: find what's the encoding.
		- .text: see the plaintext.
		- .header: To see the header use.
	4. Manipulate data as you wish :)

```python
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
```

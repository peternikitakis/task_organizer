import requests

tasks = {
    "tasks": [
        {"task_name": "Laundry", "due_date": "2025-08-08"},
        {"task_name": "Meeting", "due_date": "invalid-date"},
        {"task_name": "Study", "due_date": "2025-08-01"}
    ]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post("http://localhost:6000/organize", json=tasks, headers=headers)

if response.status_code == 200:
    for task in response.json()["tasks"]:
        print(f"{task['due_date']} - {task['task_name']}")
else:
    print("Error:", response.status_code)

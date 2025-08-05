
# Microservice A: Task Organizer

This microservice receives a list of tasks and returns them sorted by due date.

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

## How to Request Data

Send a POST request to `/organize` with a JSON body:
```json
{
  "tasks": [
    {"task_name": "Do laundry", "due_date": "2025-08-04"},
    {"task_name": "Buy groceries", "due_date": "2025-08-03"}
  ]
}
```

## How to Receive Data

You will receive a JSON response like:
```json
{
  "tasks": [
    {"task_name": "Buy groceries", "due_date": "2025-08-03"},
    {"task_name": "Do laundry", "due_date": "2025-08-04"}
  ]
}
```

![UML Sequence Diagram](uml-diagram.png)
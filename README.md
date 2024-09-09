# task-management-system
A simple task management system using Python and SQLite3

## Features

1.User

- Register
- Login

2.Task

- Add a task
- List all tasks
- Mark a task as done
- Delete a task

## How to run
1. Clone the repository
2. Run the following command:
```python -m venv venv```
3. Activate the virtual environment:
    - Windows: ```venv\Scripts\activate```
    - MacOS/Linux: ```source venv/bin/activate```
4. Install the dependencies:
```pip install -r requirements.txt```
5. Run the migrations:
```python manage.py migrate```
6. Run the server:
```python manage.py runserver```
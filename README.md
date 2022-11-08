# Software Requirements Specification for the TODO List Application

# Project Description
TODO list application is a simple application that allows users to create a list of tasks that they need to complete.
The application will allow users to add, edit, and delete tasks from their list. The application will also allow users to mark tasks as complete.

# Purpose
This is a SRS for the TODO list application. The purpose of this document is to provide a detailed description of the TODO list application and its requirements.

# Scope

This a simple TODO list application wtithout any complex features. 

# Features

- Add a task
- Edit a task
- Delete a task
- Mark a task as complete
- View all tasks
- View completed tasks
- View incomplete tasks

# Database Schema

The database schema for the TODO list application is as follows:

| Field | Type | Null | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| id | int(11) | NO | PRI | NULL | auto_increment |
| task | varchar(255) | NO | | NULL | |
| description | text | YES | | NULL | |
| status | tinyint(1) | NO | | 0 | |
| created_at | timestamp | NO | | CURRENT_TIMESTAMP | |
| updated_at | timestamp | NO | | CURRENT_TIMESTAMP | |
| user_id | int(11) | NO | | NULL | |

# API Endpoints

The API endpoints for the TODO list application are as follows:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasks | Get all tasks |
| GET | /api/tasks/{id} | Get a task |
| POST | /api/tasks | Create a task |
| POST | /api/tasks/{id} | Update a task |
| POST | /api/tasks/{id}/delete | Delete a task |
| POST | /api/tasks/{id}/complete | Mark a task as complete |
| GET | /api/tasks/completed | Get all completed tasks |
| GET | /api/tasks/incomplete | Get all incomplete tasks |

# CURL Examples

The CURL examples for the TODO list application are as follows:

- Get all tasks

```bash
curl -X GET http://localhost:8000/api/tasks
```

- Get a task

```bash
curl -X GET http://localhost:8000/api/tasks/1
```

- Create a task

```bash
curl -X POST http://localhost:8000/api/tasks -d "task=Task 1&description=Description 1"
```

- Update a task

```bash
curl -X POST http://localhost:8000/api/tasks/1 -d "task=Task 1&description=Description 1"
```

- Delete a task

```bash
curl -X POST http://localhost:8000/api/tasks/1/delete
```

- Mark a task as complete

```bash
curl -X POST http://localhost:8000/api/tasks/1/complete
```

- Get all completed tasks

```bash
curl -X GET http://localhost:8000/api/tasks/completed
```

- Get all incomplete tasks

```bash
curl -X GET http://localhost:8000/api/tasks/incomplete
```

# List of tasks

- Create a virtual environment
- Create a requirements.txt file
- Create a .gitignore file



- Create a project

```bash
django-admin startproject core .
```

- Create a TODO list application

```bash
python manage.py startapp todoAPI
```

- Register the TODO list application in the settings.py file

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todoAPI',
]
```

- Create a TODO list model

```python
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    task = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
```

- Make migrations

```bash
python manage.py makemigrations 
```

- Migrate

```bash
python manage.py migrate
```
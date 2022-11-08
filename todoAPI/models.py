from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    task = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def todo_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'task': self.task,
            'status': self.status,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __str__(self):
        return self.title

    def __str__(self):
        return self.task
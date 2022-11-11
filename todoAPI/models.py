from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    task = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def to_json(self) -> dict:
        '''to convert a task object to a dict.
        
        Args:
            self (object): task object.

        Returns:
            dict: task as dict.
        '''

        return {
            'id': self.id,
            'title': self.task,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'user': User.objects.get(username=self.user).username
        }


    def __str__(self):
        return self.task

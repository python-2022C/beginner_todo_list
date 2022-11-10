from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

from .models import Task

class CreateTask(View):
    def post(self, request):
        """
        Create a task

        args:
            request: HTTP request
            username: string
            password: string
            task: string
            description: string
        
        returns:  JSON response
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime

        """

        task = Task.objects.create(
            task = request.POST['task'],
            description = request.POST['description'],
            user = User.objects.get(username=request.POST['user'])
        )

        return JsonResponse({'task': task.to_json()})

        




from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from django.contrib.auth.models import User
from .models import Task
# Create your views here.

class CreateTask(View):
    def post(self, request):
        """
        Create aPresent task
        args:
            request: HTTP request
            username: string
            password: string
            task: string
            description: string
        
        returns:  JSON responses
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime
        """
        p = request.POST
        username = p['username']
        password = p['password']
        task = p['task']
        description = p['description']

        if not User.objects.filter(username = username):
            new_user = User.objects.create(username = username, password = password)
            new_user.save()
        if p.get('username'):
            user = User.objects.get(username = request.POST['username'])
        elif p.get('id'):
            user = User.objects.get(id = int(request.POST['id']))

        new_task = Task(user = user, task = task, description = description)
        new_task.save()

        json = {
            'id': new_task.id,
            'task': new_task.task,
            'description': new_task.description,
            'status': new_task.status,
            'created_at': new_task.created_at,
            'updated_at': new_task.updated_at
        }
        

        return JsonResponse(json)

class GetAllTaskView(View):
    def get(self, request):
        """
        Get all tasks

        args:
            request: HTTP request

        returns:  JSON response      
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime

        """

        users = request.POST
        tasks = Task.objects.all()
        json = {'results':[]}
        for i in tasks:
            json['results'].append({
                'id': i.id,
                'task': i.task,
                'description': i.description,
                'status': i.status,
                'created_at': i.created_at,
                'updated_at': i.updated_at,
            })

        
        return JsonResponse(json)
        

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from django.contrib.auth.models import User
from .models import Task
# Create your views here.

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
        

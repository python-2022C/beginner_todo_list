from django.shortcuts import render
from django.views import View
from .models import Task
from django.http import JsonResponse
# Create your views here.

class GetTask(View):
    def get(self, request, id):
        """
        Get task
        args:
            request: the request object
            id: the task id
        return:
            JsonRespons: the response object
        """
        task = Task.object.get(id=id)

        return JsonResponse({'task': task.to_json()})
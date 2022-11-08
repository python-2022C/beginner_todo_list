from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Task
# Create your views here.
class Get_all(View):
    def get(self, request):
        todo_all = Task.objects.all()
        todo_all_json = {'results':[]}
        for i in todo_all:
            todo_all_json['results'].append(i.todo_json())
        return JsonResponse(todo_all_json)
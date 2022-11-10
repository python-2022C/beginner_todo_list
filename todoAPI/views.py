from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import User,Task

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
        data=request.POST
        username=request.POST['username']
        password=request.POST['password']
        task=request.POST['tasks']
        description = request.POST['description']
        
        
        if not (User.objects.filter(username=username)):
            new_user=User.objects.create(username=username, password=password)
            new_user.save()
        if data.get('username'):
            user=User.objects.get(username=request.POST['username'])
        elif data.get('id'):
            eser=User.objects.get(id=int(request.POST['id']))

        new_task=Task(user=user,tasks=task, description=description)
        new_task.save()

        json_task={
            'id':new_task.id,
            'task':new_task.tasks,
            'description':new_task.description,
            'status':new_task.status,
            'created_at':new_task.created_at,
            'updated_id':new_task.updated_id,
        } 
        return JsonResponse(json_task)


class UpdateTask(View):
    def post(self, request, id):
        """
        Update a task

        args:
            request: HTTP request
            id: int
            task: string
            description: string
            status: boolean
        
        returns:  JSON response
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime

        """
        data=request.POST
        task=data['tasks']
        description=data['description']
        status=data['status']
        all_task=Task.objects.all()

        for i in all_task:
            if i.id == id:
                i.tasks = task
                i.status=status
                i.description=description
                i.save()

                json_task={
                    'id':i.id,
                    'task':i.tasks,
                    'description':i.description,
                    'status':i.status,
                    'created_at':i.created_at,
                    'updated_id':i.updated_id,
                }

        return JsonResponse(json_task)




class GetAllTaskView(View):
    def get(self, request):
        """
        Get all tasks

        args:
            request: HTTP request

        returns:  JSON response      

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

        





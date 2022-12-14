from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import User,Task
from base64 import b64encode, b64decode

from django.contrib.auth import authenticate
# Define a function decode_auth_header() that takes the authorization header as input and returns username and password

def decode_auth_header(auth_header):
    """
    Decodes the authorization header
    
    args:
        auth_header: string
    returns:
        username: string
        password: string
    """ 
    # Get the token from the header
    token = auth_header.split(" ")[1]
    # Decode the token
    decoded_token = b64decode(token).decode('utf-8')
    # Split the token into username and password
    username, password = decoded_token.split(':')
    # Return the username and password
    return username, password





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

        # Get the authorization header
        auth = request.headers.get('Authorization', None) 
        # If no authorization header was provided, return an error message
        if auth:
            # Decode the authorization header
            username, password = decode_auth_header(auth) 
            # authenticate the user
            user = authenticate(username=username, password=password) 
            if user:
                # Create user object
                user = User.objects.get(username=username)
                # Get the data from the request
                task = request.POST['task']
                description = request.POST['description']
                # Create a task object
                task = Task.objects.create(user=user, task=task, description=description)
                # Return the task object
                return JsonResponse(task.to_json())
            else:
                return JsonResponse({'message': 'Invalid credentials'})         
         
        else:
            return JsonResponse({'error': 'Authorization header is missing'}, status=401)

    def get(self, request):
        """
        Get all tasks

        args:
            request: HTTP request

        returns:  JSON response      
        """


        # Get the authorization header
        auth_header = request.headers.get('Authorization')
        # Check if the header is present
        if auth_header:
            # Decode the authorization header
            username, password = decode_auth_header(auth_header)
            # Check if the username and password are correct
            user = authenticate(username=username, password=password)
            # If the username and password are correct
            if user:
                # Get all user tasks
                tasks = Task.objects.filter(user=user)
                # Convert the tasks to JSON
                json_tasks = [task.to_json() for task in tasks]
                # Return the JSON response
                return JsonResponse(json_tasks, safe=False)

        # If the username and password are incorrect
            else:
                # Return an error message
                return JsonResponse({'error': 'Incorrect username or password'}, status=401)

        # If the authorization header is not present
        else:
            # Return an error message
            return JsonResponse({'error': 'Authorization header is not present'}, status=401)
        

       


        

        


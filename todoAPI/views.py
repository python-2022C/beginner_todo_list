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
        auth_header = request.headers.get('Authorization')
        if auth_header:
            username, password = decode_auth_header(auth_header)
            user = authenticate(username = username, password = password)
            if user:
                tasks = Task.objects.filter(user = user)
                for i in tasks:
                    if i.to_json()['id'] == id:
                        i.task = request.POST['task']
                        i.description = request.POST['description']
                        i.status = request.POST['status']
                        i.save()
                        return JsonResponse(i.to_json())
                    else:
                        return JsonResponse({{"error":'there is no such todo'}})
            else:
                return JsonResponse({'error': 'Incorrect username or password'}, status=401)
        else:
            return JsonResponse({'error': 'Authorization header is not present'}, status=401)

class DeleteTask(View):
    def get(self, request, id):
        """
        Delete a task

        args:
            request: HTTP request
            id: int

        returns:  JSON response
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime
        """
        auth_header = request.headers.get('Authorization')
        if auth_header:
            username, password = decode_auth_header(auth_header)
            user = authenticate(username = username, password = password)
            if user:
                tasks = Task.objects.filter(user = user)
                for i in tasks:
                    if i.to_json()['id'] == id:
                        delete_json = i.to_json()
                        i.delete()
                        return JsonResponse(delete_json)
                return JsonResponse({"error":'there is no such todo'})
            else:
                return JsonResponse({'error': 'Incorrect username or password'}, status=401)
        else:
            return JsonResponse({'error': 'Authorization header is not present'}, status=401)

class GetTask(View):
    def get(self, request, id):
        """
        Get a task

        args:
            request: HTTP request
            id: int

        returns:  JSON response      
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime

        """
        auth_header = request.headers.get('Authorization')
        if auth_header:
            username, password = decode_auth_header(auth_header)
            user = authenticate(username = username, password = password)
            if user:
                tasks = Task.objects.filter(user = user)
                for i in tasks:
                    if i.to_json()['id'] == id:
                        return JsonResponse(i.to_json())
                return JsonResponse({"error":'there is no such todo'})
            else:
                return JsonResponse({'error': 'Incorrect username or password'}, status=401)
        else:
            return JsonResponse({'error': 'Authorization header is not present'}, status=401)

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
        auth_header = request.headers.get('Authorization')
        if auth_header:
            username, password = decode_auth_header(auth_header)
            user = authenticate(username = username, password = password)
            if user:
                tasks = Task.objects.filter(user = user)
                json = {'results':[]}
                for i in tasks:
                    json['results'].append(i.to_json())
                return JsonResponse(json)
            else:
                return JsonResponse({'error': 'Incorrect username or password'}, status=401)
        else:
            return JsonResponse({'error': 'Authorization header is not present'}, status=401)

class CompleteTask(View):
    def get(self, request, id):
        """
        Complete a task
        args:
            request: HTTP request
            id: int
        returns:  JSON response
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime
        """
        auth_header = request.headers.get('Authorization')
        if auth_header:
            username, password = decode_auth_header(auth_header)
            user = authenticate(username = username, password = password)
            if user:
                tasks = Task.objects.filter(user = user)
                for i in tasks:
                    if i.to_json()['id'] == id:
                        i.status = True
                        i.save()
                        return JsonResponse(i.to_json())
                return JsonResponse({"error":'there is no such todo'})
            else:
                return JsonResponse({'error': 'Incorrect username or password'}, status=401)
        else:
            return JsonResponse({'error': 'Authorization header is not present'}, status=401)
        
class GetCompletedTask(View):
    def get(self, request):
        """
        Get completed tasks
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
        auth_header = request.headers.get('Authorization')
        if auth_header:
            username, password = decode_auth_header(auth_header)
            user = authenticate(username = username, password = password)
            if user:
                tasks = Task.objects.filter(user = user)
                json = {'results':[]}
                for i in tasks:
                    if i.to_json()['status'] == True:
                        json['results'].append(i.to_json())
                return JsonResponse(json)
            else:
                return JsonResponse({'error': 'Incorrect username or password'}, status=401)
        else:
            return JsonResponse({'error': 'Authorization header is not present'}, status=401)
        


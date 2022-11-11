from django.contrib import admin
from django.urls import path
from todoAPI.views import (
    CreateTask, 
    GetTask, 
    DeleteTask, 
    UpdateTask, 
    GetAllTaskView, 
    CompleteTask, 
    GetCompletedTask,
    GetIncompleteTask,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', CreateTask.as_view()),
    path('api/tasks/<int:id>', GetTask.as_view()),
    path('api/tasks/<int:id>/delete/', DeleteTask.as_view()),
    path('api/tasks/<int:id>/update/', UpdateTask.as_view()),
    path('api/tasks', GetAllTaskView.as_view()),
    path('api/tasks/<int:id>/complete/', CompleteTask.as_view()),
    path('api/tasks/complete/', GetCompletedTask.as_view()),
    path('api/tasks/incomplete', GetIncompleteTask.as_view())
]

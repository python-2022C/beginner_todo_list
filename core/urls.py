from django.contrib import admin
from django.urls import path
from todoAPI.views import CreateTask,UpdateTask

from todoAPI.models import Task
from todoAPI.views import GetAllTaskView
from django.views import View
from todoAPI.views import GetTask
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/tasks/all', GetAllTaskView.as_view()),
    path('get/<int:id>/', GetTask.as_view())






]

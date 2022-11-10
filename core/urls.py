from django.contrib import admin
from django.urls import path
from todoAPI.views import CreateTask,UpdateTask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', CreateTask.as_view()),
    path('api/tasks/<int:id>', UpdateTask.as_view()),
]

from django.contrib import admin
from django.urls import path
from todoAPI.views import CreateTask,UpdateTask,GetAllTaskView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/tasks/all', GetAllTaskView.as_view()),
    path('get/<int:id>/', GetTask.as_view())






]

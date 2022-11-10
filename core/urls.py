from django.contrib import admin
from django.urls import path
from todoAPI.views import CreateTask

urlpatterns = [
    path('admin/', admin.site.urls),

   
    path('api/tasks/', CreateTask.as_view()),
    


]

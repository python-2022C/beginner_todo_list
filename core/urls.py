
from django.contrib import admin
from django.urls import path
from todoAPI.views import Get_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Getalltasks/', Get_all.as_views)
]

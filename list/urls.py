from django.urls import path
from .views import post_list

app_name = 'list'

urlpatterns = [
    path('', post_list, name='list'),
    ]

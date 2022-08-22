from django.urls import path
from main.views import start

urlpatterns = [
    path('', start)
]
from django.urls import path
from .views import posts_list, first_post


urlpatterns = [
    path('1', first_post),
    path('', posts_list),
]
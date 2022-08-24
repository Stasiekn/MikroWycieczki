from django.urls import  path
from .views import galleries_list, gallery_details, add_gallery_view, add_photos_view

app_name = "galleries"
urlpatterns = [
    path('', galleries_list, name="list"),
    path('add/', add_gallery_view, name="add"),
    path('<int:gallery_id>', gallery_details, name="details"),
    path('<int:gallery_id>/add/', add_photos_view, name="add_photo")
]
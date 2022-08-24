from django.contrib import admin
from .models import Post
from import_export import resources
from import_export.admin import ExportMixin


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


@admin.register(Post)
class PostAdmin (admin.ModelAdmin, ExportMixin):
    list_display = ["id", "title", "created", "modified", "published"]
    search_fields = ["title", "description"]
    list_filter = ["published"]
    resource_class = PostResource

# admin.site.register(Post)
# Register your models here.

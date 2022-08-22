from django.db import models
from common.models import Timestamped


class Post(Timestamped):
    title = models.CharField(verbose_name="Tytuł", max_length=255)
    content = models.TextField(verbose_name="Treść")
    published = models.BooleanField(verbose_name="Opublikowany", default=False)


    def __str__(self):
        return f"{self.id} {self.title}"
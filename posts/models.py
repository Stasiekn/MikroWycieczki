from django.db import models
from django.utils.timezone import now, timedelta
from django.contrib.auth.models import  User


class CheckAgeMixin:
    def is_older_than_n_days(self, n=1):
        delta = timedelta(days=n)
        return now() - self.created > delta


class Timestamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    example_file = models.FileField(upload_to='posts/examples/', blank=True, null=True)


    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        abstract =True


class Post(Timestamped):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to="posts/examples/", null=True)


    def __str__(self):
        return f"{self.id} {self.title}"






import string

from django.db import models
from common.models import Timestamped, SlugMixin
from django.utils.text import slugify
from random import random

def upload_to(instance, filename):
    return f"galleries/{instance.gallery.title}/{filename}"

def get_random_text(n):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(n))

class Gallery (Timestamped, SlugMixin):

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title





class Photo(Timestamped):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to=upload_to)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="photos")
    source = models.CharField(max_length=512, null=True, blank=True)


    def __str__(self):
        return self.title



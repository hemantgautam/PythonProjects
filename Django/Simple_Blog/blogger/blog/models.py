from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    desc = models.TextField()
    url = models.SlugField(max_length=100, unique=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)



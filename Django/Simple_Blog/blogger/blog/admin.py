from django.contrib import admin
from .models import Blog


# Register your models here.

class BlogEntry(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}
    list_display = ['title', 'url']

admin.site.register(Blog, BlogEntry)

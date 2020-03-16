from django.contrib import admin
from .models import Course


# Register your models here.

class CourseEntry(admin.ModelAdmin):
    list_display = ['name', 'language', 'price']
    search_fields = ['name', 'language', 'price']

admin.site.register(Course, CourseEntry)

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer
from .models import Course


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

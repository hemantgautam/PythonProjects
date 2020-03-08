from django.urls import path
from . import views

urlpatterns = [
    path('', views.myresume, name="myresume")
]

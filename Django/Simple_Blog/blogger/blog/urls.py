from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('policy/', views.policy, name='policy'),
    path('contact/', views.contact, name='contact'),
    path('<slug>/', views.BlogDetailView.as_view(), name='post_detail'),
]

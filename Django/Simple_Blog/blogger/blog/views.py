from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog


# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blogs'
    ordering = ['-created']
    paginate_by = 2


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'
    slug_field = "url"


def about(request):
    return render(request, 'aboutus.html')


def policy(request):
    return render(request, 'policy.html')


def contact(request):
    return render(request, 'contact.html')

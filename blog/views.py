from django.shortcuts import render, get_object_or_404
from .models import blog

# Create your views here.


def allblogs(request):
    blogs = blog.objects
    return render(request, 'blog/allblogs.htm', {'blogs': blogs})


def detail(request, blog_id):
    detailblog = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog/detail.htm', {'blog': detailblog})

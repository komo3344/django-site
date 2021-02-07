from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/index.html', {'posts': posts})


class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post

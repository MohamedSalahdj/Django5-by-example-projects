from django.shortcuts import render
from django.http import http404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_details(requst, id):
    try:
        post = Post.published.get(id=id)
    except post.DoesNotExist:
        raise http404("No post found")
    
    return render(requst, 'blog/post/detail.html', {'post': post})
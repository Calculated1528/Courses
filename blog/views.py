from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag


def single_post(request, slug):
    current_post = get_object_or_404(Post , slug = slug)
    return render(request, 'blog/single_post.html', {'current_post': current_post})

def index(request):
    return render(request, 'blog/home.html')

def tagged(request, slug):
    tag = get_object_or_404(Tag)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/home.html', {'tag':tag, 'posts':posts})
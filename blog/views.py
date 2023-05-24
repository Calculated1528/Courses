from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from .models import Post
from .forms import PostForm
from taggit.models import Tag


def index(request):
    posts = Post.objects.all()
    # исправить shop/courses.html
    return render(request, 'shop/courses.html', {'post': posts})

def single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'shop/single_course.html', {'post': post})

def home_view(request):
    posts = Post.objects.all()
    # Show most common tags 
    form = PostForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        # Without this next line the tags won't be saved.
        form.save_m2m()
    return render(request, 'blog/home.html', {'posts':posts, 'form':form})

def detail_view(request):
    post = get_object_or_404(Post)
    return render(request, 'detail.html', {'post':post})

def tagged(request, slug):
    tag = get_object_or_404(Tag)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/home.html', {'tag':tag, 'posts':posts})
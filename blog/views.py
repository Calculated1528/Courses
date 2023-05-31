from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag
from .forms import PostForm
from django.utils import timezone

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form':form})

def single_post(request, slug):
    current_post = get_object_or_404(Post , slug = slug)
    tags = Tag.objects.filter(id = current_post.id)
    return render(request, 'blog/single_post.html', {'tags': tags, 'current_post': current_post, 'back_url': request.META.get('HTTP_REFERER')})

def index(request):
    return render(request, 'blog/home.html')

def tagged(request, slug):
    tag = get_object_or_404(Tag)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/home.html', {'tag':tag, 'posts':posts})



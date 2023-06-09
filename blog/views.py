from django.shortcuts import render, get_object_or_404
from .models import Post, PostComment
from taggit.models import Tag
from .forms import PostForm, PostCommentForm
from django.utils import timezone
from django.shortcuts import redirect


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
    comments = PostComment.objects.filter(id = current_post.id)

    if request.method == "POST":
        # A comment was posted
        comment_form = PostCommentForm(request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            #new_comment.current_post = current_post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = PostCommentForm(initial={'post': current_post})        
    return render(request, 'blog/single_post.html', {'tags': tags, 'current_post': current_post,
                                                     'comments': comments, 'comment_form': comment_form,
                                                     'back_url': request.META.get('HTTP_REFERER')})


def index(request):
    return render(request, 'blog/home.html')


def tagged(request, slug):
    tag = get_object_or_404(Tag)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/home.html', {'tag':tag, 'posts':posts})



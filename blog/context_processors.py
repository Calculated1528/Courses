from .models import Post

def GetPost(request):
    post = Post.objects.all()
    return {'Posts': post}
from django import forms
from .models import Post, PostComment

class PostForm(forms.ModelForm):
    # title = forms.CharField(max_length=100)
    # text = forms.TimeField()
    # tag = TaggableManager()

    class Meta:
        model = Post
        fields = {'title', 'text', 'tags'}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'})
        }

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment 
        fields = {'text', 'user', 'post'}
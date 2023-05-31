from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # title = forms.CharField(max_length=100)
    # text = forms.TimeField()
    # tag = TaggableManager()

    class Meta:
        model = Post
        fields = {'title', 'text'}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'})
        }
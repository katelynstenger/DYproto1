from django import forms

from .models import Post

class PostForm(forms.ModelForm):
# BTW: forms.ModelForm tells Django it is a form
    class Meta:
        model = Post
        fields = ('title', 'text',)
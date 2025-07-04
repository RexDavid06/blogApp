from django import forms
from app.models import BlogPost

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['post_title', 'post_desc']
        
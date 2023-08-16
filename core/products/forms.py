from django import forms
from .models import Comment

class CommentForm(forms.Form):
    email = forms.EmailField(max_length=100)
    comment = forms.CharField(max_length=1000)
    content_type = forms.CharField(max_length=100)
    object_id = forms.IntegerField()


    
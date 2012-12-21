#from django import forms
from django.forms import ModelForm
from models import Post

class PostForm(ModelForm):
    class meta:
        model = Post

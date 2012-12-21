from django import forms
from django.forms import ModelForm
from django.forms import Form
# Create your models here.

class LoginForm(Form):
    name = forms.CharField(label="Name", max_length=50)
    password = forms.CharField()
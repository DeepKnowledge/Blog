# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home")

def login(request):
    return HttpResponse("Login")

def logout(request):
    return HttpResponse("Logout")
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render
from forms import LoginForm

def home(request):
    return HttpResponse("Home")

def login(request):
    if request.method == 'POST': # If the form has been submitted...
        print("POST")
        return HttpResponse("POST")
    else:
        form = LoginForm() # An unbound form
        return render(request,"main/login.html",{'login_form':form})

#return HttpResponse("Login")

def logout(request):
    return HttpResponse("Logout")
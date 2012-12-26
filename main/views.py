# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from forms import LoginForm
from django.template.defaultfilters import register
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

@register.filter
def hash(h, key):
    return h[key]



def meta_html(request):
    values = request.META.items()
    html = []
    for k,v in values:
        html.append("<tr><td>%s</td><td>%s</td></tr>" % (k,v))

    HTML = '\n'.join(html)
    return HTML

def home(request):
#    return HttpResponse("Home")
    META = request.META
    return render(request,"main/meta.html",{"META":META})



def login_view(request):
    if request.method == 'POST': # If the form has been submitted...
        login(request)
        return HttpResponse("disabled account")
#        print request.POST
#
#        User()
#        login(request,User("ryan","2"))
#        user = request.user
#        print user
        username = request.POST['username'],
        password = request.POST['password'],
        print username
        print password
        user = authenticate(username = username,password = password)
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("disabled account")
        else:
            return HttpResponse("invalid login")
    else:
        print request.GET

        form = AuthenticationForm() # An unbound form
        return render(request,"main/login.html",{'login_form':form})

def logout_view(request):
    logout(request)
    return HttpResponse("Logout")

def search(request):
    error = False
    if "q" in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        return render_to_response("main/search_results.html",{"error":error})
    else:
        return render_to_response("main/search_form.html",{"error":error})

def crispy_view(request):
    return render_to_response("main/crispy_demo.html")
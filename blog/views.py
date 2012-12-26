from django.views.generic import ListView
from blog.models import Post
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from blog.forms import PostForm
from django.shortcuts import render

def list(request):
    return ListView.as_view(query=Post.objects.all().order_by('-create_at'))

#def detail(request):
#    return HTTPResponse()

@login_required
@staff_member_required
def tagpages(request,tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html",{"posts":posts,"tag":tag})


from django.contrib.auth import authenticate,login,logout,user_logged_in,user_logged_out
#from django.http import HttpResponse
from  django.contrib.auth.forms import AdminPasswordChangeForm

def user_login(request):
    username = request.POST['username'],
    password = request.POST['password'],

    user = authenticate(username = username,password = password);
    print user


def logout_view(request):
    return logout(request)

from django.http import HttpResponse

def time(request,offset):
    print offset
    return HttpResponse("Hello")

def post_add(request):
    if request.user.is_authenticated():
        print "request.user.is_authenticated() == 1"
    else:
        print "request.user.is_authenticated() == 0"

    print request.user.last_login
    print request.method

    if request.method == 'POST': # If the form has been submitted...
        form = PostForm(data=request.POST)
        new_blog = form.save()
#        return render_to_response("blog/post_add.html",{"post_form": form})
        return HttpResponse("POST")
    else:
        form = PostForm()
        return render_to_response("blog/post_add.html",{"post_form": form})

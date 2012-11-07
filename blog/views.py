from django.views.generic import ListView
from blog.models import Post
from django.shortcuts import render_to_response

def list(request):
    return ListView.as_view(query=Post.objects.all().order_by('-create_at'))

#def detail(request):
#    return HTTPResponse()

def tagpages(request,tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html",{"posts":posts,"tag":tag})
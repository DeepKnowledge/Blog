from django.conf.urls import patterns, include, url
from django.views.generic import ListView,DetailView
from blog.models import Post
from feeds import Blogfeed

urlpatterns = patterns('blog.views',
    url(r'^$',ListView.as_view(queryset=Post.objects.all().order_by("-create_at")[:2],template_name="blog.html")),
    url(r"^(?P<pk>\d+)$",DetailView.as_view(model=Post,template_name="post.html")),
    url(r'^archive$',ListView.as_view(queryset=Post.objects.all().order_by("-create_at"),template_name="archive.html")),

    url(r'^add$',"post_add"),


    url(r"^tag/(?P<tag>\w+)$", 'tagpages'),
    url(r"^feed/$",Blogfeed()),
    url(r'^logout$',"logout_view"),
    url(r'^time/(\d{1,2})/$',"time"),
)

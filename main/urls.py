from django.conf.urls import url, include, patterns

urlpatterns = patterns("main.views",
    url(r"^$","home",name="home"),
    url(r'^login$',"login"),
    url(r"^logout$","logout"),
)
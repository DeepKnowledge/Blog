from django.conf.urls import url, include, patterns



urlpatterns = patterns("main.views",
    url(r"^$","home",name="home"),
    url(r'^login$',"login_view"),
    url(r"^logout$","logout_view"),
    url(r"search","search"),
    url(r"^crispy$","crispy_view",name="crispy"),

)

#urlpatterns += patterns('',
#    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
#    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
#)

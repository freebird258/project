from django.conf.urls import patterns, url
from login_profile import views

 
urlpatterns = patterns('',
    url(r'^$', views.index, name='login1'),
)

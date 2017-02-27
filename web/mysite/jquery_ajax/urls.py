from django.conf.urls import patterns, url
#from login import views

urlpatterns = patterns('',
    #url(r'^$', views.login),
	url(r'^$', 'jquery_ajax.views.index', name='home'),
    url(r'^add/$', 'jquery_ajax.views.add', name='add'),
)



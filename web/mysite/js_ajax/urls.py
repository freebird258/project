from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'js_ajax.views.index', name='index'),
    url(r'^add/((?:-|\d)+)/((?:-|\d)+)/$', 'js_ajax.views.add', name='add'),

)


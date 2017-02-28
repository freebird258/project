from django.conf.urls import include, url
from django.contrib import admin

from focus import views

urlpatterns = [
	url(r'^focus/', include("focus.urls")),
	url(r'^$', views.index, name='index'),
	url(r'^admin/', include(admin.site.urls)),
]

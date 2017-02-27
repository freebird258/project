from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^login_profile/', include('login_profile.urls')),
    url(r'^jquery_ajax/', include('jquery_ajax.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^js_ajax/', include('js_ajax.urls')),	
]

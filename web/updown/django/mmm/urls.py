from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mmm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^disk/', 'disk.views.register'),
    url(r'^disk1/', 'disk.views.download'),
]

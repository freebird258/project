from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mmm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#	url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'disk.views.register'),
	url(r'^disk/', 'disk.views.register'),
	url(r'^disk1/', 'disk.views.download_nginx'),
]

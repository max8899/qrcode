from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qrcode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cnut.views.qrview', name='home'),
    url(r'^2/$', 'cnut.views.qrview1', name='home1'),
    url(r'^admin/', include(admin.site.urls)),
)

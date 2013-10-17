from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from django.conf import settings
import sys, re


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'test42cc.contact.views.index', name='index'),
    url(r'^requests/$', 'test42cc.contact.views.show_requests', name='show_requests'),
    url(r'^edit/$', 'test42cc.contact.views.edit_contacts', name='edit_contacts'),
    url(r'^login/$', login, name='login'),
    # url(r'^$', 'test42cc.views.home', name='home'),
    # url(r'^test42cc/', include('test42cc.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)



if 'test' in sys.argv:
    static_url = re.escape(settings.STATIC_URL.lstrip('/'))
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % static_url, 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
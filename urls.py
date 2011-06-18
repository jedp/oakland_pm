from settings import _HAVE_SOCIAL_AUTH
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url('^logged-in/$', 'oakland_pm.web.views.home'),
    url('^debug/$', 'oakland_pm.web.views.debug'),

    # Old School POSTS
    url('^$', 'oakland_pm.web.views.home', name='home'),
    url('^home/', 'oakland_pm.web.views.home', name='home'),
    url('^feed/', 'oakland_pm.web.views.feed'),
    url('^categories/', 'oakland_pm.web.views.categories'),
    url('^event/', 'oakland_pm.web.views.event'),

    # XHR Requests
    url('^xhr/logged-in/$', 'oakland_pm.web.xhr.home'),
    url('^xhr/feed/', 'oakland_pm.web.xhr.feed'),    
    url('^xhr/categories/', 'oakland_pm.web.xhr.categories'),
    url('^xhr/event/', 'oakland_pm.web.xhr.event'),    
)

if _HAVE_SOCIAL_AUTH:
    urlpatterns += patterns('',
        url(r'', include('social_auth.urls')),
    )


urlpatterns += staticfiles_urlpatterns()


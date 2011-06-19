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
)

urlpatterns += patterns('oakland_pm.web.views',
    url('^$', 'feed', name='home'),
    url('^feed/', 'feed'),
    url('^search/', 'search'),
    url('^friends/', 'friends'),
    url('^messages/', 'messages'),
    url('^categories/', 'categories'),
    url('^about/', 'about'),
    url('^event/(?P<event_id>\d+)/', 'event'),
)

urlpatterns += patterns('oakland_pm.web.xhr',
    # XHR Requests
    url('^xhr/feed/', 'feed'),
    url('^xhr/about/', 'about'),
    url('^xhr/categories/', 'categories'),
    url('^xhr/event/(?P<event_id>\d+)/', 'event'),
)

if _HAVE_SOCIAL_AUTH:
    urlpatterns += patterns('',
        url(r'', include('social_auth.urls')),
    )


urlpatterns += staticfiles_urlpatterns()


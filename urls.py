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

    # social auth
    url(r'', include('social_auth.urls')),

    url('^logged-in/$', 'oakland_pm.web.views.home'),
    url('^debug/$', 'oakland_pm.web.views.debug'),

    url('^$', 'oakland_pm.web.views.home', name='home'),
)

urlpatterns += staticfiles_urlpatterns()


from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'heater.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^webapi/', include('webapi.urls')),
    url(r'^mcu/', include('mcu.urls')),
    url(r'^demo/', include('demo.urls')),
    url(r'^client/', include('client.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^$', include('demo.urls')), 
)

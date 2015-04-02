from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from webapi import views

urlpatterns = patterns('',
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetails.as_view()),
    url(r'^device/$', views.DeviceList.as_view()),
    url(r'^device/(?P<pk>[0-9]+)/$', views.DeviceDetails.as_view()),
    url(r'^sensor/$', views.SensorList.as_view()),
    url(r'^sensor/(?P<pk>[0-9]+)/$', views.SensorDetails.as_view()),
    #url(r'^data/$', views.DataList.as_view()),
    url(r'^data/(?P<pk>[0-9]+)/$', views.DataDetails.as_view()),
    url(r'^interface/$', views.InterfaceLists.as_view()),
    url(r'^interface/(?P<pk>[0-9]+)/$', views.InterfaceDetails.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

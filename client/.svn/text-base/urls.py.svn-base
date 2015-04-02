from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from client.views import clogin,clogout,cregister,client_get_response,client_post_cmd,get_deviceid_by_userid,\
    get_deviceid_by_username,del_device_by_username

urlpatterns = patterns('',
                (r'^register/$',cregister),      
                (r'^login/$',clogin),
                (r'^logout/$',clogout),
                (r'^getinfo/$',client_get_response),
                (r'^postcmd/$',client_post_cmd),
                (r'^getdeviceid/$',get_deviceid_by_userid),
                (r'^getDevByUser/$',get_deviceid_by_username),
                (r'^delDevByUser/$',del_device_by_username),
                (r'^$','demo.views.deliverCmd'),
)

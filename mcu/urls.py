from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^device/$', 'mcu.views.reg_device'),
    url(r'^deviceinfo/$', 'mcu.views.get_dev_info'),
    url(r'^sensor/$', 'mcu.views.reg_sensor'),
    url(r'^datas/$', 'mcu.views.post_data'),
    url(r'^getcmd/$', 'mcu.views.get_cmd'),
    url(r'^checkupdate/$', 'mcu.views.checkupdate'),
    url(r'^servertime/$', 'mcu.views.servertime'),
)   
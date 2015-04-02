from django.conf.urls import patterns, url
from demo import views
from demo import myviews

urlpatterns = patterns('demo.views', 
    url(r'^getdevicestatus/$','get_device_status'),
    url(r'^setdevicestatus/$','set_device_status'),
    url('^$','index'),
    url('^deliverCmd/$','deliverCmd'),
    url('^interface/$',myviews.MyInterface.as_view()),
    url('^project/$','project'),
    url('^backstage/$','backstage'),
    url('^debug/$',myviews.MyDebug.as_view()),
    url('^register/$','register'),
    url('^login/$','login'),
    url('^logout/$','logout'),
    url('^updateMcuVersion/$','updateMcuVersion'),
    url('^shutdownUpdate/$','shutdownUpdate'),
)

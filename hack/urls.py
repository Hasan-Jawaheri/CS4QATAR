from django.conf.urls import patterns, include, url
from hack import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'execCmd/$', views.execCmd, name='execCmd')
)

from django.conf.urls import patterns, url
from rOne import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about')
        )

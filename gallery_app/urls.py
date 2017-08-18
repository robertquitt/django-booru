from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^image/(?P<pk>[0-9]+)$', views.image, name='image'),
    url(r'^tag/(?P<pk>.+)$', views.tag, name='tag'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^about/$', views.about, name='about')
]

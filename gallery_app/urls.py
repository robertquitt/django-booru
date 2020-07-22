from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.list, name="list"),
    path("image/(?P<pk>[0-9]+)", views.image, name="image"),
    path("tag/(?P<pk>.+)", views.tag, name="tag"),
    path("upload/", views.upload, name="upload"),
    path("about/", views.about, name="about"),
]

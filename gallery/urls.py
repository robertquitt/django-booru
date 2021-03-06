from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin


urlpatterns = [
    path("", include("gallery_app.urls")),
    # path("admin/", include('admin.site.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

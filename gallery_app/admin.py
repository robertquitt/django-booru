from django.contrib import admin

from .models import Image, Tag
from sorl.thumbnail.admin import AdminImageMixin
# Register your models here.

class ImageAdmin(AdminImageMixin, admin.ModelAdmin):
	pass

admin.site.register(Image, ImageAdmin)
admin.site.register(Tag)

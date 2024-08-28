from django.contrib import admin
from .models import *

class brandadmin(admin.ModelAdmin):
    list_display = ['id', 'en_name', 'url', 'active']
admin.site.register(brand, brandadmin)

class brand_slide_admin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'slide', 'active']
admin.site.register(brand_slide, brand_slide_admin)

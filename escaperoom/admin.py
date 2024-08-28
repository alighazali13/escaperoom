from django.contrib import admin
from .models import *

class slides_home(admin.ModelAdmin):
    list_display = ['id', 'admin_login', 'name', 'url', 'slide', 'active']
admin.site.register(slides, slides_home)

class advertising_banner_home(admin.ModelAdmin):
    list_display = ['id', 'admin_login', 'adv_banner_name', 'adv_banner_url', 'adv_banner_slide', 'active']
admin.site.register(advertising_banner, advertising_banner_home)

class advertising_slide_home(admin.ModelAdmin):
    list_display = ['id', 'admin_login', 'adv_slide_name', 'adv_slide_url', 'adv_slide_slide', 'active']
admin.site.register(advertising_slide, advertising_slide_home)



from django.contrib import admin
from .models import *

class admin_login_admin(admin.ModelAdmin):
    list_display = ['id', 'collector_id', 'username', 'phonenumber', 'last_login', 'active']
admin.site.register(admin_login, admin_login_admin)
class admin_info_admin(admin.ModelAdmin):
    list_display = ['id', 'admin_login', 'collector_id', 'last_name', 'active']
admin.site.register(admin_info, admin_info_admin)
from django.contrib import admin
from .models import *

class player_login_admin(admin.ModelAdmin):
    list_display = ['id', 'username', 'mail', 'phonenumber', 'joined_at', 'modified_at',  'last_login', 'active']
admin.site.register(player_login, player_login_admin)

class player_info_admin(admin.ModelAdmin):
    list_display = ['id', 'player_login', 'last_name', 'age', 'gender', 'birthday_date',  'complited_at', 'active']
admin.site.register(player_info, player_info_admin)
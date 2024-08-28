from django.contrib import admin
from .models import *

class game_admin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'en_name', 'fa_name', 'price', 'admin',  'url', 'active']
admin.site.register(game, game_admin)

class game_type_admin(admin.ModelAdmin):
    list_display = ['id', 'fa_name', 'en_name', 'active']
admin.site.register(game_type, game_type_admin)

class game_details_admin(admin.ModelAdmin):
    list_display = ['id', 'game', 'full_address', 'active']
admin.site.register(game_details, game_details_admin)

class two_days_later_admin(admin.ModelAdmin):
    list_display = ['id', 'game', 'game_details', 'enable_date', 'active']
admin.site.register(two_days_later, two_days_later_admin)

class genre_admin(admin.ModelAdmin):
    list_display = ['id', 'fa_name', 'en_name', 'active']
admin.site.register(genre, genre_admin)

class game_genres_admin(admin.ModelAdmin):
    list_display = ['id', 'genre', 'game', 'active']
admin.site.register(game_genres, game_genres_admin)

class game_time_admin(admin.ModelAdmin):
    list_display = ['id', 'game', 'time_from', 'time_to', 'active']
admin.site.register(game_time, game_time_admin)

class closed_time_admin(admin.ModelAdmin):
    list_display = ['id', 'game', 'game_time', 'day', 'active']
admin.site.register(closed_time, closed_time_admin)

class closed_day_admin(admin.ModelAdmin):
    list_display = ['id', 'game', 'day', 'active']
admin.site.register(closed_day, closed_day_admin)

class sold_time_admin(admin.ModelAdmin):
    list_display = ['id', 'game', 'player', 'game_time', 'day', 'active']
admin.site.register(sold_time, sold_time_admin)

class game_comment_admin(admin.ModelAdmin):
    list_display = ['id', 'game', 'player_info', 'created_at', 'like', 'active']
admin.site.register(game_comment, game_comment_admin)

class game_reply_admin(admin.ModelAdmin):
    list_display = ['id', 'game_comment', 'admin_info', 'active']
admin.site.register(game_reply, game_reply_admin)



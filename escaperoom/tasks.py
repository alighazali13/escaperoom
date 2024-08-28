from celery import shared_task
from celery.schedules import crontab
import jdatetime
from game.models import game
from .functions import get_free_for_book
from config.celery import app


app.conf.beat_schedule = {
    'update-database-every-midnight': {
        'task': 'escaperoom.tasks.update_game_values',
        'schedule': crontab(hour=23, minute=20),  # هر روز ساعت 00:00
    },
}

@shared_task
def update_game_values():
    print('hi')
    # به روز رسانی مقدار روز بسته و سانس های خالی هر بازی
    # today = jdatetime.datetime.now().strftime("%Y-%m-%d")
    # game.objects.filter(active=True).update(today_time=game__game_time.number,today_close=False)
    
    # closed_games_today = closed_day.objects.filter(day=today).values_list('game', flat=True)
    
    # # پیدا کردن سانس‌های بسته شده و فروخته شده امروز
    # closed_sessions_today = closed_time.objects.filter(day=today).values_list('game_time', flat=True)
    # sold_sessions_today = sold_time.objects.filter(day=today).values_list('game_time', flat=True)

    # games = game.objects.filter(game_type__en_name='escaperoom', active=True)
    # gametime_obj = game_time.objects.filter(game=g)
    #     gt_len = len(gametime_obj)
    #     not_available_len = len(closed_sessions_today) + len(sold_sessions_today)
    #     if gt_len - not_available_len > 0:
            
    #         available_time_len = gt_len - not_available_len
    #         print('available_time_len')
    #         print(available_time_len)
    #         free_games[g.id] = available_time_len

    
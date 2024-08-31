from celery import shared_task
from celery.schedules import crontab
from config.celery import app
from django.db.models import F
import jdatetime, logging
from game.models import game
from .functions import get_free_for_book

from game.models import game, game_details, game_time, closed_day, closed_time, sold_time


app.conf.beat_schedule = {
    'update-database-every-midnight': {
        'task': 'escaperoom.tasks.update_game_values',
        'schedule': crontab(hour=0, minute=0),  # everyday @ 00:00
        # 'schedule': crontab(minute='*/1'),
    },
}
# config logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.task
def update_game_values():
    logging.info("Task executed at 00:00")

    today = jdatetime.datetime.now().strftime("%Y-%m-%d")
    
    # change to defaul value
    if game.objects.filter(active=True).exists():
        games_obj = game.objects.filter(active=True)
        for game_obj in games_obj:
            game_detailes_obj = game_details.objects.get(game=game_obj, active=True)
            game_obj.today_game_times = game_detailes_obj.game_time_number
            game_obj.today_close = False
            game_obj.save()

    

    # change closed_games_today to True for closed today games
    if closed_day.objects.filter(day=today).exists():
        closed_games_today = closed_day.objects.filter(day=today)
        for cgt in closed_games_today:
            cgame_obj = cgt.game
            cgame_obj.today_close = True
            cgame_obj.save()
    
    if closed_time.objects.filter(day=today).exists():
        closed_time_today = closed_time.objects.filter(day=today)
        for ctt in closed_time_today:
            ctgame_obj = ctt.game
            ctgame_obj.today_game_times -= 1
            if ctgame_obj.today_game_times == 0:
                today_close = True
            ctgame_obj.save()

    if sold_time.objects.filter(day=today).exists():
        sold_time_today = sold_time.objects.filter(day=today)
        for stt in sold_time_today:
            stgame_obj = stt.game
            stgame_obj.today_game_times -= 1
            if stgame_obj.today_game_times == 0:
                today_close = True
            stgame_obj.save()

    
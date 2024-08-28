import random, jdatetime
from adminstrator.models import admin_codes
from player.models import player_codes
from game.models import game, game_time, closed_day, sold_time, closed_time
from django.db.models import Q

def send_code(phonenumber, client):
    if client == 'admin':
        code = random.randint(10000,99999)
        admin_codes.objects.create(
            phonenumber = phonenumber,
            code = code
        )
    if client == 'player':
        code = random.randint(100000,999999)
        player_codes.objects.create(
            phonenumber = phonenumber,
            code = code
        )

    return code

def validation(input_code, phonenumber, req_type):
    if req_type == 'admin':
        if admin_codes.objects.filter(phonenumber=phonenumber, code=input_code).exists():
            status = True
            admin_codes.objects.get(phonenumber=phonenumber, code=input_code).delete()
        else:
            status = False

    if req_type == 'player':
        if player_codes.objects.filter(phonenumber=phonenumber, code=input_code).exists():
            status = True
            player_codes.objects.filter(phonenumber=phonenumber, code=input_code).delete()
        else:
            status = False
    return status

def reset_code_sent():
    admin_codes.objects.all().delete()
    player_codes.objects.all().delete()

def get_free_for_book():
    today = jdatetime.datetime.now().strftime("%Y-%m-%d")
    print(today)
    
    free_games = {}
    
    games = game.objects.filter(game_type__en_name='escaperoom', active=True)

    for g in games:
        closed_games_today = closed_day.objects.filter(day=today).values_list('game', flat=True)
        available_games = game.objects.exclude(id__in=closed_games_today)

        # پیدا کردن سانس‌های بسته شده و فروخته شده امروز
        closed_sessions_today = closed_time.objects.filter(day=today).values_list('game_time', flat=True)
        sold_sessions_today = sold_time.objects.filter(day=today).values_list('game_time', flat=True)

        

        gametime_obj = game_time.objects.filter(game=g)
        gt_len = len(gametime_obj)
        not_available_len = len(closed_sessions_today) + len(sold_sessions_today)
        if gt_len - not_available_len > 0:
            
            available_time_len = gt_len - not_available_len
            print('available_time_len')
            print(available_time_len)
            free_games[g.id] = available_time_len

    print('free_games')
    print(free_games)
    


    
    return free_games, closed_games_today
        


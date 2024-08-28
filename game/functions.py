from django.shortcuts import render, redirect
from django.http import JsonResponse
import uuid, json, random, jdatetime
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from game.models import *


def get_halidays(request):
    data = json.loads(request.POST.get('getdata'))
    game_name = data['game_name']
    past_days = []
    closed_days = []

    game_obj = game.objects.none()
    if game.objects.filter(fa_name=game_name, active=True).exists():
        game_obj = game.objects.get(fa_name=game_name, active=True)

    today = jdatetime.datetime.now()
    year = today.strftime('%Y')
    month = today.strftime("%m")
    day = int(today.strftime("%d"))
    
    past_days = list(range(1, day))
    closed_days_obj = closed_day.objects.none()
    if closed_day.objects.filter(game = game_obj, active=True).exists():
        closed_days_obj = closed_day.objects.filter(game = game_obj, active=True)
        for cd in closed_days_obj:
            cd_month = cd.day.strftime('%m')
            cd_day = cd.day.strftime('%d')

            #برای این ماه
            if int(cd_month) == int(month) :
                closed_days.append(int(cd_day))
            #برای ماه بعد
            if int(cd_month) == int(month)+1:
                closed_days.append(str(cd_day))


    context = {
        'past_days':past_days,
        'closed_days':closed_days,
    }

    return JsonResponse(context)

def get_gametime(request):
    data = json.loads(request.POST.get('getdata'))
    today = jdatetime.datetime.now()
    year = today.strftime('%Y')
    month = today.strftime("%m")
    day = data['day']
    selected_date = jdatetime.datetime(int(year), int(month),int(day))
    
    game_obj = game.objects.none()
    if game.objects.filter(fa_name=data['name'], active=True):
        game_obj = game.objects.get(fa_name=data['name'], active=True)

    game_time_obj = game_time.objects.none()
    if game_time.objects.filter(active=True).exists():
        game_time_obj = game_time.objects.filter(active=True)

    

    game_time_length  = len(game_time_obj)
    

    closed_time_obj = closed_time.objects.none()
    if closed_time.objects.filter(day=selected_date, game=game_obj, active=True).exists():
        closed_time_obj = closed_time.objects.filter(day=selected_date, game=game_obj, active=True)

    print(closed_time_obj)

    sold_time_obj = sold_time.objects.none()
    if sold_time.objects.filter(day=selected_date, game=game_obj, active=True).exists():
        sold_time_obj = sold_time.objects.filter(day=selected_date, game=game_obj, active=True)

    

    closed_time_length = len(closed_time_obj)
    sold_time_length = len(sold_time_obj)


    
    
    status = 'time'
    #تبدیل کوعری به جیسون برای جنریت کردن سلکت باکس در فانکشن جی اس
    game_time_json = serialize('json', game_time_obj)

    



    time_closed_id = []
    time_sold_id = []
    for time in closed_time_obj:
        time_closed_id.append(time.game_time.id)
    for time in sold_time_obj:
        time_sold_id.append(time.game_time.id)

    print(time_closed_id)
    print(time_sold_id)

    context = {
        'status' : status,
        'time_closed_id' : time_closed_id,
        'time_sold_id' : time_sold_id,
        'game_time_length' : game_time_length,

        'game_time_json' : game_time_json,
    }

    return JsonResponse(context)

def close_time(request):
    status = 500
    msg = ''
    context = {}

    data = json.loads(request.POST.get('getdata'))
    name = data['name']

    today = jdatetime.datetime.now()
    year = today.strftime('%Y')
    month = today.strftime("%m")
    today_day = today.strftime("%d")
    day = data['day']
    # ایا روز انتخاب شده در این ماه است یا ماه بعد
    if int(today_day) > int(day):
        selected_date = jdatetime.datetime(int(year), int(month)+1,int(day))
    else:
        selected_date = jdatetime.datetime(int(year), int(month),int(day))

    game_obj = game.objects.none()
    if game.objects.filter(fa_name=name, active=True).exists():
        game_obj = game.objects.get(fa_name=name, active=True)

    game_time_obj = game_time.objects.none()
    if game_time.objects.filter(id=data['time'], active=True):
        game_time_obj = game_time.objects.get(id=data['time'], active=True)

    if closed_time.objects.filter(game=game_obj, game_time=game_time_obj, day=selected_date).exists():
        status = 500
        msg = ' این سانس قبلا بسته شده است. '
        context = {
            'status':status,
            'msg':msg,
        }
    else:
        game_time_id = game_time_obj.id
        if sold_time.objects.filter(game=game_obj, game_time=game_time_obj, day=selected_date).exists():
            status = 500
            msg = 'این سانس قبلا فروخته شده است .'
        else:
            status = 200
            msg = 'سانس بسته شد .'
            closed_time.objects.create(
                game=game_obj,
                game_time=game_time_obj,
                day=selected_date,
                active=True
            )
            if today.strftime("%Y-%m-%d") == selected_date.strftime("%Y-%m-%d"):
                game_obj.today_game_times = game_obj.today_game_times - 1
                game_obj.save()
        context = {
            'status':status,
            'msg':msg,
            'game_time_id':game_time_id
        }

    return JsonResponse(context)

def open_time(request):
    status = 500
    msg = ''
    context = {}

    data = json.loads(request.POST.get('getdata'))
    name = data['name']

    today = jdatetime.datetime.now()
    year = today.strftime('%Y')
    month = today.strftime("%m")
    today_day = today.strftime("%d")
    day = data['day']
    # ایا روز انتخاب شده در این ماه است یا ماه بعد
    if int(today_day) > int(day):
        selected_date = jdatetime.datetime(int(year), int(month)+1,int(day))
    else:
        selected_date = jdatetime.datetime(int(year), int(month),int(day))

    game_obj = game.objects.none()
    if game.objects.filter(fa_name=name, active=True).exists():
        game_obj = game.objects.get(fa_name=name, active=True)

    game_time_obj = game_time.objects.none()
    if game_time.objects.filter(id=data['time'], active=True):
        game_time_obj = game_time.objects.get(id=data['time'], active=True)

    if closed_time.objects.filter(game=game_obj, game_time=game_time_obj, day=selected_date).exists():
        if sold_time.objects.filter(game=game_obj, game_time=game_time_obj, day=selected_date).exists():
            status = 500
            msg = 'این سانس قبلا فروخته شده است .'
        else:
            status = 200
            msg = ' سانس باز شد . '
            closed_time.objects.get(game=game_obj, game_time=game_time_obj, day=selected_date).delete()
            game_time_id = game_time_obj.id
            game_time_val = game_time_obj.time_from + ' تا ' + game_time_obj.time_to
            if today.strftime("%Y-%m-%d") == selected_date.strftime("%Y-%m-%d"):
                game_obj.today_game_times = game_obj.today_game_times + 1
                game_obj.save()
        context = {
            'status':status,
            'msg':msg,
            'game_time_id':game_time_id,
            'game_time_val':game_time_val
        }
    else:
        msg = ' این سانس باز است اشتباه انتخاب کرده اید .'
        context = {
            'status':status,
            'msg':msg,
        }

    return JsonResponse(context)

def selling_time(request):
    status = 500
    msg = ''
    context = {}

    data = json.loads(request.POST.get('getdata'))
    name = data['name']

    today = jdatetime.datetime.now()
    year = today.strftime('%Y')
    month = today.strftime("%m")
    today_day = today.strftime("%d")
    day = data['day']
    # ایا روز انتخاب شده در این ماه است یا ماه بعد
    if int(today_day) > int(day):
        selected_date = jdatetime.datetime(int(year), int(month)+1,int(day))
    else:
        selected_date = jdatetime.datetime(int(year), int(month),int(day))

    game_obj = game.objects.none()
    if game.objects.filter(fa_name=name, active=True).exists():
        game_obj = game.objects.get(fa_name=name, active=True)

    game_time_obj = game_time.objects.none()
    if game_time.objects.filter(id=data['time'], active=True):
        game_time_obj = game_time.objects.get(id=data['time'], active=True)

    if sold_time.objects.filter(game=game_obj, game_time=game_time_obj, day=selected_date).exists():
        status = 500
        msg = ' این سانس قبلا فروخته شده است. '
        context = {
            'status':status,
            'msg':msg,
        }
    else:
        
        game_time_id = game_time_obj.id
        if closed_time.objects.filter(game=game_obj, game_time=game_time_obj, day=selected_date).exists():
            status = 500
            msg = 'سانس قبلا بسته شده است ابتدا آن را باز کنید .'
        else:
            status = 200
            msg = 'سانس فروخته شده ثبت شد .'
            sold_time.objects.create(
                game=game_obj,
                game_time=game_time_obj,
                day=selected_date,
                active=True
            )
            if today.strftime("%Y-%m-%d") == selected_date.strftime("%Y-%m-%d"):
                game_obj.today_game_times = game_obj.today_game_times - 1
                game_obj.save()
        context = {
            'status':status,
            'msg':msg,
            'game_time_id':game_time_id
        }

    return JsonResponse(context)

def buy_time(request):
    status = 500
    msg = ''
    context = {}

    data = json.loads(request.POST.get('getdata'))
    name = data['name']

    today = jdatetime.datetime.now()
    year = today.strftime('%Y')
    month = today.strftime("%m")
    today_day = today.strftime("%d")
    day = data['day']
    # ایا روز انتخاب شده در این ماه است یا ماه بعد
    if int(today_day) > int(day):
        selected_date = jdatetime.datetime(int(year), int(month)+1,int(day))
    else:
        selected_date = jdatetime.datetime(int(year), int(month),int(day))

    game_obj = game.objects.none()
    if game.objects.filter(fa_name=name, active=True).exists():
        game_obj = game.objects.get(fa_name=name, active=True)

    game_time_obj = game_time.objects.none()
    if game_time.objects.filter(id=data['time'], active=True):
        game_time_obj = game_time.objects.get(id=data['time'], active=True)

    if sold_time.objects.filter(game=game_obj, game_time=game_time_obj, day=selected_date).exists():
        if closed_time.objects.filter(game=game_obj, game_time=game_time_obj, day=selected_date).exists():
            status = 500
            msg = 'این سانس قبلا بسته شده است .'
        else:
            status = 200
            msg = ' سانس خریده شد شد . '
            sold_time.objects.get(game=game_obj, game_time=game_time_obj, day=selected_date).delete()
            game_time_id = game_time_obj.id
            game_time_val = game_time_obj.time_from + ' تا ' + game_time_obj.time_to
            if today.strftime("%Y-%m-%d") == selected_date.strftime("%Y-%m-%d"):
                game_obj.today_game_times = game_obj.today_game_times + 1
                game_obj.save()
        context = {
            'status':status,
            'msg':msg,
            'game_time_id':game_time_id,
            'game_time_val':game_time_val
        }
    else:
        msg = ' این سانس فروخته نشده است اشتباه انتخاب کرده اید .'
        context = {
            'status':status,
            'msg':msg,
        }

    return JsonResponse(context)

def close_day(request):
    status = 500
    msg = ''
    context = {}

    data = json.loads(request.POST.get('getdata'))
    name = data['name']

    today = jdatetime.datetime.now()
    year = today.strftime('%Y')
    month = today.strftime("%m")
    today_day = today.strftime("%d")
    day = data['day']
    # ایا روز انتخاب شده در این ماه است یا ماه بعد
    if int(today_day) > int(day):
        selected_date = jdatetime.datetime(int(year), int(month)+1,int(day))
    else:
        selected_date = jdatetime.datetime(int(year), int(month),int(day))
    
    game_obj = game.objects.none()
    if game.objects.filter(fa_name=name, active=True).exists():
        game_obj = game.objects.get(fa_name=name, active=True)

    if closed_day.objects.filter(game=game_obj, day=selected_date, active=True).exists():
        status = 500
        msg = 'این روز قبلا بسته شده است .'
    else:
        if sold_time.objects.filter(game=game_obj, day=selected_date, active=True).exists():
            status = 500
            msg = 'در این روز سانسی فروخته شده است .'
        else:
            if selected_date.strftime('%m') > month:
                day = '0'+day
            status = 200
            msg = 'روز بسته شد .'
            closed_day.objects.create(
                game = game_obj,
                day = selected_date,
                active = True
            )
            if today.strftime("%Y-%m-%d") == selected_date.strftime("%Y-%m-%d"):
                game_obj.today_close = True
                game_obj.save()
        context = {
            'status':status,
            'msg':msg,
            'day':day
        }

    return JsonResponse(context)

def open_day(request):
    status = 500
    msg = ''
    context = {}

    data = json.loads(request.POST.get('getdata'))
    name = data['name']

    today = jdatetime.datetime.now()
    year = today.strftime('%Y')
    month = today.strftime("%m")
    today_day = today.strftime("%d")
    day = data['day']
    # ایا روز انتخاب شده در این ماه است یا ماه بعد
    if int(today_day) > int(day):
        selected_date = jdatetime.datetime(int(year), int(month)+1,int(day))
    else:
        selected_date = jdatetime.datetime(int(year), int(month),int(day))
    
    game_obj = game.objects.none()
    if game.objects.filter(fa_name=name, active=True).exists():
        game_obj = game.objects.get(fa_name=name, active=True)

    if closed_day.objects.filter(game=game_obj, day=selected_date, active=True).exists():
        closed_day.objects.filter(game=game_obj, day=selected_date, active=True).delete()
        status = 200
        msg = 'روز باز شد، 3 ثانیه صبر کنید  .'
        if today.strftime("%Y-%m-%d") == selected_date.strftime("%Y-%m-%d"):
            game_obj.today_close = False
            game_obj.save()
    else:
        status = 500
        msg = 'روز بسته نیست اشتباه انتخاب کرده اید .'
        
    context = {
        'status':status,
        'msg':msg,
        'day':day
    }

    return JsonResponse(context)









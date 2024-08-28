from django.shortcuts import render, redirect
from django.http import JsonResponse
import json, random, uuid, jdatetime
from .models import *
from escaperoom.functions import *
from .models import *
from game.models import game_comment, game_reply

def account_validation(request):
    context = {}
    data = json.loads(request.POST.get('getdata'))
    print(data['protocol'])
    if data['protocol'] == 'validation' :

        phonenumber = data['phonenumber']
        if data['length'] == 10 :
            phonenumber = '0' + phonenumber
        print(phonenumber)
        if player_login.objects.filter(phonenumber=phonenumber).exists():
            status = 200
            code = send_code(phonenumber, 'player')
            print(code)
            context = {
                'status' : status,
                'phonenumber' : phonenumber,
            }
        else:
            status = 404
            context = {
                'status' : status,
                'phonenumber' : phonenumber,
            }
    if data['protocol'] == 'code' :
        input_code = data['code']
        phonenumber = data['phonenumber']
        print('hi')
        if validation(input_code, phonenumber, 'player') == True :
            player_login_obj = player_login.objects.get(phonenumber=phonenumber, active=True)
            request.session['player_phonenumber_s'] = player_login_obj.phonenumber
            player_login_obj.last_login = jdatetime.date.today()
            player_login_obj.save()
            status = 200
            url = '/v1/player/'
            context = {
                'status' : status,
                'url' : url
            }
            
        else:
            status = 500
            context = {
                'status' : status,
                'msg' : '*کد وارد شده اشتباه می باشد.'
            }


    return JsonResponse(context)


# first step
def create_user_acc(request):
    print('hello view')
    context = {}
    data = json.loads(request.POST.get('getdata'))
    first_name = data['first_name']
    last_name = data['last_name']
    mail = data['mail']
    password = data['password']
    phonenumber = data['phonenumber']
    if len(phonenumber) == 10 :
        phonenumber = '0' + phonenumber
    print(phonenumber)
    print(type(phonenumber))

    player_login_obj = player_login.objects.create(
        password=password,
        mail=mail,
        phonenumber=phonenumber,
        joined_at=jdatetime.datetime.now(),
        modified_at=jdatetime.datetime.now(),
        last_login=jdatetime.datetime.now(),
        active=True,
    )

    player_info.objects.create(
        player_login=player_login_obj,
        first_name=first_name,
        last_name=last_name,
        complited_at=jdatetime.datetime.now(),
        active=True,
    )
    request.session['player_phonenumber_s'] = player_login_obj.phonenumber
    status = 200
    context = {
        'url':'/v1/player/',
        'status':status
    }
        

    return JsonResponse(context)


def logout_player(request):
    if 'player_phonenumber_s' not in request.session :
        return redirect('landing_page')
    else:
        del request.session['player_phonenumber_s']
        return redirect('/')

def manage_comments(request):
    ul_on = 'comments'
    this_page = 'نظرات'
    if 'player_phonenumber_s' not in request.session:
        return redirect('landing_page')
    else:
        playerlogin_obj = player_login.objects.get(phonenumber = request.session['player_phonenumber_s'], active=True) 
        playerinfo_obj = player_info.objects.get(player_login=playerlogin_obj, active=True)
        
        gamecomments_obj = game_comment.objects.none()
        if game_comment.objects.filter(player_info=playerinfo_obj, active=True).exists():
            gamecomments_obj = game_comment.objects.filter(player_info=playerinfo_obj, active=True)

        gamereplies_obj = game_reply.objects.none()
        if game_reply.objects.filter(game_comment__player_info=playerinfo_obj, active=True).exists():
            gamereplies_obj = game_reply.objects.filter(game_comment__player_info=playerinfo_obj, active=True)

        print(playerinfo_obj.avatar)
        print('playerinfo_obj.avatar')
    
    context = {
            'ul_on' : ul_on,
            'this_page' : this_page,
            'playerlogin' : playerlogin_obj,
            'playerinfo' : playerinfo_obj,
            'comments' : gamecomments_obj,
            'replies' : gamereplies_obj,
        }
    return render(request, 'player/comment/manage_comments.html', context)



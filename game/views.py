from django.shortcuts import render
from .models import *
from brand.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def games(request):
    games_status = 404
    login_status = 404

    playerinfo_obj = player_info.objects.none()
    if 'player_phonenumber_s' not in request.session:
        login_status = 500
    else:
        playerlogin_obj = player_login.objects.get(phonenumber = request.session['player_phonenumber_s'], active=True) 
        playerinfo_obj = player_info.objects.get(player_login=playerlogin_obj, active=True)
        login_status = 200

    games = game.objects.none()
    if game.objects.filter(active=True).exists():
        games = game.objects.filter(active=True)

    game_det = game_details.objects.none()
    if game_details.objects.filter(active=True):
        games_det = game_details.objects.filter(active=True)

    genres = genre.objects.none()
    if genre.objects.filter(active=True).exists():
        genres = genre.objects.filter(active=True)

    game_genres_obj = game_genres.objects.none()
    if game_genres.objects.filter(active=True).exists():
        game_genres_obj = game_genres.objects.filter(active=True)

    brands_obj = brand.objects.none()
    if brand.objects.filter(active=True).exists():
        brand_status = 200
        brands_obj = brand.objects.filter(active=True).order_by('?')

    

    # paginate
    game_page = Paginator(games, 6)
    page_number = request.GET.get('page')
    try:
        games_obj = game_page.get_page(page_number)
    except PageNotAnInteger:
        games_obj = game_page.page(1)
    except EmptyPage:
        games_obj = game_page.page(p.num_pages)

    context = {
        'login_status' : login_status,
        'playerinfo_obj' : playerinfo_obj,

        'brands' : brands_obj,
        'games' : games_obj,
        'games_det' : games_det,
        'game_genres' : game_genres_obj,
        'genres' : genres,
    }

    return render(request, 'base/game/games.html', context)

def game_detail(request, brand_url, game_url):
    status = 404
    login_status = 404

    playerinfo_obj = player_info.objects.none()
    if 'player_phonenumber_s' not in request.session:
        login_status = 500
    else:
        playerlogin_obj = player_login.objects.get(phonenumber = request.session['player_phonenumber_s'], active=True) 
        playerinfo_obj = player_info.objects.get(player_login=playerlogin_obj, active=True)
        login_status = 200


    game_obj = game.objects.none()
    game_det_obj = game_details.objects.none()
    if game.objects.filter(url=game_url, active=True).exists():
        game_obj = game.objects.get(url=game_url, active=True)
        if game_details.objects.filter(game=game_obj, active=True).exists():
            game_det_obj = game_details.objects.get(game=game_obj, active=True)

    brand_obj = brand.objects.none()
    if brand.objects.filter(url=brand_url, active=True).exists():
        brand_obj = brand.objects.get(url=brand_url, active=True)

    othergames = game.objects.none()
    if game.objects.filter(brand=brand_obj, active=True).exists():
        othergames = game.objects.filter(brand=brand_obj, active=True)[:6]


    brands_obj = brand.objects.none()
    if brand.objects.filter(active=True).exists():
        brand_status = 200
        brands_obj = brand.objects.filter(active=True)

    game_genres_obj = game_genres.objects.none()
    if game_genres.objects.filter(game=game_obj, active=True).exists():
        game_genres_obj = game_genres.objects.filter(game=game_obj, active=True)

    comments = game_comment.objects.none()
    if game_comment.objects.filter(game=game_obj, active=True).exists():
        comments = game_comment.objects.filter(game=game_obj, active=True)

    # paginate
    game_page = Paginator(comments, 2)
    page_number = request.GET.get('page')
    try:
        games_obj = game_page.get_page(page_number)
    except PageNotAnInteger:
        games_obj = game_page.page(1)
    except EmptyPage:
        games_obj = game_page.page(p.num_pages)

    replies = game_reply.objects.none()
    if game_reply.objects.filter(game=game_obj, active=True).exists():
        replies = game_reply.objects.filter(game=game_obj, active=True)

    context = {
        'status' : status,
        'login_status' : login_status,
        'playerinfo_obj' : playerinfo_obj,

        'game' : game_obj,
        'game_det' : game_det_obj,
        'othergames' : othergames,
        'brand' : brand_obj,
        'brands' : brands_obj,
        'game_genres' : game_genres_obj,
        'comments' : games_obj,
        'replies' : replies,
    }


    return render(request, 'base/game/game_details.html', context)


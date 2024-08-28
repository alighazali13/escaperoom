from django.shortcuts import render
from .models import *
from brand.models import brand
from game.models import *
import jdatetime, datetime, random
from .functions import *


def landing_page(request):
    
    reset_code_sent()

    login_status = 404
    banner_header_status = 404
    slides_status = 404
    adv_banner_top_status = 404
    adv_banner_bottom_status = 404
    adv_slide_status = 404
    brand_status = 404
    two_days_later_status = 404
    cinema_status = 404
    games_status = 404
    allgames_status = 404

    if 'player_phonenumber_s' not in request.session:
        login_status = 500
    else:
        playerlogin_obj = player_login.objects.get(phonenumber = request.session['player_phonenumber_s'], active=True) 
        playerinfo_obj = player_info.objects.get(player_login=playerlogin_obj, active=True)
        login_status = 200


    today_date = jdatetime.date.today()
    time = jdatetime.datetime.now().strftime("%H:%M:%S")
    
    banner_header_obj = banner_header.objects.none()
    if banner_header.objects.filter(active=True).exists():
        banner_header_status = 200
        banner_header_obj = banner_header.objects.get(active=True)

    slides_obj = slides.objects.none()
    if slides.objects.filter(active=True).exists():
        slides_status = 200
        slides_obj = slides.objects.filter(active=True).order_by('-id')

    adv_banner_top_obj = advertising_banner.objects.none()
    if advertising_banner.objects.filter(number=0, active=True).exists():
        adv_banner_top_status = 200
        adv_banner_top_obj = advertising_banner.objects.get(number=0, active=True)

    adv_banner_bottom_obj = advertising_banner.objects.none()
    if advertising_banner.objects.filter(number=1, active=True).exists():
        adv_banner_bottom_status = 200
        adv_banner_bottom_obj = advertising_banner.objects.get(number=1, active=True)

    adv_slide_obj = advertising_slide.objects.none()
    if advertising_slide.objects.filter(active=True).exists():
        adv_slide_status = 200
        adv_slide_obj = advertising_slide.objects.filter(active=True)
    
    brands_obj = brand.objects.none()
    brands = brand.objects.none()
    condition = True
    if brand.objects.filter(active=True).exists():
        brand_status = 200
        brands_obj = brand.objects.filter(active=True).order_by('?')

            

    time_left = ''
    two_days_later_obj = two_days_later.objects.none()
    if two_days_later.objects.filter(enable_date=today_date, active=True).exists():
        two_days_later_status = 200
        two_days_later_obj = two_days_later.objects.filter(enable_date=today_date, active=True)
        now = jdatetime.datetime.now()
        end_of_day = jdatetime.datetime(now.year, now.month, now.day) + jdatetime.timedelta(days=1)
        time_left = (end_of_day - now).total_seconds()
        print(time_left)
        print('time_left')


    # cinema
    cinemas = game.objects.none()
    game_types = game_type.objects.get(en_name='cinema of fear', active=True)
    if game.objects.filter(game_type=game_types, active=True).exists():
        cinema_status = 200
        cinemas = game.objects.filter(game_type=game_types, active=True)
        print(cinemas)

    
    # today
    free_games = get_free_for_book()
    games = game.objects.none()
    for free_game in free_games :
        if game.objects.filter(game_type__fa_name='اسکیپ روم', active=True).exists():
            games_status = 200
            games = game.objects.filter(game_type__fa_name='اسکیپ روم', active=True)[:6]

    # all active game 
    allgames = game.objects.none()
    first_row = game.objects.none()
    second_row = game.objects.none()
    third_row = game.objects.none()
    selected_game = []
    condition = True
    if game.objects.filter(game_type=0, active=True).exists():
        allgames = game.objects.filter(game_type=0, active=True)
        games_lenght = len(allgames)
        while condition:
            random_int = random.randint(1, games_lenght)
            if games_lenght >= 12:
                if len(first_row) <= 3 :
                    if random_int not in selected_game :
                        # |= append to queryset
                        first_row |= (game.objects.filter(gameID=random_int, active=True))
                        selected_game.append(random_int)
                if len(first_row) == 4:
                    if len(second_row) <= 3:
                        if random_int not in selected_game :
                            second_row |= (game.objects.filter(gameID=random_int, active=True))
                            selected_game.append(random_int)
                    if len(second_row) == 4:
                        if len(third_row) <= 3:
                            if random_int not in selected_game :
                                third_row |= (game.objects.filter(gameID=random_int, active=True))
                                selected_game.append(random_int)

                        if len(third_row) == 4:
                            allgames_status = 200
                            condition = False

    game_genres_obj = game_genres.objects.none() 
    if game_genres.objects.filter(active=True).exists():
        game_genres_obj = game_genres.objects.filter(active=True)
                
            
        


    context = {
        'login_status': login_status,
        'banner_header_status': banner_header_status,
        'banner_header': banner_header_obj,
        'slides_status': slides_status,
        'slides': slides_obj,
        'adv_banner_top_status': adv_banner_top_status,
        'adv_top_banner': adv_banner_top_obj,
        'adv_banner_bottom_status': adv_banner_bottom_status,
        'adv_bottom_banner': adv_banner_bottom_obj,
        'adv_slide_status': adv_slide_status,
        'adv_slides': adv_slide_obj,

        'playerinfo_obj': playerinfo_obj,

        'brand_status': brand_status,
        'brands': brands_obj,

        'two_day_status' : two_days_later_status,
        'two_day_games' : two_days_later_obj,
        'time_left' : time_left,

        'cinema_status' : cinema_status,
        'cinemas' : cinemas,

        'games_status' : games_status,
        'games' : games,

        'first_row' : first_row,
        'second_row' : second_row,
        'third_row' : third_row,

        'game_genres' : game_genres_obj
    }

    return render(request, 'base/index.html', context)

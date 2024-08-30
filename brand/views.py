from django.shortcuts import render, redirect
from .models import *
from game.models import *

def brand_details(request, url):
    status = 404
    slider_status = 404
    games_status = 404

    playerinfo_obj = player_info.objects.none()
    if 'player_phonenumber_s' not in request.session:
        login_status = 500
    else:
        playerlogin_obj = player_login.objects.get(phonenumber = request.session['player_phonenumber_s'], active=True) 
        playerinfo_obj = player_info.objects.get(player_login=playerlogin_obj, active=True)
        login_status = 200

    brands_obj = brand.objects.none()
    if brand.objects.filter(active=True).exists():
        brand_status = 200
        brands_obj = brand.objects.filter(active=True).order_by('?')

    brand_obj = brand.objects.none()
    brand_slides_obj = brand_slide.objects.none()
    othergames = game.objects.none()

    if brand.objects.filter(url = url).exists():
        status = 200
        brand_obj = brand.objects.get(url = url)
        
        if game.objects.filter(brand=brand_obj, active=True).exists():
            games_status = 200
            othergames = game.objects.filter(brand=brand_obj, active=True)[:6]

        if brand_slide.objects.filter(brand = brand_obj, active=True).exists():
            slider_status = 200
            brand_slides_obj = brand_slide.objects.filter(brand = brand_obj, active=True)
    else:
        return redirect('/')

    context = {
        'login_status' : login_status,
        'playerinfo_obj' : playerinfo_obj,
        
        'brand' : brand_obj,
        
        'brands' : brands_obj,
        
        'slider_status' : slider_status,
        'slides' : brand_slides_obj,
        
        'games_status' : games_status,
        'games' : othergames,
    }
    return render(request, 'base/brand/brand_details.html', context)
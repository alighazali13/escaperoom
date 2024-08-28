from django.shortcuts import render, redirect
from .models import *
from game.models import *

def brand_details(request, url):
    status = 404
    slider_status = 404
    games_status = 404

    

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
        'brand' : brand_obj,
        
        'brands' : brands_obj,
        
        'slider_status' : slider_status,
        'slides' : brand_slides_obj,
        
        'games_status' : games_status,
        'games' : othergames,
    }
    return render(request, 'base/brand/brand_details.html', context)
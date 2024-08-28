from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
import uuid, json, random, jdatetime
from .models import *
from .forms import *
from brand.models import brand
from brand.forms import *
from game.models import *
from game.forms import *
from escaperoom.models import *
from escaperoom.fomrs import *
from escaperoom.functions import *
from player.models import *

def login_admin(request):

    return render(request, 'adminstrator/login.html')

def logout_admin(request):
    if 'admin_phonenumber_s' not in request.session :
        return redirect('login_admin')
    else:
        del request.session['admin_phonenumber_s']
        return redirect('/')

def account_validation(request):
    context = {}
    data = json.loads(request.POST.get('getdata'))
    print(data['protocol'])
    if data['protocol'] == 'validation' :

        phonenumber = data['phonenumber']

        if admin_login.objects.filter(phonenumber=phonenumber).exists():
            status = 200
            code = send_code(phonenumber, 'admin')
            print(code)
            print('code1')
            context = {
            'status' : status,
            'phonenumber' : phonenumber,
            }
        else:
            status = 404
            context = {
                'status' : status,
                'msg' : 'حساب کاربری با این شماره پیدا نشد.'
            }
    if data['protocol'] == 'code' :
        input_code = data['code']
        phonenumber = data['phonenumber']
        if validation(input_code, phonenumber, 'admin') == True :
            admin_login_obj = admin_login.objects.get(phonenumber=phonenumber, active=True)
            request.session['admin_phonenumber_s'] = admin_login_obj.phonenumber
            admin_login_obj.last_login = jdatetime.date.today()
            admin_login_obj.save()
            status = 200
            url = '/v1/admin/strator/'
            context = {
                'status' : status,
                'url' : url
            }
            
        else:
            status = 500
            context = {
                'status' : status,
                'msg' : 'کد وارد شده اشتباه می باشد.'
            }


    return JsonResponse(context)


def ur_brand(request):
    ul_on = 'dashboard'
    li_on = 'ur_brand'
    parent_page = ''
    this_page = 'مدیریت مجموعه '
    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'
        parent_page = brand_obj.en_name

        form = brand_form(instance = brand_obj)
        if request.POST:
            if 'edit_brand_BTN' in request.POST:
                fa_name = request.POST.get('fa_name', 'null')
                print(fa_name)
                en_name = request.POST.get('en_name', 'null')
                print(en_name)
                big_logo = request.FILES.get('big_logo', 'null')
                print(big_logo)
                sm_logo = request.FILES.get('sm_logo', 'null')
                print(sm_logo)
                descriptions = request.POST.get('descriptions', 'null')
                print(descriptions)
                url = request.POST.get('url', 'null')
                print(url)
                if fa_name != 'null' : brand_obj.fa_name = fa_name
                if en_name != 'null' : brand_obj.en_name = en_name
                if big_logo != 'null' : brand_obj.big_logo = big_logo
                if sm_logo != 'null' : brand_obj.sm_logo = sm_logo
                if descriptions != 'null' : brand_obj.descriptions = descriptions
                if url != 'null' : brand_obj.url = url
                brand_obj.save()
                return redirect(ur_brand)

    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'form' : form,
        'brand' : brand_obj,
    }

    return render(request, 'adminstrator/brands/ur_brand.html', context)

def ur_games(request):
    ul_on = 'dashboard'
    li_on = 'ur_games'
    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'
        parent_page = brand_obj.en_name
        this_page = 'مدیریت بازی های شما'
        games = game.objects.none()
        if game.objects.filter(brand=brand_obj, active=True).exists():
            games = game.objects.filter(brand=brand_obj, active=True)

        games_det = game_details.objects.none()
        if game_details.objects.filter(active=True).exists():
            games_det = game_details.objects.filter(active=True)


    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'games' : games,
        'games_det' : games_det,

    }

    return render(request, 'adminstrator/hobby/ur_games.html', context)

def ur_booking(request, slug):
    ul_on = 'dashboard'
    li_on = 'ur_games'
    parent_page = ''
    this_page = ''
    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'

        parent_page = brand_obj.en_name
        today_date = jdatetime.date.today()

        game_obj = game.objects.none()
        if game.objects.filter(brand=brand_obj, active=True).exists():
            game_obj = game.objects.get(brand=brand_obj, slug=slug)
            this_page = game_obj.fa_name
        
        game_det = game_details.objects.none()
        if game_details.objects.filter(game=game_obj, active=True).exists():
            game_det = game_details.objects.get(game=game_obj, active=True)

       
        game_times = game_time.objects.none()
        if game_time.objects.filter(game=game_obj, active=True).exists():
            game_times = game_time.objects.filter(game=game_obj, active=True)

        closed_times = closed_time.objects.none()
        if closed_time.objects.filter(game=game_obj,active=True).exists():
            closed_times = closed_time.objects.filter(game=game_obj,active=True)


    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,
        'today_date' : today_date,


        'game_obj' : game_obj,
        'game_det' : game_det,
        'game_times' : game_times,
        'closed_times' : closed_times,

    }

    return render(request, 'adminstrator/hobby/booking.html', context)

def ur_admins(request):
    ul_on = 'dashboard'
    li_on = 'ur_admins'
    parent_page = ''
    this_page = 'مدیریت ادمین ها'
    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'
        parent_page = brand_obj.en_name

        adminlogins_obj = admin_login.objects.none()
        if admin_login.objects.filter(brand=brand_obj, active=True).exists():
            adminlogins_obj = admin_login.objects.filter(brand=brand_obj, active=True).exclude(phonenumber=adminlogin_obj.phonenumber)


        admininfos_obj = admin_info.objects.none()
        if admin_info.objects.filter(active=True).exists():
            admininfos_obj = admin_info.objects.filter(active=True).exclude(admin_login=adminlogin_obj)


    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'adminlogins' : adminlogins_obj,
        'admininfos' : admininfos_obj,
    }

    return render(request, 'adminstrator/admins/ur_admins.html', context)

def ur_slides(request):
    ul_on = 'dashboard'
    li_on = 'ur_slides'
    parent_page = ''
    this_page = 'مدیریت اسلاید ها'
    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'
        parent_page = brand_obj.en_name

        brand_slides_obj = brand_slide.objects.none()
        if brand_slide.objects.filter(brand=brand_obj, active=True).exists:
            brand_slides_obj = brand_slide.objects.filter(brand=brand_obj, active=True)

        form = sliders_form()
        if request.POST:
            if 'add_brand_slider_BTN' in request.POST:
                slide = request.FILES.get('slide', 'null')
                brand_slide.objects.create(
                    brand=brand_obj,
                    slide=slide,
                    active=True,
                )

    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,
        
        'form' : form,

        'brand_slides' : brand_slides_obj,
    }

    return render(request, 'adminstrator/brands/ur_slides.html', context)


def statistics(request):
    ul_on = 'statistics'
    # li_on = ''
    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        parent_page = brand_obj.en_name
        this_page = 'آمار'

        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'

        


    context = {
        'ul_on' : ul_on,
        # 'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,
    }

    return render(request, 'adminstrator/statistics.html', context)

def genre_am(request):
    ul_on = 'setting'
    li_on = 'genre'
    parent_page = 'داشبورد'
    this_page = 'ژانر'

    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'
        form = genre_form()
        if request.POST:
            if 'add_genre_BTN' in request.POST:
                fa_name = request.POST.get('fa_name', 'null')
                en_name = request.POST.get('en_name', 'null')
                genre.objects.create(
                    fa_name = fa_name,
                    en_name = en_name
                )
        
        genres = genre.objects.none()
        if genre.objects.filter(active=True).exists():
            genres = genre.objects.filter(active=True)



    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'form' : form,

        'genres' : genres,



    }

    return render(request, 'adminstrator/hobby/genre.html', context)

def twodayslater(request):
    ul_on = 'setting'
    li_on = 'twodayslater'
    parent_page = 'داشبورد'
    this_page = 'دو روز بعد'

    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'

        games_obj = game.objects.none()
        if game.objects.filter(brand=brand_obj, active=True).exists():
            games_obj = game.objects.filter(brand=brand_obj, active=True)
        
        twodayslatergames = two_days_later.objects.none()
        if two_days_later.objects.filter(active=True).exists():
            twodayslatergames = two_days_later.objects.filter(active=True).order_by('-enable_date')

        if request.POST:
            if 'add_twodayslater_BTN' in request.POST:
                enable_date = request.POST.get('datepicker_twodaysgames', 'null')
                enable_date = jdatetime.datetime.strptime(enable_date, '%Y/%m/%d')
                print(type(enable_date))
                game_obj = game.objects.get(id=request.POST.get('game', 'null'))
                game_det = game_details.objects.get(game=game_obj)
                two_days_later.objects.create(
                    enable_date = enable_date,
                    game = game_obj,
                    game_details = game_det,
                    active=True
                )
                return redirect(twodayslater)
        




    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,


        'games_obj' : games_obj,
        'twodayslatergames' : twodayslatergames,
    }

    return render(request, 'adminstrator/hobby/twodayslater.html', context)

def banners(request):
    ul_on = 'setting'
    li_on = 'banners'
    parent_page = 'داشبورد'
    this_page = 'بنرها'

    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'

        # banner header 
        banner_header_obj = banner_header.objects.none()
        if banner_header.objects.filter(active=True).exists():
            banner_header_obj = banner_header.objects.filter(active=True).order_by('-id')

        banner_headerform = banner_header_form()
        if request.POST:
            if 'add_banner_header_BTN' in request.POST:
                name = request.POST.get('name', 'null')
                url = request.POST.get('url', 'null')
                slide = request.FILES.get('slide', 'null')
                banner_header.objects.create(
                    admin_login=adminlogin_obj,
                    name=name,
                    url=url,
                    slide=slide,
                    active=True
                )
        
        # slider header 
        header_slider_obj = slides.objects.none()
        if slides.objects.filter(active=True).exists():
            header_slider_obj = slides.objects.filter(active=True).order_by('-id')

        slidersform = sliders_form()
        if request.POST:
            if 'add_header_slider_BTN' in request.POST:
                name = request.POST.get('name', 'null')
                url = request.POST.get('url', 'null')
                slide = request.FILES.get('slide', 'null')
                slides.objects.create(
                    admin_login=adminlogin_obj,
                    name=name,
                    url=url,
                    slide=slide,
                    active=True
                )
        

        # adv_banner
        adv_banner_obj = advertising_banner.objects.none()
        if advertising_banner.objects.filter(active=True).exists():
            adv_banner_obj = advertising_banner.objects.filter(active=True)
        
        adv_bannerform = advbanner_form()
        if request.POST:
            if 'add_adv_banner_BTN' in request.POST:
                name = request.POST.get('adv_banner_name', 'null')
                url = request.POST.get('adv_banner_url', 'null')
                slide = request.FILES.get('adv_banner_slide', 'null')
                number = request.POST.get('number', 'null')
                
                advertising_banner.objects.create(
                    number = number,
                    admin_login = adminlogin_obj,
                    adv_banner_name = name,
                    adv_banner_url = url,
                    adv_banner_slide = slide,
                    active = True
                )
        

        # adv_slide
        adv_slide_obj = advertising_slide.objects.none()
        if advertising_slide.objects.filter(active=True).exists():
            adv_slide_obj = advertising_slide.objects.filter(active=True)
        
        adv_slideform = advslide_form()
        if request.POST:
            if 'add_adv_slide_BTN' in request.POST:
                name = request.POST.get('adv_slide_name', 'null')
                url = request.POST.get('adv_slide_url', 'null')
                slide = request.FILES.get('adv_slide_slide', 'null')
                
                advertising_slide.objects.create(
                    admin_login = adminlogin_obj,
                    adv_slide_name = name,
                    adv_slide_url = url,
                    adv_slide_slide = slide,
                    active = True
                )

    

    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'banner_header' : banner_header_obj,
        'banner_headerform' : banner_headerform,

        'header_slider' : header_slider_obj,
        'sliders_form' : slidersform,

        'adv_banner' : adv_banner_obj,
        'adv_banner_form' : adv_bannerform,

        'adv_slide' : adv_slide_obj,
        'adv_slide_form' : adv_slideform,




    }

    return render(request, 'adminstrator/banners.html', context)


def manage_brands(request):
    ul_on = 'brands'
    li_on = 'manage_brand'
    parent_page = 'مجموعه ها'
    this_page = 'مدیریت مجموعه ها'

    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'

        brands = brand.objects.none()
        if brand.objects.filter(active=True):
            brands = brand.objects.filter(active=True)

        admin_login_obj = admin_login.objects.none()
        if admin_login.objects.filter(active=True).exists():
            admin_login_obj = admin_login.objects.filter(active=True)
        admin_info_obj = admin_info.objects.none()
        if admin_info.objects.filter(active=True).exists():
            admin_info_obj = admin_info.objects.filter(active=True)
    

    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'brands' : brands,
        'admin_login' : admin_login_obj,
        'admin_info' : admin_info_obj,


    }

    return render(request, 'adminstrator/brands/manage_brands.html', context)

def add_brand(request):
    ul_on = 'brands'
    li_on = 'add_brand'
    parent_page = 'مجموعه ها'
    this_page = 'اضافه کردن مجموعه'

    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'
        
        admininfos_obj = admin_info.objects.none()
        if admin_info.objects.filter(active=True, admin_login__admin_type=admin_type_choices.collector):
            admininfos_obj = admin_info.objects.filter(active=True, admin_login__admin_type=admin_type_choices.collector)
        print(admininfos_obj)
        form = brand_form()
        if request.POST:
            if 'add_brand_BTN' in request.POST:
                fa_name = request.POST.get('fa_name', 'null')
                en_name = request.POST.get('en_name', 'null')
                url = request.POST.get('url', 'null')
                big_logo = request.FILES.get('big_logo', 'null')
                sm_logo = request.FILES.get('sm_logo', 'null')
                descriptions = request.POST.get('descriptions', 'null')
                if fa_name != 'null' and en_name != 'null' and url != 'null' and big_logo != 'null' and sm_logo != 'null' and descriptions != 'null':
                    brand.objects.create(
                        fa_name = fa_name,
                        en_name = en_name,
                        url = url,
                        big_logo = big_logo,
                        sm_logo = sm_logo,
                        descriptions = descriptions,
                        active=True
                    )

    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'admininfos' : admininfos_obj,
        'form' : form,

    }

    return render(request, 'adminstrator/brands/add_brand.html', context)


def manage_scaperoom(request):
    ul_on = 'scaperoom'
    li_on = 'manage_escaperoom'
    parent_page = 'اتاق فرار ها'
    this_page = 'مدیریت کردن اتاق فرار'
    hobby_type = ' اتاق فرار '

    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'
    
    gamesdet_obj = game_details.objects.none()
    if game_details.objects.filter(active=True).exists():
        gamesdet_obj = game_details.objects.filter(active=True)

    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'games_det' : gamesdet_obj,
    }

    return render(request, 'adminstrator/hobby/manage_hobby.html', context)

def add_escaperoom(request):
    ul_on = 'scaperoom'
    li_on = 'add_escaperoom'
    parent_page = 'اتاق فرار ها'
    this_page = 'اضافه کردن اتاق فرار'
    hobby_type = ' اتاق فرار '

    gameform = game_form()
    gamedetform = game_det_form()
    gametimeform =  game_time_form()

    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'
        admin_info_obj = admin_info.objects.get(admin_login=adminlogin_obj, active=True)

        genres_obj = genre.objects.none()
        if genre.objects.filter(active=True).exists():
            genres_obj = genre.objects.filter(active=True)

        if request.POST:
            if 'add_hobby_BTN' in request.POST:
                poster = request.FILES.get('poster', 'null')
                teaser = request.FILES.get('teaser', 'null')
                full_address = request.POST.get('full_address', 'null')
                short_address = request.POST.get('short_address', 'null')
                fa_name = request.POST.get('fa_name', 'null')
                en_name = request.POST.get('en_name', 'null')
                url = request.POST.get('url', 'null')
                brand_obj = brand.objects.get(id=int(request.POST.get('brand', 'null')))
                price = request.POST.get('price', 'null')
                age = request.POST.get('age', 'null')
                hardship = request.POST.get('hardship', 'null')
                player_from = request.POST.get('player_from', 'null')
                player_to = request.POST.get('player_to', 'null')
                time = request.POST.get('time', 'null')
                roles = request.POST.get('roles', 'null')
                descriptions = request.POST.get('descriptions', 'null')
                unique_description = request.POST.get('unique_description', 'null')
                scenario = request.POST.get('scenario', 'null')

                if game.objects.filter().exists():
                    latest = game.objects.filter().last()
                    if teaser != 'null' :
                        game_obj = game.objects.create(
                            gameID = latest.gameID + 1,
                            brand = brand_obj,
                            admin = admin_info_obj,
                            game_type = game_type.objects.get(en_name='escaperoom', active=True),
                            fa_name = fa_name,
                            en_name = en_name,
                            scenario = scenario,
                            roles = roles,
                            descriptions = descriptions,
                            unique_description = unique_description,
                            teaser = teaser,
                            poster = poster,
                            price = price,
                            url = url,
                        )
                    if teaser == 'null':
                        game_obj = game.objects.create(
                            gameID = latest.gameID + 1,
                            brand = brand_obj,
                            admin = admin_info_obj,
                            game_type = game_type.objects.get(en_name='escaperoom', active=True),
                            fa_name = fa_name,
                            en_name = en_name,
                            scenario = scenario,
                            roles = roles,
                            descriptions = descriptions,
                            unique_description = unique_description,
                            poster = poster,
                            price = price,
                            url = url,
                        )

                else:
                    if teaser != 'null' :
                        game_obj = game.objects.create(
                            gameID = 1,
                            brand = brand_obj,
                            admin = admin_info_obj,
                            game_type = game_type.objects.get(en_name='escaperoom', active=True),
                            fa_name = fa_name,
                            en_name = en_name,
                            scenario = scenario,
                            roles = roles,
                            descriptions = descriptions,
                            unique_description = unique_description,
                            teaser = teaser,
                            poster = poster,
                            price = price,
                            url = url,
                        )
                    if teaser == 'null':
                        game_obj = game.objects.create(
                            gameID = 1,
                            brand = brand_obj,
                            admin = admin_info_obj,
                            game_type = game_type.objects.get(en_name='escaperoom', active=True),
                            fa_name = fa_name,
                            en_name = en_name,
                            scenario = scenario,
                            roles = roles,
                            descriptions = descriptions,
                            unique_description = unique_description,
                            poster = poster,
                            price = price,
                            url = url,
                        )
                
                gamedet_obj = game_details.objects.create(
                    game = game_obj,
                    age = age,
                    hardship = hardship,
                    player_from = player_from,
                    player_to = player_to,
                    time = time,
                    short_address = short_address,
                    full_address = full_address,
                )
                game_obj.active = True
                game_obj.save()

                # ژانر
                genresID = request.POST.getlist('genres', 'null')
                for genreID in genresID :
                    genre_obj = genre.objects.get(id=genreID, active=True)
                    game_genres.objects.create(
                        genre = genre_obj,
                        game = game_obj,
                    )

                # سانس بندی
                selected = request.POST.get('selectedinp', 'null')
                if selected != 'null':
                    selected_list = selected.split('_')
                    for inpID in selected_list:
                        time_from = request.POST.get('from_'+inpID, 'null')
                        time_to = request.POST.get('to_'+inpID, 'null')
                        if time_from != 'null' and time_to != 'null':
                            game_time.objects.create(
                                game = game_obj,
                                time_from = time_from,
                                time_to = time_to,
                            )
            

    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'game_form' : gameform,
        'game_det_form' : gamedetform,
        'game_time_form' : gametimeform,

        'genres' : genres_obj,
    }

    return render(request, 'adminstrator/hobby/add_hobby.html', context)


def manage_players(request):
    ul_on = 'users'
    li_on = 'manage_users'
    parent_page = ' کاربران '
    this_page = 'مدیریت کاربران'

    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'

        players_info_obj = player_info.objects.none()
        if player_info.objects.filter(active=True).exists():
            players_info_obj = player_info.objects.filter(active=True)


    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'players_info' : players_info_obj,
    }

    return render(request, 'adminstrator/players/manage_players.html', context)


def manage_admins(request):
    ul_on = 'admins'
    li_on = 'manage_admins'
    parent_page = 'ادمین ها'
    this_page = 'مدیریت ادمین ها'

    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'   

        admin_info_obj = admin_info.objects.none()
        if admin_info.objects.filter(active=True).exists():
            admin_info_obj = admin_info.objects.filter(active=True)

        admin_login_obj = admin_info.objects.none()
        if admin_login.objects.filter(active=True).exists():
            admin_login_obj = admin_login.objects.filter(active=True)


    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'admin_infos' : admin_info_obj,
        'admin_logins' : admin_login_obj,

    }

    return render(request, 'adminstrator/admins/manage_admins.html', context)

def add_admin(request):
    ul_on = 'admins'
    li_on = 'add_admin'
    parent_page = 'ادمین ها'
    this_page = 'اضافه کردن ادمین'

    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'

        admininfo_form = admin_info_form()
        adminlogin_form = admin_login_form()
        if request.POST:
            if 'add_admin_BTN' in request.POST:
                first_name = request.POST.get('first_name', 'null')
                last_name = request.POST.get('last_name', 'null')
                gender = request.POST.get('gender', 'null')
                password = request.POST.get('password', 'null')
                phonenumber = request.POST.get('phonenumber', 'null')
                admin_type = request.POST.get('admin_type', 'null')
                brandID = int(request.POST.get('brand', 'null'))
                if first_name != 'null' and last_name != 'null' and password != 'null' and phonenumber != 'null' :
                    if brand.objects.filter(id=brandID).exists():
                        brand_obj = brand.objects.get(id=brandID)
                        adminlogin_obj =  admin_login.objects.create(
                            password = password,
                            phonenumber = phonenumber,
                            admin_type = admin_type,
                            brand = brand_obj,
                        )
                        
                        admin_info_obj = admin_info.objects.create(
                            admin_login = adminlogin_obj,
                            first_name = first_name,
                            last_name = last_name,
                            gender = gender,
                            active = True
                        )
                        adminlogin_obj.active = True
                        adminlogin_obj.save()
                        brand_obj.active = True
                        brand_obj.save()



    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'admin_info_form' : admininfo_form,
        'admin_login_form' : adminlogin_form,

    }

    return render(request, 'adminstrator/admins/add_admin.html', context)


def manage_comments(request):
    ul_on = 'comments'
    li_on = 'manage_comments'
    parent_page = 'کامنت ها'
    this_page = 'مدیریت کامنت ها'

    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        adminlogin_obj = admin_login.objects.get(phonenumber = request.session['admin_phonenumber_s'], active=True) 
        brand_obj = adminlogin_obj.brand
        admininfo_obj = admin_info.objects.get(admin_login=adminlogin_obj, active=True)
        
        if adminlogin_obj.admin_type == admin_type_choices.core:
            base_template = 'adminstrator/masterpage.html'
        if adminlogin_obj.admin_type == admin_type_choices.collector:
            base_template = 'adminstrator/masterpage_collector.html'
        if adminlogin_obj.admin_type == admin_type_choices.personel:
            base_template = 'adminstrator/masterpage_personel.html'

        comments_obj = game_comment.objects.none()
        if game_comment.objects.filter(game__brand=brand_obj).exists():
            comments_obj = game_comment.objects.filter(game__brand=brand_obj)

        replies_obj = game_reply.objects.none()
        if game_reply.objects.filter(game__brand=brand_obj).exists():
            replies_obj = game_reply.objects.filter(game__brand=brand_obj)

        if request.POST:
            if 'add_reply_BTN' in request.POST:
                reply = request.POST.get('reply', 'null')
                comment_obj = game_comment.objects.get(id=request.POST.get('comment_id'))
                game_reply.objects.create(
                    game = comment_obj.game,
                    game_comment = comment_obj,
                    admin_info = admininfo_obj,
                    reply = reply,
                    active=True
                )

    context = {
        'ul_on' : ul_on,
        'li_on' : li_on,
        'parent_page' : parent_page,
        'this_page' : this_page,
        'urbrand' : brand_obj,
        'adminlogin' : adminlogin_obj,
        'base_template' : base_template,

        'comments' : comments_obj,
        'replies' : replies_obj,

    }

    return render(request, 'adminstrator/hobby/manage_comments.html', context)





def delete_game(request, slug):
    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        game_object = game.objects.none()
        if game.objects.filter(slug=slug, active=True).exists():
            game.objects.filter(slug=slug, active=True).delete()

        return HttpResponseRedirect(request.path)


def delete_brand(request, slug):
    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        brand_object = brand.objects.none()
        if brand.objects.filter(slug=slug, active=True).exists():
            brand.objects.filter(slug=slug, active=True).delete()

        return HttpResponseRedirect(request.path)


def active_comment(request, slug):
    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        comment_object = game_comment.objects.none()
        if game_comment.objects.filter(slug=slug, active=False).exists():
            comment_obj = game_comment.objects.get(slug=slug, active=False)
            comment_obj.active = True
            comment_obj.save()

        return redirect(manage_comments)

def deactive_comment(request, slug):
    if 'admin_phonenumber_s' not in request.session:
        return redirect('login_admin')
    else:
        comment_object = game_comment.objects.none()
        if game_comment.objects.filter(slug=slug, active=True).exists():
            comment_obj = game_comment.objects.get(slug=slug, active=True)
            comment_obj.active = False
            comment_obj.save()

        return redirect(manage_comments)


from django.db import models
from adminstrator.models import admin_login
from brand.models import brand
from django.utils.translation import gettext as _
import uuid


def home_slide_image_path(instance, filename):
    
    if ' ' in instance.name:
        name = instance.name.replace(' ','-')
        filename = 'h_' + uuid.uuid4().hex + instance.name + '.webp'
    if '_' in instance.name:
        name = instance.name.replace('_','-')
        filename = 'h_' + uuid.uuid4().hex + instance.name + '.webp'
    else:
        name = instance.name
        filename = 'h_' + uuid.uuid4().hex + instance.name + '.webp'
    filename = 'h_' + uuid.uuid4().hex + instance.name + '.webp'
    return 'landing/Images/slides/{0}'.format(filename)

class slides(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    admin_login = models.ForeignKey(admin_login, on_delete=models.CASCADE)
    name = models.CharField(_( 'eng slide name' ), max_length=100)
    url = models.CharField(_( 'url slide' ), max_length=100)
    slide = models.ImageField(upload_to=home_slide_image_path)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


def banner_header_image_path(instance, filename):
    
    if ' ' in instance.name:
        name = instance.name.replace(' ','-')
        filename = 'bh_' + uuid.uuid4().hex + instance.name + '.webp'
    if '_' in instance.name:
        name = instance.name.replace('_','-')
        filename = 'bh_' + uuid.uuid4().hex + instance.name + '.webp'
    else:
        name = instance.name
        filename = 'bh_' + uuid.uuid4().hex + instance.name + '.webp'
    filename = 'bh_' + uuid.uuid4().hex + instance.name + '.webp'
    return 'landing/Images/header_banner/{0}'.format(filename)

class banner_header(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    admin_login = models.ForeignKey(admin_login, on_delete=models.CASCADE)
    name = models.CharField(_( 'eng slide name' ), max_length=100)
    url = models.CharField(_( 'url slide' ), max_length=100)
    slide = models.ImageField(upload_to=home_slide_image_path)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


def advertising_banner_image_path(instance, filename):
    
    if ' ' in instance.adv_banner_name:
        name = instance.adv_banner_name.replace(' ','-')
        filename = 'h_' + uuid.uuid4().hex + instance.adv_banner_name + '.webp'
    if '_' in instance.adv_banner_name:
        name = instance.adv_banner_name.replace('_','-')
        filename = 'h_' + uuid.uuid4().hex + instance.adv_banner_name + '.webp'
    else:
        name = instance.adv_banner_name
        filename = 'h_' + uuid.uuid4().hex + instance.adv_banner_name + '.webp'
    filename = 'h_' + uuid.uuid4().hex + instance.adv_banner_name + '.webp'
    return 'landing/Images/advertising_banner/{0}'.format(filename)

class place_choices(models.IntegerChoices):
    top = 0 ,
    bottom = 1 ,

class advertising_banner(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    number = models.IntegerField(default=place_choices.top, choices=place_choices.choices)
    admin_login = models.ForeignKey(admin_login, on_delete=models.CASCADE)
    adv_banner_name = models.CharField(_( 'eng slide name' ), max_length=100)
    adv_banner_url = models.CharField(_( 'url slide' ), max_length=100)
    adv_banner_slide = models.ImageField(upload_to=advertising_banner_image_path)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.adv_banner_name


def advertising_slide_image_path(instance, filename):
    
    if ' ' in instance.adv_slide_name:
        name = instance.adv_slide_name.replace(' ','-')
        filename = 'h_' + uuid.uuid4().hex + instance.adv_slide_name + '.webp'
    if '_' in instance.adv_slide_name:
        name = instance.adv_slide_name.replace('_','-')
        filename = 'h_' + uuid.uuid4().hex + instance.adv_slide_name + '.webp'
    else:
        name = instance.adv_slide_name
        filename = 'h_' + uuid.uuid4().hex + instance.adv_slide_name + '.webp'
    filename = 'h_' + uuid.uuid4().hex + instance.adv_slide_name + '.webp'
    return 'landing/Images/advertising_slide/{0}'.format(filename)

class advertising_slide(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    admin_login = models.ForeignKey(admin_login, on_delete=models.CASCADE)
    adv_slide_name = models.CharField(_( 'eng slide name' ), max_length=100)
    adv_slide_url = models.CharField(_( 'url slide' ), max_length=100)
    adv_slide_slide = models.ImageField(upload_to=advertising_slide_image_path)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.adv_slide_name



def logo_image_path(instance, filename):
    return 'landing/Images/logo.png'
    
class logo(models.Model):
    logo = models.ImageField(upload_to=logo_image_path)
    active = models.BooleanField(default=False)

    
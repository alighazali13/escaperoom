from django.db import models
from brand.models import brand
from django.utils.translation import gettext as _
from datetime import datetime
import uuid, os, jdatetime
from django_jalali.db import models as jmodels

class gender_choices(models.IntegerChoices):
    null = 0 ,
    male = 1 ,
    female = 2 , 
    whatyouneed = 3 ,

class player_login(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    password = models.CharField(max_length=100)
    mail = models.EmailField()
    phonenumber = models.CharField(max_length=12, unique=True)
    joined_at = jmodels.jDateField(default=jdatetime.date.today)
    modified_at = jmodels.jDateField(default=jdatetime.date.today, null=True , blank=True)
    last_login = jmodels.jDateField(default=jdatetime.date.today)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.phonenumber


def player_avatar_path(instance, filename):
    
    # if ' ' in instance.url:
    #     name = instance.url.replace(' ','-')
    #     filename = 'big_' + uuid.uuid4().hex + '.webp'
    # if '_' in instance.url:
    #     name = instance.url.replace('_','-')
    #     filename = 'big_' + uuid.uuid4().hex + '.webp'
    # else:
    #     name = instance.url
    #     filename = 'big_' + uuid.uuid4().hex + '.webp'

    name = instance.first_name + '_' + instance.last_name
    filename = 'avatar_' + uuid.uuid4().hex + '.webp'
    return 'avatar/Images/{0}/{1}'.format(name,filename)


class player_info(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    player_login = models.ForeignKey(player_login, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=4, blank=True, null=True)
    gender = models.IntegerField(default=gender_choices.null, choices=gender_choices.choices, blank=True, null=True)
    birthday_date = jmodels.jDateField(default=jdatetime.date.today, blank=True, null=True)
    complited_at = jmodels.jDateField(default=jdatetime.date.today)
    avatar = models.ImageField(upload_to=player_avatar_path, null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + self.last_name

class player_codes(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    phonenumber = models.CharField(max_length=12, unique=True)
    code = models.CharField(max_length=5)
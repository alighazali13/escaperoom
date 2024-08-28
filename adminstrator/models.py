from django.db import models
from brand.models import brand
from django.utils.translation import gettext as _
from datetime import datetime
import uuid, os, jdatetime
from django_jalali.db import models as jmodels
from brand.models import brand

class gender_choices(models.IntegerChoices):
    null = 0 ,
    male = 1 ,
    female = 2 , 
    
class admin_type_choices(models.IntegerChoices):
    null = 0 ,
    core = 1 ,
    collector = 2 , 
    personel = 3 ,

class admin_login(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    collector_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=100)
    mail = models.EmailField(null=True, blank=True)
    phonenumber = models.CharField(max_length=12, unique=True)
    admin_type = models.IntegerField(default=admin_type_choices.null, choices=admin_type_choices.choices)
    brand = models.ForeignKey(brand, on_delete=models.SET_NULL, blank=True, null=True)
    joined_at = jmodels.jDateField(default=jdatetime.date.today)
    modified_at = jmodels.jDateField(default=jdatetime.date.today, null=True , blank=True)
    last_login = jmodels.jDateField(default=jdatetime.date.today)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.phonenumber)

class admin_info(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    admin_login = models.ForeignKey(admin_login, on_delete=models.CASCADE)
    collector_id = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=4, null=True , blank=True)
    gender = models.IntegerField(default=gender_choices.null, choices=gender_choices.choices)
    birthday_date = jmodels.jDateField(null=True , blank=True)
    complited_at = jmodels.jDateField(default=jdatetime.date.today)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.first_name + self.last_name)

class admin_codes(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    phonenumber = models.CharField(max_length=12, unique=True)
    code = models.CharField(max_length=5)

    
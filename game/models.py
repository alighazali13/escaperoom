from django.db import models
from brand.models import brand
from adminstrator.models import *
from player.models import *
from django.utils.translation import gettext as _
from datetime import datetime
import uuid, os, jdatetime
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



def game_poster_path(instance, filename):
    if ' ' in instance.brand.url:
        name = instance.brand.url.replace(' ','-')
        filename = uuid.uuid4().hex + uuid.uuid4().hex + '.webp'
    if '_' in instance.brand.url:
        name = instance.brand.url.replace('_','-')
        filename = uuid.uuid4().hex + uuid.uuid4().hex + '.webp'
    else:
        name = instance.brand.url
        filename = uuid.uuid4().hex + uuid.uuid4().hex + '.webp'
    filename = uuid.uuid4().hex + uuid.uuid4().hex + '.webp'
    return 'Games/Posters/{0}/{1}'.format(name,filename)

class game_type(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    fa_name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.fa_name

def game_teaser_path(instance, filename):
    if ' ' in instance.brand.url:
        name = instance.brand.url.replace(' ','-')
        filename = uuid.uuid4().hex + uuid.uuid4().hex + '.webp'
    if '_' in instance.brand.url:
        name = instance.brand.url.replace('_','-')
        filename = uuid.uuid4().hex + uuid.uuid4().hex + '.webp'
    else:
        name = instance.brand.url
        filename = uuid.uuid4().hex + uuid.uuid4().hex + '.webp'
    filename = uuid.uuid4().hex + uuid.uuid4().hex + '.webp'
    return 'Games/Teaser/{0}/{1}'.format(name,filename)

class game(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    gameID = models.IntegerField(unique=True, null=True, blank=True)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    admin = models.ForeignKey(admin_info, on_delete=models.CASCADE)
    game_type = models.ForeignKey(game_type, on_delete=models.CASCADE)
    fa_name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100)
    scenario = RichTextField(_('Game scenario'))
    roles = RichTextField(_('Game roles'))
    descriptions = RichTextField(_('Game descriptions'))
    unique_description = RichTextField(_('Game unique description'))
    teaser = models.FileField(upload_to=game_teaser_path, null=True, blank=True)
    poster = models.ImageField(upload_to=game_poster_path)
    price = models.IntegerField()
    url = models.CharField(max_length=150)
    today_game_times = models.IntegerField(default=4)
    today_close = models.BooleanField(_('today close ?'), default=False)
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.fa_name

class game_details(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    age = models.IntegerField()
    hardship = models.IntegerField()
    player_from = models.IntegerField()
    player_to = models.IntegerField()
    time = models.IntegerField()
    short_address = models.CharField(max_length=50)
    full_address = models.TextField()
    game_time_number = models.IntegerField(default=4)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.game.fa_name


class two_days_later(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    game_details = models.ForeignKey(game_details, on_delete=models.CASCADE)
    enable_date = jmodels.jDateField(default=jdatetime.date.today)
    active = models.BooleanField(default=True)
        
    def __str__(self):
        return self.game.en_name


class genre(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    fa_name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.fa_name

class game_genres(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    genre = models.ForeignKey(genre, on_delete=models.CASCADE)
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.game.fa_name

class game_time(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    time_from = models.CharField(max_length=4)
    time_to = models.CharField(max_length=4)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.game.fa_name

class closed_time(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    game_time = models.ForeignKey(game_time, on_delete=models.CASCADE)
    day = jmodels.jDateField(default=jdatetime.date.today)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.game.fa_name 

class closed_day(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    day = jmodels.jDateField(default=jdatetime.date.today)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.game.fa_name 

class sold_time(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    player = models.ForeignKey(player_info, on_delete=models.CASCADE, blank=True, null=True)
    game_time = models.ForeignKey(game_time, on_delete=models.CASCADE)
    day = jmodels.jDateField(default=jdatetime.date.today)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.game.fa_name 

class game_comment(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    player_info = models.ForeignKey(player_info, on_delete=models.CASCADE)
    created_at = jmodels.jDateField(default=jdatetime.date.today)
    comment = models.TextField()
    like = models.IntegerField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.comment

class game_reply(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    game_comment = models.ForeignKey(game_comment, on_delete=models.CASCADE)
    admin_info = models.ForeignKey(admin_info, on_delete=models.CASCADE)
    reply = models.TextField()
    active = models.BooleanField(default=True)

    
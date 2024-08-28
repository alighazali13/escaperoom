from django.db import models
from django.utils.translation import gettext as _
import uuid, os 
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



def big_logo_image_path(instance, filename):
    
    if ' ' in instance.url:
        name = instance.url.replace(' ','-')
        filename = 'big_' + uuid.uuid4().hex + name + '.webp'
    if '_' in instance.url:
        name = instance.url.replace('_','-')
        filename = 'big_' + uuid.uuid4().hex + name + '.webp'
    else:
        name = instance.url
        filename = 'big_' + uuid.uuid4().hex + name + '.webp'
    filename = 'big_' + uuid.uuid4().hex + name + '.webp'
    return 'Brands/Images/{0}/{1}'.format(name,filename)

def sm_logo_image_path(instance, filename):
    
    if ' ' in instance.url:
        name = instance.url.replace(' ','-')
        filename = 'sm_' + uuid.uuid4().hex + name + '.webp'
    if '_' in instance.url:
        name = instance.url.replace('_','-')
        filename = 'sm_' + uuid.uuid4().hex + name + '.webp'
    else:
        name = instance.url
        filename = 'sm_' + uuid.uuid4().hex + name + '.webp'
    filename = 'sm_' + uuid.uuid4().hex + name + '.webp'
    return 'Brands/Images/{0}/{1}'.format(name,filename)

class brand(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    fa_name = models.CharField(_( 'Persian Name' ), max_length=100)
    en_name = models.CharField(_( 'English Name' ), max_length=100)
    big_logo = models.ImageField(upload_to=big_logo_image_path)
    sm_logo = models.ImageField(upload_to=sm_logo_image_path)
    descriptions = RichTextField(_( 'Description About Brand' ))
    url = models.CharField(max_length=150)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.en_name


def brand_slide_image_path(instance, filename):
    
    if ' ' in instance.brand.url:
        name = instance.brand.url.replace(' ','-')
        filename = 'slide_' + uuid.uuid4().hex + '.webp'
    if '_' in instance.brand.url:
        name = instance.brand.url.replace('_','-')
        filename = 'slide_' + uuid.uuid4().hex + '.webp'
    else:
        name = instance.brand.url
        filename = 'slide_' + uuid.uuid4().hex + '.webp'
    filename = 'slide_' + uuid.uuid4().hex + '.webp'
    return 'Brands/Images/{0}/slides/{1}'.format(name,filename)


class brand_slide(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    slide = models.ImageField(upload_to=brand_slide_image_path)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.brand.en_name

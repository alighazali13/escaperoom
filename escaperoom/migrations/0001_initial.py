# Generated by Django 5.0.7 on 2024-08-11 12:56

import django.db.models.deletion
import escaperoom.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminstrator', '0008_alter_admin_login_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to=escaperoom.models.logo_image_path)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='advertising_banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4)),
                ('number', models.IntegerField(choices=[(0, 'Top'), (1, 'Bottom')], default=0)),
                ('adv_banner_name', models.CharField(max_length=100, verbose_name='eng slide name')),
                ('adv_banner_url', models.CharField(max_length=100, verbose_name='url slide')),
                ('adv_banner_slide', models.ImageField(upload_to=escaperoom.models.advertising_banner_image_path)),
                ('active', models.BooleanField(default=False)),
                ('admin_login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminstrator.admin_login')),
            ],
        ),
        migrations.CreateModel(
            name='advertising_slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4)),
                ('adv_slide_name', models.CharField(max_length=100, verbose_name='eng slide name')),
                ('adv_slide_url', models.CharField(max_length=100, verbose_name='url slide')),
                ('adv_slide_slide', models.ImageField(upload_to=escaperoom.models.advertising_slide_image_path)),
                ('active', models.BooleanField(default=False)),
                ('admin_login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminstrator.admin_login')),
            ],
        ),
        migrations.CreateModel(
            name='slides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4)),
                ('name', models.CharField(max_length=100, verbose_name='eng slide name')),
                ('url', models.CharField(max_length=100, verbose_name='url slide')),
                ('slide', models.ImageField(upload_to=escaperoom.models.home_slide_image_path)),
                ('active', models.BooleanField(default=False)),
                ('admin_login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminstrator.admin_login')),
            ],
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-04 18:17

import django.db.models.deletion
import django_jalali.db.models
import jdatetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=12, unique=True)),
                ('joined_at', django_jalali.db.models.jDateField(default=jdatetime.date.today)),
                ('modified_at', django_jalali.db.models.jDateField(blank=True, default=jdatetime.date.today, null=True)),
                ('last_login', django_jalali.db.models.jDateField(default=jdatetime.date.today)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='player_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=4)),
                ('gender', models.IntegerField(choices=[(0, 'Null'), (1, 'Male'), (2, 'Female'), (3, 'Whatyouneed')], default=0)),
                ('birthday_date', django_jalali.db.models.jDateField(default=jdatetime.date.today)),
                ('complited_at', django_jalali.db.models.jDateField(default=jdatetime.date.today)),
                ('active', models.BooleanField(default=False)),
                ('player_login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player_login')),
            ],
        ),
    ]

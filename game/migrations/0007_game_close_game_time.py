# Generated by Django 5.0.7 on 2024-08-28 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_closed_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='close',
            field=models.BooleanField(default=False, verbose_name='close ?'),
        ),
        migrations.AddField(
            model_name='game',
            name='time',
            field=models.IntegerField(default=4),
        ),
    ]
# Generated by Django 5.0.7 on 2024-08-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_details',
            name='time',
            field=models.IntegerField(),
        ),
    ]

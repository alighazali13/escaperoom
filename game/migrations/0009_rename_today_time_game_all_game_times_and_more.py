# Generated by Django 5.0.7 on 2024-08-28 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_rename_time_game_today_time_remove_game_close_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='today_time',
            new_name='all_game_times',
        ),
        migrations.AddField(
            model_name='game',
            name='today_game_times',
            field=models.IntegerField(default=4),
        ),
    ]

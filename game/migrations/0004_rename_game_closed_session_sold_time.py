# Generated by Django 5.0.7 on 2024-08-15 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0011_alter_admin_codes_code'),
        ('game', '0003_closed_time'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='game_closed_session',
            new_name='sold_time',
        ),
    ]
# Generated by Django 5.0.7 on 2024-08-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0009_admin_codes'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_codes',
            name='code',
            field=models.CharField(default=1, max_length=5, unique=True),
            preserve_default=False,
        ),
    ]
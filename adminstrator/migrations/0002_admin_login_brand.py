# Generated by Django 5.0.7 on 2024-08-05 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0001_initial'),
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_login',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='brand.brand'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0010_admin_codes_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_codes',
            name='code',
            field=models.CharField(max_length=5),
        ),
    ]

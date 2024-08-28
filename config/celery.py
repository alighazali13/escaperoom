from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# تنظیمات Django را برای Celery بارگذاری کنید
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# از تنظیمات Django برای پیکربندی Celery استفاده کنید
app.config_from_object('django.conf:settings', namespace='CELERY')

# بارگذاری تسک‌ها از تمام اپلیکیشن‌ها
app.autodiscover_tasks()
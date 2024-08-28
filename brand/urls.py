
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('<str:url>/', views.brand_details, name="brand_details"),
]

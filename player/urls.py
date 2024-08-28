from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('login/valvalidation/', views.account_validation, name="account_validation"),
    path('login/crtacc/', views.create_user_acc, name="create_user_acc"),

    path('', views.manage_comments, name="manage_comments"),
    path('logout', views.logout_player, name="logout_player"),
]

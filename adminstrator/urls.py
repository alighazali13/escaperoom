from django.urls import path, include, re_path
from . import views, functions

urlpatterns = [
    path('login/', views.login_admin, name="login_admin"),
    path('logout/', views.logout_admin, name="logout_admin"),
    path('login/valvalidation/', views.account_validation),

    path('', views.statistics, name="statistics_admin"),
    
    path('ur_brand/', views.ur_brand, name="ur_brand"),
    path('ur_games/', views.ur_games, name="ur_games"),
    path('ur_games/booking/<slug:slug>/', views.ur_booking, name="ur_booking"),
    path('ur_admins/', views.ur_admins, name="ur_admins"),
    path('ur_slides/', views.ur_slides, name="ur_slides"),



    path('genre_am/', views.genre_am, name="genre"),
    path('banners/', views.banners, name="banners"),
    path('twodayslater/', views.twodayslater, name="twodayslater"),
    
    path('brand/manage/', views.manage_brands, name="manage_brands"),
    path('brand/add/', views.add_brand, name="add_brand"),

    path('escaperoom/add/', views.add_escaperoom, name="add_escaperoom"),
    path('escaperoom/manage/', views.manage_scaperoom, name="manage_scaperoom"),
    
    path('comments/manage/', views.manage_comments, name="manage_comments"),
    
    path('admin/manage/', views.manage_admins, name="manage_admins"),
    path('admin/add/', views.add_admin, name="add_admin"),

    path('players/manage/', views.manage_players, name="manage_players"),



    path('ur_games/delete/<slug:slug>/', views.delete_game, name="delete_game"),
    path('brand/delete/<slug:slug>/', views.delete_brand, name="delete_brand"),
    path('comment/active/<slug:slug>/', views.active_comment, name="active_comment"),
    path('comment/deactive/<slug:slug>/', views.deactive_comment, name="deactive_comment"),
]

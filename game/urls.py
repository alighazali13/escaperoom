
from django.urls import path, include
from . import views, functions

urlpatterns = [
    path('', views.games, name='games'),
    path('<str:brand_url>/<str:game_url>/', views.game_detail, name="game_details"),
    
    path('geturhalidays/', functions.get_halidays, name="get_halidays"),
    path('getgametime/', functions.get_gametime, name="get_gametime"),
    path('closetime/', functions.close_time, name="close_time"),
    path('opentime/', functions.open_time, name="open_time"),
    path('sellingtime/', functions.selling_time, name="selling_time"),
    path('buytime/', functions.buy_time, name="buy_time"),
    path('closeday/', functions.close_day, name="close_day"),
    path('openday/', functions.open_day, name="open_day"),

]

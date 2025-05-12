from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new_game, name='new_game'),
    path('play/<int:game_id>/', views.play_game, name='play_game'),
    path('play/<int:game_id>/guess/', views.guess_letter, name='guess_letter'),
]

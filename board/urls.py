from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('game/<int:size>', views.game, name='game'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('all_games/', views.random_games, name='all_games'),
    path('coin/<int:n>', views.coin, name='coin'),
    path('coin/', views.coin, name='coin'),
    path('cube/', views.cube, name='cube'),
    path('number/', views.number, name='number'),
    path('statistic/<int:n>', views.statistic, name='statistic'),
]
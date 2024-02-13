from django.urls import path
from . import views

urlpatterns = [
    path('coin/', views.coin, name='coin'),
    path('cube/', views.cube, name='cube'),
    path('number/', views.number, name='number'),
    path('statistic/<int:n>', views.statistic, name='statistic'),
]
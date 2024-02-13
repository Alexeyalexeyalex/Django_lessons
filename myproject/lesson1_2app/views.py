from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from random import choice, randint
import logging
from .models import Coin



logger = logging.getLogger(__name__)

def my_logger(func):
    def wrapper(*args, **kwargs):
        coin = func(*args, **kwargs)
        logger.info(f"Была вызвана функция {func.__name__}")
        return coin
    return wrapper

@my_logger
def coin(request):
    result = choice(["Орел","Решка"])
    coin = Coin(side=result)
    coin.save()
    return HttpResponse(result)

@my_logger
def cube(request):
    return HttpResponse(randint(1,6))

@my_logger
def number(request):
    return HttpResponse(randint(1,100))

def statistic(request, n):
    return JsonResponse(Coin.get_last_n_flip(n), json_dumps_params={'ensure_ascii':False})
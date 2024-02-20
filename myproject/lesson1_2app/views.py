from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from random import choice, randint
import logging
from .models import Coin
from .form import RandomGames



logger = logging.getLogger(__name__)

def my_logger(func):
    def wrapper(*args, **kwargs):
        coin = func(*args, **kwargs)
        logger.info(f"Была вызвана функция {func.__name__}")
        return coin
    return wrapper

@my_logger
def coin(request, n=1):
    result_list = []
    for i in range(n):
        result = choice(["Орел","Решка"])
        coin = Coin(side=result)
        coin.save()
        result_list.append(result)
        
    return render(request, 'lesson1_2app/base.html', {'result_list':result_list})

@my_logger
def cube(request):
    return HttpResponse(randint(1,6))

@my_logger
def number(request):
    return HttpResponse(randint(1,100))

def statistic(request, n):
    return JsonResponse(Coin.get_last_n_flip(n), json_dumps_params={'ensure_ascii':False})


def random_games(request):
    if request.method == 'POST':
        form = RandomGames(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            if game == 'Coin':
                return coin(request, count)
            elif game == 'Cube':
                return cube(request)
            else:
                return number(request)


    else:
        form = RandomGames()
    return render(request, 'lesson1_2app/random_games.html', {'form': form})
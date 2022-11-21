import datetime
import time
import os
from django.http import HttpResponse
from django.core.paginator import Paginator

# Параметры запросов
from django.shortcuts import render


# def index(request):
#     return HttpResponse(f'<h1>Список доступных страниц</h1><br>'
#                         '<ul><li><h3>Главная страница</h3></li><li><h3>Текущее время</h3></li><li><h3>Рабочая директория: </h3></li></ul>')
#
# def current_time(request):
#     times = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
#     return HttpResponse(f'<h2>{times}</h2><br><h2>Time = {datetime.datetime.now().time()}</h2>')
#
# def workdir(request):
#     workdir = []
#     path = '/home/vitaly/Документы/Нетология/Django/Hi Django'
#     for filename in os.listdir(path):
#         workdir.append(filename)
#     return HttpResponse(f'<h2>Содержимое рабочей директории:<br>{workdir}</h2>')

# =================================  Параметры запросов  =====================================

def hello(request):
    # name = request.GET['name']
    # age = int(request.GET.get('age', 28)) # 28 дефолтное зн-е
    # country = request.GET.get('country') # При этом способе ошибки не будет если не введешь параметр будет - NONE
    # print(country)
    # print(age)
    # return HttpResponse(f'Hello! {name}, your age: {age}')

    # Вывод с помощью шаблона
    context = {
        'test': 5,
        'data': [1, 5, 8],
        'word_list': ['pen', 'name', 'home', 'cat', 'room'],
        'val': 'Hello',
    }

    return render(request, 'demo.html', context)


def sum(request, a, b):
    # result = int(a) + int(b) # Без конвертора
    result = a + b # С конвертором
    return HttpResponse(f'Sum = {result}')


# Обработчик пагинации

CONTENT = [str(i) for i in range(10000)]


def pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10) # 10 Это поскольку выдавать
    #page = paginator.get_page(5) # 5 Номер страницы
    page = paginator.get_page(page_number) # Запрашиваем страничку у пользователя какую он хочет
    context = {
        'page': page
    }
    return render(request, 'pagi.html', context)



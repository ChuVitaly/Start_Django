import datetime
import time
import os
from django.http import HttpResponse

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
    return HttpResponse('Hello from django')




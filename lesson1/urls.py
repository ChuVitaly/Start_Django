"""lesson1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import request
from django.urls import path
# from demo.views import index, current_time, workdir
from demo.views import hello, sum, pagi
from recipes.views import selection_recipes, omlet, pasta, buter, russian_salad

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='home'),
    # path('current_time/', current_time, name='time'),
    # path('workdir/', workdir, name='dir')
# Параметры запросов
    path('hello/', hello),
    # path('sum/<a>/<b>', sum),
    path('sum/<int:a>/<int:b>', sum), # Задаем маршрут с помощью конвектора
    path('pagi/', pagi),
    path('recipes/', selection_recipes),
    path('omlet/', omlet),
    path('pasta/', pasta),
    path('buter/', buter),
    path('russian_salad/', russian_salad)

]

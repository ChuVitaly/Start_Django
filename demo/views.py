import datetime

from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello from django</h1>')

def time (request):
    return HttpResponse(f'<h2>Time = {datetime.datetime.now().time()}</h2>')
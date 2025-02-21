from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, ToDoList
# Create your views here.
def home(response):
    ls = ToDoList.objects.get(id = 1)
    return render(response, 'main/base.html', {'ls': ls})

def index(response, id):
    ls = ToDoList.objects.get(id = id)
    return HttpResponse('<h1>%s</h1>' % ls)
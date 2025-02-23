from django.shortcuts import render
from .forms import CreateNewList

# Create your views here.
def home(response):
    return render(response, 'mysite/home.html', {})

def create(response):
    return render(response, 'mysite/list.html', {})
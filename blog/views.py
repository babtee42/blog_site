from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,"blog/index.html")

def hello(request):
    return HttpResponse("<h2>Hello, This is my first Django App!</h2> <h3>My name is BABATUNDE, what can i help you with?</h3>", )
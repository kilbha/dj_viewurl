from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def HomePage(request):
    return HttpResponse("<h1>Welcome to HomePage.</h1>")
def IndexPage(request):
    return HttpResponse("<h1>Welcome to Indexpage.</h1>")
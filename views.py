from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

# def data(request):
#     return HttpResponse("This is My app page")


def data(request):
    return render(request, "index.html")

def new(request):
    return HttpResponse("This is new page")
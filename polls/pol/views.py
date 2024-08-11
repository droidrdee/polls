from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello let's learn django from scratch in one day")
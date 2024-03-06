from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<a href='/rango/about/'> The about page is here! </a>")


def about(request):
    return HttpResponse("<a href='/rango/'> Back to the index </a>")

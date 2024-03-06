from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse('<a href="/rango/about/">About</a> Rango says hey there partner!')


def about(request):
    return HttpResponse('<a href="/rango/">Index</a> Rango says here is the about page.')

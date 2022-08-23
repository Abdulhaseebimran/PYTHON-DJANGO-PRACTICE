from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def myfirstfunc(request):
    return HttpResponse('ABDUL HASEEB IMRAN')

def mySecondfunc(request):
    return HttpResponse("HELLO PROGRAMMERS !")
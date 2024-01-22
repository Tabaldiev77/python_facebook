from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('<h1>Hello world<h1/>')


def my_url(request):
    return HttpResponse('my first page')











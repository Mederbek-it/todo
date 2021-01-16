from django.shortcuts import render, HttpResponse


def go(request):
    return HttpResponse("<h1>This is my first page</h1>")
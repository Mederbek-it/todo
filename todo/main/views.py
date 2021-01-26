from django.shortcuts import render, HttpResponse


def homepage(request):
    return HttpResponse("hello world!")


def test(request):
    return render(request, "test.html")

def second(request):
    return render(request, "index2.html")


def books_store(request):
    return render(request, "books.html")
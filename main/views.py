from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo


def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def books_store(request):
    form = request.POST
    text = form["books_store"]
    books_store = books_store(text=text)
    books_store.save()
    return redirect(books)

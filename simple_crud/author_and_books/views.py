from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    author = Author.objects.all()
    book = Book.objects.all()
    data = {"Author": author, "Book": book}
    return render(request, "author_and_books/home.html", data)

def create_author(request):
    form = AuthorForm()

    if(request.method == "POST"):
        form = AuthorForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    data = {"form": form}
    return render(request, "author_and_books/create_author.html", data)

def create_book(request):
    form = BookForm()

    if(request.method == "POST"):
        form = BookForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    data = {"form": form}
    return render(request, "author_and_books/create_book.html", data)

def update_author(request,pk):
    author = Author.objects.get(id=pk)
    form = AuthorForm(instance=author)

    if(request.method == 'POST'):
        form = AuthorForm(request.POST, instance=author)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    data ={"form": form}
    return render(request, "author_and_books/update_author.html", data)

def update_book(request,pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if(request.method == 'POST'):
        form = BookForm(request.POST, instance=book)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    data ={"form": form}
    return render(request, "author_and_books/update_book.html", data)

def delete_author(request,pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return redirect("/")

def delete_book(request,pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect("/")

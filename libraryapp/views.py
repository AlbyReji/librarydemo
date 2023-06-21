from django.shortcuts import render,redirect
import json
from django.http import HttpResponse
from django.urls import reverse
from .models import book,Author,Category,Genre
from .forms import Bookcreate,Authoradd
# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):

    return render(request,'libraryapp/home.html')

# def book_list(request):

#     with open('libraryapp/static/files/book.json') as book:

        
#         data = json.load(book)
#         book_list_data = data['books']
#         context = {'book_list': book_list_data}

#     return render(request,'libraryapp/list_of_books.html',context)



def book_list(request):

    books = book.objects.all()
    context = {
        "Books": books
    }

    return render(request,'libraryapp/list_of_books.html',context)

# def book_detial(request,id):

#     with open('libraryapp/static/files/book.json') as book:
#         data = json.load(book)
#         book_list_data = data['books']

#         for item in book_list_data:
#             if item.get ('id') == id:
#                 bk = item
#                 break
            
#     context = {'bk': bk}
#     return render(request,'libraryapp/book_details.html',context)


def book_detial(request,id):

    books = book.objects.all()

    for item in books:
        if item.id == id:
            return render(request,'libraryapp/book_details.html',{"Books":item})

    return HttpResponse("Book not found")
 
    


import requests
from django.views.generic import ListView ,CreateView ,UpdateView

# class author_list(ListView):
#     template_name = 'libraryapp/author_list.html'
#     context_object_name = 'authors'

#     def get_queryset(self):
#         response = requests.get('https://random-data-api.com/api/v2/users?size=10')

#         if response.status_code == 200:
#             authors = response.json()
#             print(authors)
#             return authors
#         else:
#             return []

class author_list(ListView):
    template_name = 'libraryapp/author_list.html'
    queryset = book.objects.all()
    context_object_name = 'books'


def book_create(request):
    form = Bookcreate()
    if request.method == 'POST':
        form = Bookcreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_create')
    
    context = {"form":form}
    return render(request ,'libraryapp/add_book.html',context)

class add_author(CreateView):
    template_name = 'libraryapp/add_author.html'
    form_class = Authoradd

    def get_success_url(self) -> str:
        return reverse('add_author')

class update_book(UpdateView):

    model = book
    form_class = Bookcreate
    template_name = 'libraryapp/update_book.html'

    def get_success_url(self) -> str:
        return reverse('')

        













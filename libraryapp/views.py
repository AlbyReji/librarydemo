from django.shortcuts import render
import json

# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):

    return render(request,'libraryapp/home.html')

def book_list(request):

    with open('libraryapp/static/files/book.json') as book:

        
        data = json.load(book)
        book_list_data = data['books']
        context = {'book_list': book_list_data}

    return render(request,'libraryapp/list_of_books.html',context)


def book_detial(request,id):

    with open('libraryapp/static/files/book.json') as book:
        data = json.load(book)
        book_list_data = data['books']

        for item in book_list_data:
            if item.get ('id') == id:
                bk = item
                break
            
    context = {'bk': bk}
    return render(request,'libraryapp/book_details.html',context)


import requests
from django.views.generic import ListView

class author_list(ListView):
    template_name = 'libraryapp/author_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        response = requests.get('https://random-data-api.com/api/v2/users?size=10')

        if response.status_code == 200:
            authors = response.json()
            print(authors)
            return authors
        else:
            return []






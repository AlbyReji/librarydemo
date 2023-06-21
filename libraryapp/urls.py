from django.urls import path 
from .import views 
from libraryapp.views import author_list,add_author,update_book


urlpatterns = [
    path('',views.home,name = 'home'),
    path('base/',views.base , name = 'base'),
    path('book_list/',views.book_list,name= 'book_list'),
    path('book_list/<int:id>',views.book_detial,name = 'book_detail'),
    path('author/', author_list.as_view(), name='author_list'),
    path('add_book/',views.book_create,name= 'book_create'),
    path('addauthor/',add_author.as_view(),name= 'add_author'),
    path('updatebook/<int:pk>/',update_book.as_view(),name= 'update_book'),

]
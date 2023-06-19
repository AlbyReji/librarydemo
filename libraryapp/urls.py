from django.urls import path 
from .import views ;
from libraryapp.views import author_list

urlpatterns = [
    path('',views.home,name = 'home'),
    path('base/',views.base , name = 'base'),
    path('book_list/',views.book_list,name= 'book_list'),
    path('book_list/<int:id>',views.book_detial,name = 'book_detail'),
    path('author/', author_list.as_view(), name='author_list'),

]
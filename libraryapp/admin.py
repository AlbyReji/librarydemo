from django.contrib import admin

from .models import  Author,Category,Genre,book

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(book)

from django.db import models

# from django.db.models import(
#     CharField,
#     DateField,
#     TextField,
#     ForeignKey,
#     BooleanField,
#     DecimalField,
#     ManyTOManyField,
#     EmailField,
#     CASECADE

# )

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length =255)
    birth_date = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =120)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length =120)

    def __str__(self):
        return self.name



class book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(Author ,on_delete = models.CASCADE)
    publication_date = models.DateField()
    created_date = models.DateField(auto_now_add = True)
    is_availble = models.BooleanField(default = True)
    price = models.DecimalField(max_digits = 8,decimal_places =2)
    description = models.TextField(max_length = 200)
    book_code = models.CharField(max_length = 20)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    genre = models.ManyToManyField(Genre)
    rating = models.DecimalField(max_digits = 5 ,decimal_places=2)

    def __str__(self):
        return self.title

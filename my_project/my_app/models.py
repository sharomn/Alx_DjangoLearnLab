from django.db import models
#from .models import Book
#
# from .serializers import BookSerializer

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

# Create your models here.


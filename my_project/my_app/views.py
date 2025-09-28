

#class MyModelListCreateAPIView(generics.ListCreateAPIView):
    #queryset = MyModel.objects.all()
    #serializer_class = MyModelSerializer

# Create your views here.


from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


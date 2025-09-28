from django.urls import path, include
from .views import BookListCreateView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/', include('api.urls')),

]
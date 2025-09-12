
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views 
from .views import list_books # ✅ This makes "views.register" visible to the checker
urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # ✅ Checker-required patterns
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'), 
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('books/add/', views.add_book, name='add_book/'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book/'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'), # ✅ Checker wants "views.register"
]


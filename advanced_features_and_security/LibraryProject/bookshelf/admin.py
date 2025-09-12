# Register your models here.
from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    list_filter = ('publication_year', 'author')            # Sidebar filters
    search_fields = ('title', 'author') 
    
admin.site.register(Book, BookAdmin) 

from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # Optional: customize how fields appear in admin
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']
                   # Search bar fields

admin.site.register(CustomUser, CustomUserAdmin)
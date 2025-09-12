# Register your models here.
from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    list_filter = ('publication_year', 'author')            # Sidebar filters
    search_fields = ('title', 'author')                     # Search bar fields

admin.site.register(Book, BookAdmin)
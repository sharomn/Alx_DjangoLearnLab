# CRUD Operations for Book Model

This document summarizes the Create, Retrieve, Update, and Delete operations performed on the `Book` model using Django's ORM via the shell.

---

## 📘 Create

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984 by George Orwell (1949)>
 Book instance successfully created.



📗 Retrieve
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# ('1984', 'George Orwell', 1949)


✅ Book instance retrieved with correct attributes.


📙 Update
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# 'Nineteen Eighty-Four'


✅ Book title successfully updated.

📕 Delete
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# <QuerySet []>


✅ Book instance deleted and confirmed by empty queryset.


 
# Advanced API Project

## Objective
Learn to construct custom views and utilize generic views in Django REST Framework.

## Features
- CRUD operations for Book model
- Generic views: List, Detail, Create, Update, Delete
- Permission-based access control
- Custom validation and filtering

## API Endpoints
- `GET /api/books/` — List all books
- `GET /api/books/<id>/` — Retrieve a book
- `POST /api/books/create/` — Create a book (auth required)
- `PUT /api/books/<id>/update/` — Update a book (auth required)
- `DELETE /api/books/<id>/delete/` — Delete a book (auth required)

## Setup
```bash
git clone <your-repo-url>
cd advanced_api_project
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py runserver



## Advanced Query Features

### Filtering
Use query parameters to filter books:
- `/api/books/?author=Chimamanda`
- `/api/books/?publication_year=2020`

### Searching
Search by title or author:
- `/api/books/?search=Purple Hibiscus`

### Ordering
Sort results:
- `/api/books/?ordering=title`
- `/api/books/?ordering=-publication_year`
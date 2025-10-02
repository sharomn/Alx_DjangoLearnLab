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

## Testing Strategy

Unit tests are located in `api/test_views.py`. They cover:
- CRUD operations for Book model
- Filtering, searching, and ordering
- Permission enforcement for authenticated vs unauthenticated users

### Running Tests
```bash
python manage.py test api

# 💬 Comment System Documentation

## Overview
Users can view comments on blog posts. Authenticated users can add, edit, and delete their own comments.

## Features
- Add comment on post detail page
- Edit/delete own comments
- View all comments under each post

## Permissions
- Only logged-in users can comment
- Only comment authors can edit/delete

## URLs
- `/posts/<post_id>/comments/new/` → Add comment
- `/comments/<pk>/edit/` → Edit comment
- `/comments/<pk>/delete/` → Delete comment

## Testing
- Log in and add a comment
- Edit/delete your comment
- Try unauthorized actions (should be blocked)
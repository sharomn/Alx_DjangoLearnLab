# 🛡️ Authentication System Documentation

## 📌 Overview
This authentication system enables users to:
- Register with a username, email, and password
- Log in and log out securely
- View and update their profile information

It uses Django’s built-in authentication views and forms, extended with custom registration and profile management.

---

## 🧩 Setup Instructions

### 1. Forms
- `CustomUserCreationForm` in `blog/forms.py` extends Django’s `UserCreationForm` to include an email field.

### 2. Views
- `register` view handles user registration.
- `profile` view allows authenticated users to view and update their email.
- Django’s built-in `LoginView` and `LogoutView` are used for login/logout.

### 3. URLs
Defined in `blog/urls.py`:
```python
path('login/', LoginView.as_view(template_name='blog/login.html'), name='login')
path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout')
path('register/', views.register, name='register')
path('profile/', views.profile, name='profile')
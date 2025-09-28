from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='sharon', password='pass123')
        self.client.login(username='sharon', password='pass123')
        self.book_data = {
            'title': 'Test Book',
            'author': 'Sharon Namatovu',
            'publication_year': 2025
        }

    def test_create_book(self):
        url = reverse('book-create')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Book')


    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        url = reverse('book-update', args=[book.id])
        updated_data = {**self.book_data, 'title': 'Updated Book'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book')


    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        url = reverse('book-delete', args=[book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



    def test_list_books_with_filters(self):
        Book.objects.create(title='Alpha', author='A', publication_year=2020)
        Book.objects.create(title='Beta', author='B', publication_year=2021)
        url = reverse('book-list') + '?search=Alpha'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Alpha')


    def test_unauthenticated_create_fails(self):
        self.client.logout()
        url = reverse('book-create')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)







    

    
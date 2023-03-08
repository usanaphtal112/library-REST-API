from django.test import TestCase

# Create your tests here.

from django.urls import reverse

from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="This is a good title",
            subtitle="here is best subtitle",
            author="naphtal",
            isbn="1234567890123",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "This is a good title")
        self.assertEqual(self.book.subtitle, "here is best subtitle")
        self.assertEqual(self.book.author, "naphtal")
        self.assertEqual(self.book.isbn, "1234567890123")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "here is best subtitle")
        self.assertTemplateUsed(response, "book_list.html")

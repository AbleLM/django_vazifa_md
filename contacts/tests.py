from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage


class ContactMessageViewsTests(TestCase):
    def setUp(self):
        self.home_url = reverse("contacts:contact_form")
        self.list_url = reverse("contacts:message_list")
        self.valid_data = {
            "first_name": "Furqat",
            "last_name": "Yo‘ldoshev",
            "phone": "+998993554555",
            "email": "abcd@gmail.com",
            "message": "Assalomu alaykum, darslar juda foydali.",
        }

    def test_home_page_displays_form(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ism")
        self.assertContains(response, "Familiya")
        self.assertContains(response, "Telefon raqam")
        self.assertContains(response, "Email manzil")
        self.assertContains(response, "Yuborilgan xabar")
        self.assertContains(response, "Jo‘natish")

    def test_valid_post_saves_message_and_redirects(self):
        response = self.client.post(self.home_url, self.valid_data)
        self.assertRedirects(response, self.list_url)
        self.assertEqual(ContactMessage.objects.count(), 1)
        saved = ContactMessage.objects.get()
        self.assertEqual(saved.first_name, "Furqat")
        self.assertEqual(saved.email, "abcd@gmail.com")

    def test_invalid_post_does_not_save(self):
        invalid_data = self.valid_data | {"email": "not-an-email"}
        response = self.client.post(self.home_url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)
        self.assertContains(response, "To‘g‘ri email manzil kiriting")

    def test_message_list_displays_saved_messages(self):
        ContactMessage.objects.create(**self.valid_data)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Furqat")
        self.assertContains(response, "+998993554555")
        self.assertContains(response, "abcd@gmail.com")

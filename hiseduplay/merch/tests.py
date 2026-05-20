from django.test import TestCase
from django.urls import reverse


class MerchViewTests(TestCase):
    def test_merch_page_renders(self):
        response = self.client.get(reverse("merch:merch"))

        self.assertEqual(response.status_code, 200)

    def test_quiz_page_renders(self):
        response = self.client.get(reverse("merch:quiz"))

        self.assertEqual(response.status_code, 200)

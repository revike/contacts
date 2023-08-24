from rest_framework import status
from django.urls import reverse
from base.tests import BaseTestCase
from contact.models import Contact


class TestContact(BaseTestCase):
    """Test Contact app"""

    def setUp(self) -> None:
        super().setUp()
        contact = {
            'author': self.user,
            'first_name': 'first',
            'last_name': 'last',
            'phone': '+72957288980'
        }
        self.count_numbers = 10
        for _ in range(self.count_numbers):
            self.contact = Contact.objects.create(**contact)
            self.contact.contact_data.email = 'email@example.com'
            self.contact.contact_data.save()

    def test_contact_list(self):
        """Test contacts list"""
        url = reverse('contact:list')
        response = self._make_get(url, self.user.email)
        self.assertEqual(response['count'], self.count_numbers)

    def test_contact_detail(self):
        """Test contact detail"""
        url = reverse('contact:detail', kwargs={'pk': self.contact.id})
        response = self._make_get(url, self.user.email)
        self.assertEqual(response['id'], self.contact.id)

        data = {
            'email': 'new_email@example.com',
            'first_name': 'new_name'
        }
        response = self._make_patch(url, self.user.email, data)
        self.assertEqual(response['email'], data['email'])
        self.assertNotEqual(self.contact.contact_data.email, data['email'])
        self.assertEqual(response['first_name'], data['first_name'])
        self.assertNotEqual(self.contact.first_name, data['first_name'])

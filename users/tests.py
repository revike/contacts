from rest_framework import status
from django.urls import reverse
from base.tests import BaseTestCase


class TestUser(BaseTestCase):
    """Test for Users app"""

    def test_login(self):
        """Test login"""
        url = reverse('user:login')
        data = {
            'email': self.user.email,
            'password': self.password
        }
        response = self._make_post(url, '', data=data, status_code=status.HTTP_200_OK)
        self.assertEqual(list(response.keys()), ['refresh', 'access'])

    def test_register(self):
        """Test register"""
        url = reverse('user:register')
        data = {
            'first_name': 'user',
            'last_name': 'user',
            'email': f'1_{self.user.email}',
            'password': self.password
        }
        response = self._make_post(url, '', data=data, status_code=status.HTTP_201_CREATED)
        self.assertEqual(response['email'], data['email'])

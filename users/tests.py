from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import register, profile


# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_register_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_profile_url(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

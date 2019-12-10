from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pulse_search.views import home, about, team, display_results


# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('pulse-home')
        self.assertEquals(resolve(url).func, home)

    def test_about_url(self):
        url = reverse('pulse-about')
        self.assertEquals(resolve(url).func, about)

    def test_team_url(self):
        url = reverse('pulse-team')
        self.assertEquals(resolve(url).func, team)

    def test_results_url(self):
        url = reverse('pulse-results')
        self.assertEquals(resolve(url).func, display_results)

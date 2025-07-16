from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
class HomepageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response =self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_based_on_name(self):
        response =self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def check_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'home.html')

    def test_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response,'<h1>Company Homepage</h1>')

class AboutpageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)

    def test_based_on_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code,200)

    def test_for_template_present(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response,'<h1>company About Website</h1>')
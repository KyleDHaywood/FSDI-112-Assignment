from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_returns_correct_templates(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "index.html")
        self.assertTemplateUsed(response, "base.html")
        
    def test_about_page_returns_correct_templates(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "about.html")
        self.assertTemplateUsed(response, "base.html")

    def test_home_page_returns_correct_content(self):
        response = self.client.get("/") 
        self.assertContains(response, "Hello, world!")

    def test_about_page_returns_correct_content(self):
        response = self.client.get("/about/") 
        self.assertContains(response, "About the author")

    def test_home_url_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_about_url_reverse_lookup(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
from .models import Content

User = get_user_model()


class ContentTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create_user(
            username='test',
            email='test@example.com',
            password='test_password',
        )
        cls.content = Content.objects.create(
            title="Harry Potter",
            creator=user,
            price=25,
        )

    def test_content_listing(self):
        self.assertEqual(f"{self.content.title}", "Harry Potter")
        self.assertEqual(f"{self.content.creator.username}", "test")
        self.assertEqual(self.content.price, 25)

    def test_content_list_view(self):
        response = self.client.get(reverse("content_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "contents/content_list.html")

    def test_content_detail_view(self):
        response = self.client.get(self.content.get_absolute_url())
        no_response = self.client.get("/contents/123/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "contents/content_detail.html")
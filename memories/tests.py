from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from memories.models import Memory


class TestCases(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

    def test_memory_create(self):
        memory = Memory.objects.create(
            title="Test Memory",
            comment="It's unreal",
            location="0101000020E610000000000000000000000000000000000000",
        )
        assert memory.title == "Test Memory"
        assert memory.comment == "It's unreal"
        assert memory.location == "0101000020E610000000000000000000000000000000000000"

    def test_published_memory(self):
        self.client.post(
            "/memory/add_memory/",
            {
                "author": get_user_model().objects.last().id,
                "title": "Test Memory2",
                "comment": "oops",
                "location": "0101000020E610000000000000000000000000000000000000",
            },
        )
        self.assertEqual(Memory.objects.last().title, "Test Memory2")

    def test_display_memory(self):
        memory = Memory.objects.create(
            title="Test Memory3",
            comment="It's unreal",
            location="0101000020E610000000000000000000000000000000000000",
        )
        response = self.client.get(reverse("memories:memory-detail", pk=memory.pk))
        self.assertContains(response, "Test Memory3")

    def test_memory_list(self):
        test_response = self.client.get("/")
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue("memories" in test_response.context)
        self.assertTemplateUsed(test_response, "memories_list.html")

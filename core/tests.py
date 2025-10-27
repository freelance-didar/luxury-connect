from django.test import TestCase
from django.urls import reverse


class CoreSmokeTests(TestCase):
    def test_index_renders(self) -> None:
        resp = self.client.get(reverse("core:index"))
        self.assertEqual(resp.status_code, 200)

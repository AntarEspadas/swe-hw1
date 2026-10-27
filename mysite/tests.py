from urllib.request import urlopen

from django.test import LiveServerTestCase


class SmokeTests(LiveServerTestCase):
    def test_app_is_reachable(self):
        with urlopen(f"{self.live_server_url}/", timeout=5) as response:
            self.assertEqual(response.status, 200)

from unittest.mock import MagicMock, patch

from django.test import RequestFactory, SimpleTestCase

from flapjack_api.health import healthz


class HealthzTests(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch("flapjack_api.health.redis.Redis")
    @patch("flapjack_api.health.connection")
    def test_healthz_success(self, mock_connection, mock_redis):
        mock_connection.cursor.return_value.__enter__.return_value = MagicMock()
        mock_redis.return_value = MagicMock()

        response = healthz(self.factory.get("/healthz/"))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"status": "ok"', response.content)

    @patch("flapjack_api.health.redis.Redis")
    @patch("flapjack_api.health.connection")
    def test_healthz_failure(self, mock_connection, mock_redis):
        mock_connection.cursor.side_effect = Exception("db down")
        mock_redis.side_effect = Exception("redis down")

        response = healthz(self.factory.get("/healthz/"))

        self.assertEqual(response.status_code, 503)
        self.assertIn(b'"status": "error"', response.content)

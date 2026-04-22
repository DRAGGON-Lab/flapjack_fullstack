from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckTests(TestCase):
    def test_health_endpoint_is_public_and_reports_ok(self):
        client = APIClient()
        response = client.get('/api/healthz/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('status'), 'ok')

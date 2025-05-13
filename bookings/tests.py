from django.test import TestCase
from rest_framework.test import APIClient
from .models import Room

class BookingTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.room = Room.objects.create(name="Test Room", capacity=5)

    def test_create_booking(self):
        response = self.client.post('/api/room_booking/', {
            "room": self.room.id,
            "booked_by": "Alice",
            "booking_start": "2025-05-12T10:00:00Z",
            "duration_minutes": 30
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("booking_end", response.data)


import uuid
from django.db import models
from django.utils import timezone
from datetime import timedelta

class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (Capacity: {self.capacity})"

class RoomBooking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    booked_by = models.CharField(max_length=100)
    booking_start = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()

    @property
    def booking_end(self):
        return self.booking_start + timedelta(minutes=self.duration_minutes)

    def __str__(self):
        return f"Booking by {self.booked_by} in {self.room.name}"


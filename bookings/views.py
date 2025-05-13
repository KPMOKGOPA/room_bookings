from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Room, RoomBooking
from .serializers import RoomSerializer, RoomBookingSerializer
from datetime import timedelta

class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomBookingViewSet(viewsets.ModelViewSet):
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        room = data.get("room")
        start = data.get("booking_start")
        duration = int(data.get("duration_minutes"))

        start_dt = self.serializer_class().fields['booking_start'].to_internal_value(start)
        end_dt = start_dt + timedelta(minutes=duration)

        overlapping = RoomBooking.objects.filter(
            room_id=room,
            booking_start__lt=end_dt,
            booking_start__gte=start_dt - timedelta(minutes=duration)
        )

        if overlapping.exists():
            return Response({"error": "Room is unavailable at the selected time."},
                            status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data

        room = data.get("room", instance.room.id)
        start = data.get("booking_start", instance.booking_start)
        duration = int(data.get("duration_minutes", instance.duration_minutes))

        start_dt = self.serializer_class().fields['booking_start'].to_internal_value(start)
        end_dt = start_dt + timedelta(minutes=duration)

        overlapping = RoomBooking.objects.filter(
            room_id=room,
            booking_start__lt=end_dt,
            booking_start__gte=start_dt - timedelta(minutes=duration)
        ).exclude(pk=instance.pk)

        if overlapping.exists():
            return Response({"error": "Room is unavailable at the selected time."},
                            status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, *args, partial=partial, **kwargs)

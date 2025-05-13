from rest_framework import serializers
from .models import Room, RoomBooking

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomBookingSerializer(serializers.HyperlinkedModelSerializer): 
    booking_end = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = RoomBooking
        fields = ['url', 'id', 'room', 'booking_id', 'booked_by', 'booking_start', 'duration_minutes', 'booking_end']


    def get_booking_end(self, obj):
        return obj.booking_end

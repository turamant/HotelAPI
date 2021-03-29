from rest_framework import serializers

from hotel.models import Hotel, Room, RoomCategory, Reservation, Payment, Sale


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id','name','address','zip_code',
                  'description')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','number','room_category','hotel','is_free')

class RoomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = ('id','name','max_guest','description')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('guid','start_date','end_date','period',
                  'guests_number','customer')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('guid','reservation','customer','datetime',
                  'is_paid','amount')

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('charge_id','payment')
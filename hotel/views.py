from rest_framework.viewsets import ModelViewSet

from hotel.models import Hotel, Room, RoomCategory, Reservation, Payment
from hotel.serializers import HotelSerializer, RoomSerializer, RoomCategorySerializer, ReservationSerializer, \
    PaymentSerializer


class HotelList(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    #permission_classes = (permissions.IsAuthenticated,)

class RoomList(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomCategoryList(ModelViewSet):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer


class ReservationList(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class PaymentList(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


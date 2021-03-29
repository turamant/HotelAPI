from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet

from hotel.models import Hotel, Room, RoomCategory, Reservation, Payment, Sale
from hotel.serializers import HotelSerializer, RoomSerializer, RoomCategorySerializer, ReservationSerializer, \
    PaymentSerializer, SaleSerializer


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

class SaleList(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


# rendering views
class ListHotelView(ListView):
    model = Hotel
    template_name = 'list_hotel.html'

class DetailRoomView(DetailView):
    model = Room
    template_name = 'detail_room.html'

class DetailHotelView(DetailView):
    model = Hotel
    template_name = 'detail_hotel.html'
    slug_field = 'slug'

class ListRoomView(ListView):
    model = Room
    template_name = 'list_room.html'

class ListReservationView(ListView):
    model = Reservation
    template_name = 'list_reservation.html'


class DetailReservationView(DetailView):
    model = Reservation
    template_name = 'detail_reservation.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(DetailReservationView, self).get_context_data(**kwargs)
        context['hotel_all'] = Hotel.objects.all()
        context['room_all'] = Room.objects.all()
        return context


class CreateReservation(CreateView):
    model = Reservation
    template_name = 'create_reservation.html'
    fields = '__all__'




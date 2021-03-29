from django.urls import path
from django.views.generic import TemplateView

from hotel.views import ListHotelView, DetailHotelView, ListRoomView, DetailRoomView, ListReservationView, \
    DetailReservationView, CreateReservation

urlpatterns = [
    path('reservation/create/',CreateReservation.as_view(), name='create_reservation'),

    path('reservation/<slug:slug>/',DetailReservationView.as_view(), name='detail_reserv'),
    path('reservation/',ListReservationView.as_view(), name='list_reservation'),

    path('room/<int:pk>/',DetailRoomView.as_view(), name='detail_room'),
    path('<int:pk>/room/',ListRoomView.as_view(), name='list_room'),

    path('<slug:slug>/',DetailHotelView.as_view(), name='detail_hotel'),
    path('',ListHotelView.as_view(), name='list_hotel'),

]
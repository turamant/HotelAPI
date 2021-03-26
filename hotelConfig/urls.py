from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from rest_auth.registration.views import RegisterView,LoginView
from rest_framework.routers import SimpleRouter

from hotel.views import HotelList, RoomList, RoomCategoryList, ReservationList, PaymentList

router = SimpleRouter()

#API endpoints
router.register('api/hotel',HotelList)
router.register('api/room',RoomList)
router.register('api/rcat',RoomCategoryList)
router.register('api/reserv',ReservationList)
router.register('api/payment',PaymentList)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'), name='index'),

    #API endpoints
    path('api/auth/register/',RegisterView.as_view()),
    path('api/auth/login/',LoginView.as_view()),
    path('api/auth/logout/',LoginView.as_view()),
]
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



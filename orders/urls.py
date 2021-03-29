from django.urls import path

from orders.views import OrdersPageView, charge

urlpatterns = [
    path('charge/',charge, name='charge'),
    path('',OrdersPageView.as_view(), name='orders')
]
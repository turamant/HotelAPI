# Create your models here.
import uuid

import stripe
from django.conf import settings
from django.db import models
#from django.contrib.gis.db import models as gis_models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Hotel(models.Model):
    """ Model of Hotel """
    name = models.CharField(
        max_length=255,
        verbose_name= _('Name of Hotel'),
    )
    slug = models.SlugField(max_length=255,null=True)
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Location of Hotel'),
    )
    '''
    location = gis_models.PointField(
        verbose_name=_('Location'),
        null=True,
        blank=True,
        geography=True,
        help_text=_('Location of Hotel'),
    )
    '''
    zip_code = models.IntegerField(
        verbose_name=_('ZIP Code'),
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name=_('Description'),
        blank='',
        default=True,
    )
    class Meta:
        verbose_name = _('Hotel')
        verbose_name_plural = _('Hotels')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('detail_hotel', kwargs={"slug": self.slug})

class RoomCategory(models.Model):
    """ Category of room """
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name of category'),
    )
    max_guest = models.IntegerField(
        verbose_name=_('Max number of guests'),
        default=2
    )
    description = models.TextField(
        verbose_name=_('Description of Category'),
        max_length=255,
        blank=True,
        null=True,
    )
    price_for_night = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text='Цена за одну ночь',
        null=True,
    )
    class Meta:
        verbose_name = _('RoomCategory')
        verbose_name_plural = _('RoomCategories')

    def __str__(self):
        return f'{self.name}'


class Room(models.Model):
    """ Model of Room"""
    number = models.IntegerField(
        verbose_name=_('Number of room'),
        default=0,
    )
    room_category = models.ForeignKey(
        to=RoomCategory,
        on_delete=models.CASCADE,
        related_name='rooms',
    )
    hotel = models.ForeignKey(
        to=Hotel,
        on_delete=models.CASCADE,
        related_name='rooms',
    )
    is_free = models.BooleanField(
        verbose_name=_('Check that room is free'),
        default=True
    )
    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')

    def __str__(self):
        return f'{self.hotel}: {self.number}'


class Reservation(models.Model):
    """ Reservation Model """
    guid = models.UUIDField(
        verbose_name=_('GUID of Reservation'),
        default=uuid.uuid4,
        primary_key=True,
    )
    slug = models.SlugField(max_length=255,null=True)
    hotel = models.ForeignKey(to=Hotel,on_delete=models.CASCADE,null=True)
    room = models.ForeignKey(to=Room,on_delete=models.CASCADE,null=True)

    start_date = models.DateField(
        verbose_name=_('Start date of reservation'),
        blank=True,
    )
    end_date = models.DateField(
        verbose_name=_('End date of reservation'),
        blank=True
    )
    period = models.IntegerField(
        verbose_name=_('Period of reservation')
    )
    guests_number = models.IntegerField(
        verbose_name=_('Number of guests')
    )
    # add status , payment with stripe
    customer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('customer'),
        related_name='reservations',
        help_text=_('')
    )
    class Meta:
        verbose_name = _('Reservation')
        verbose_name_plural = _('Reservations')

    def __str__(self):
        return f'{self.period}: {self.customer}'

    def get_absolute_url(self):
        return reverse('detail_reserv', kwargs={"slug": self.slug})

    @property
    def period(self):
        delta = self.end_date - self.start_date
        return delta.days

class Payment(models.Model):
    """ Model for payment """

    guid = models.UUIDField(
        verbose_name=_('GUID of Payment'),
        default=uuid.uuid4,
        primary_key=True,
    )
    reservation = models.OneToOneField(
        to=Reservation,
        on_delete=models.CASCADE,
        verbose_name=_('reservation_id'),
        related_name='payment',
        help_text=_('Id of reservation for payment'),
    )
    customer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('customer'),
        related_name=_('payments'),
        help_text=_('')
    )
    datetime = models.DateTimeField(
        verbose_name=_('Date of payment'),
        null=True,
        blank=True,
    )
    is_paid = models.BooleanField(
        verbose_name=_('Status of payment'),
        default=False,
    )
    amount = models.FloatField(
        verbose_name=_('Amount of reservation'),
        null=True,
        blank=True,
    )
    def __str__(self):
        return f'{self.reservation}: {self.customer}'

class Sale(models.Model):
    def __init__(self, *args, **kwargs):
        super(Sale,self).__init__(*args, **kwargs)

        #bring in stripe, and get the api key from settings.py
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        self.stripe = stripe
    charge_id = models.CharField(
        max_length=32,
    )
    payment = models.OneToOneField(
        to=Payment,
        on_delete=models.CASCADE,
        verbose_name=_('payment'),
        related_name=_('sale'),
        help_text=_(''),
        blank=True,
        null=True,
    )
    def charge(self, price_in_cents, number, exp_month, exp_year, cvc ):
        if self.charge_id:
            return False
        try:
            responce = self.stripe.Charge.create(
                amount=price_in_cents,
                currency="usd",
                card={
                    "number":number,
                    "exp_month":exp_month,
                    "exp_year":exp_year,
                    "cvc":cvc,
                },
                description='Thank you for your purchase!')
            self.charge_id = responce.id
        except self.stripe.CardError:
            return False, False
        return True, responce


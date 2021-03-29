from django.contrib import admin

# Register your models here.
from hotel.models import Hotel, Room, RoomCategory, Reservation, Payment, Sale


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name','slug','address','zip_code',
                    'description',]
    prepopulated_fields = {'slug':('name',),}


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number','room_category','hotel',
                    'is_free',]

@admin.register(RoomCategory)
class RoomCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','max_guest',
                    'price_for_night']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['guid', 'slug','hotel','room','start_date',
                    'end_date','period',
                    'guests_number','customer']
    prepopulated_fields = {'slug':('guid',),}


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['guid', 'reservation',
                    'customer','datetime','is_paid',
                    'amount']

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['charge_id','payment']

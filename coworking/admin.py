from django.contrib import admin

from coworking.models import Rooms, RoomReservation


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(RoomReservation)
class RoomsAdmin(admin.ModelAdmin):
    exclude = ()


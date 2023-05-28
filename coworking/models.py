from django.db import models
from django.contrib.auth.models import User

class Rooms(models.Model):    
    name = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Rooms"

class RoomReservation(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):
        return f"{self.user.username} / {self.room.name}"

    class Meta:
        verbose_name_plural = "Room Reservation"



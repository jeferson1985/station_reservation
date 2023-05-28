from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from coworking.models import Rooms, RoomReservation
from coworking.serializers import RoomsSerializer, RoomReservationSerializer


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class RoomResevationViewSet(viewsets.ModelViewSet):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer


from django.urls import include, path
from rest_framework import routers

from coworking.views import RoomsViewSet, RoomResevationViewSet

router = routers.DefaultRouter()

router.register(r'rooms', RoomsViewSet)
router.register(r'roomreservation', RoomResevationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
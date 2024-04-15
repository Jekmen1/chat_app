from django.urls import path
from .views import UserViewSet, rooms, room

urlpatterns = [
    path("", rooms, name="rooms"),
    path("<str:slug>/", room, name="room"),
]

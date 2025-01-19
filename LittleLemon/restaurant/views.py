from django.shortcuts import render
from rest_framework import generics
from .models import Menu, Booking  # Import the MenuItem model
from .serializers import (
    MenuItemSerializer,
    BookingSerializer,
)  # Import the MenuItemSerializer
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, "index.html", {})


# MenuItemView for handling GET and POST for Menu items
class MenuItemsView(generics.ListCreateAPIView):
    serializer_class = MenuItemSerializer
    queryset = Menu.objects.all()  # Ensure 'Menu' is beinxg queried properly


# SingleMenuItemView for handling GET, PUT, and DELETE for a single Menu item
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    serializer_class = MenuItemSerializer
    queryset = Menu.objects.all()  # Ensure 'Menu' is being queried properly


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()  # Fetch all objects from the Booking model
    serializer_class = BookingSerializer

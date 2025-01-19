from rest_framework import serializers
from .models import Menu, Booking  # Make sure the MenuItem model is correctly imported


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "name",
            "menu_item_description",
            "price",
        ]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Set the model to the Booking model
        fields = "__all__"

# test-models.py
from django.test import TestCase
from restaurant.models import Menu  # Import the Menu model


# TestCase class
class MenuTest(TestCase):
    def test_get_item(self):
        # Create a new Menu instance
        item = Menu.objects.create(
            name="IceCream", price=80, menu_item_description="Delicious ice cream"
        )

        # Test string representation of the Menu instance
        self.assertEqual(str(item), "IceCream")

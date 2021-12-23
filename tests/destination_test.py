import unittest
from models.city import City
from models.country import Country
from models.destination import Destination

class TestDestination(unittest.TestCase):
    def setUp(self):
        self.country= Country("United Kingdom", True)
        self.country2= Country("United States", False)
        self.city= City("Edinburgh", True, self.country)
        self.city2 = City("New York", False, self.country2)
        self.destination= Destination("Princess Street", self.city, True)

    def test_destination_has_name(self):
        self.assertEqual("Princess Street", self.destination.name)

    def test_destination_has_true_value(self):
        self.assertEqual(True, self.destination.visited)

    def test_destination_has_False_value(self):
        self.destination= Destination("River Place", self.city2, False)
        self.assertEqual(False, self.destination.visited)

    def test_destination_has_city_id(self):
        self.assertEqual(self.city, self.destination.city)
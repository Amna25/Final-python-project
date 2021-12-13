import unittest
from models.destination import Destination
from models.city import City
class TestDestination(unittest.TestCase):
    def setUp(self):
        self.destination=Destination('street',city, True)

    def test_destination_has_a_name(self):
        self.assertEqual('street', self.destination.name)

    def destination_has_places_to_visit(self):
        self.assertEqual('true',self.destination.visited)

    def destination_has_places_still_to_visit(self):
        self.assertEqual('False', self.destination.visited)

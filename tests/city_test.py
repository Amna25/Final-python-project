import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):
    def setUp(self):
        self.country= Country("United Kingdom", True)
        self.country2= Country("United States", False)

        self.city= City("Edinburgh", True, self.country)
    
    def test_city_has_name(self):
        self.assertEqual("Edinburgh", self.city.name)

    def test_city_has_true_value(self):
        self.assertEqual(True, self.city.visited)

    def test_city_has_False_value(self):
        self.city= City("New York", False, self.country2)
        self.assertEqual(False, self.city.visited)

    def test_city_has_country_id(self):
        self.assertEqual(self.country, self.city.country)

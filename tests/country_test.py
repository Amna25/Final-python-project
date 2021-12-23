import unittest 
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country("United Kingdom", True)

    def test_country_has_a_name(self):
        self.assertEqual("United Kingdom", self.country.name)

    def test_country_has_true_value(self):
        self.assertEqual(True, self.country.visited)

    def test_country_can_have_False_value(self):
        self.country = Country("United States", False)
        self.assertEqual(False, self.country.visited)

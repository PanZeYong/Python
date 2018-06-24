import unittest
from city_country import get_city_country

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')
        
    def test_city_country_population(self):
        city_country = get_city_country('santiago', 'chile', 5000)
        self.assertEqual(city_country, 'Santiago, Chile - Population=5000')

unittest.main()

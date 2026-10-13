
from unittest import TestCase
from temparute_converter import *

class TestTemperatureConverter(TestCase):
    def test_freezing_point(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)

    def test_boiling_point(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)

    def test_minus_forty(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40)

    def test_convert_back(self):
        fahrenheit = celsius_to_fahrenheit(25)
        celsius = fahrenheit_to_celsius(fahrenheit)

        self.assertAlmostEqual(celsius, 25)

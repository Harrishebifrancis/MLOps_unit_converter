import unittest
from src.unit_converter import (
    km_to_miles, miles_to_km, celsius_to_fahrenheit, fahrenheit_to_celsius,
    kg_to_pounds, pounds_to_kg, convert_units
)

class TestUnitConverter(unittest.TestCase):
    def test_km_to_miles(self): self.assertAlmostEqual(km_to_miles(1), 0.6213711922373339, places=12)
    def test_miles_to_km(self): self.assertAlmostEqual(miles_to_km(1), 1.609344, places=12)
    def test_celsius_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0, places=12)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0, places=12)
    def test_kg_pounds(self):
        self.assertAlmostEqual(kg_to_pounds(1), 2.2046226218487757, places=12)
        self.assertAlmostEqual(pounds_to_kg(2.2046226218487757), 1.0, places=12)
    def test_convert_units_router(self):
        self.assertAlmostEqual(convert_units(1, "km", "miles"), 0.6213711922373339, places=12)
        self.assertAlmostEqual(convert_units(1, "miles", "km"), 1.609344, places=12)
        self.assertAlmostEqual(convert_units(100, "celsius", "fahrenheit"), 212.0, places=12)
        self.assertAlmostEqual(convert_units(32, "fahrenheit", "celsius"), 0.0, places=12)
        self.assertAlmostEqual(convert_units(1, "kg", "pounds"), 2.2046226218487757, places=12)
        self.assertAlmostEqual(convert_units(2.2046226218487757, "pounds", "kg"), 1.0, places=12)

if __name__ == "__main__":
    unittest.main()

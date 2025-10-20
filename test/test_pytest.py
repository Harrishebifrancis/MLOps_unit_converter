import pytest
from src.unit_converter import (
    km_to_miles, miles_to_km, celsius_to_fahrenheit, fahrenheit_to_celsius,
    kg_to_pounds, pounds_to_kg, convert_units
)

def test_km_to_miles():
    assert km_to_miles(1) == pytest.approx(0.6213711922373339, abs=1e-9)

def test_miles_to_km():
    assert miles_to_km(1) == pytest.approx(1.609344, abs=1e-9)

def test_celsius_fahrenheit():
    assert celsius_to_fahrenheit(0) == pytest.approx(32.0, abs=1e-12)
    assert fahrenheit_to_celsius(212) == pytest.approx(100.0, abs=1e-12)

def test_kg_pounds():
    assert kg_to_pounds(1) == pytest.approx(2.2046226218487757, abs=1e-12)
    assert pounds_to_kg(2.2046226218487757) == pytest.approx(1.0, abs=1e-12)

def test_convert_units_router():
    assert convert_units(1, "km", "miles") == pytest.approx(0.6213711922373339, abs=1e-9)
    assert convert_units(1, "miles", "km") == pytest.approx(1.609344, abs=1e-9)
    assert convert_units(100, "celsius", "fahrenheit") == pytest.approx(212.0, abs=1e-12)
    assert convert_units(32, "fahrenheit", "celsius") == pytest.approx(0.0, abs=1e-12)
    assert convert_units(1, "kg", "pounds") == pytest.approx(2.2046226218487757, abs=1e-12)
    assert convert_units(2.2046226218487757, "pounds", "kg") == pytest.approx(1.0, abs=1e-12)

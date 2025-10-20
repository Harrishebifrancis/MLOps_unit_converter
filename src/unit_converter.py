MILES_PER_KM = 0.6213711922373339
KM_PER_MILE = 1.609344
LB_PER_KG   = 2.2046226218487757

def km_to_miles(km: float) -> float:
    return km * MILES_PER_KM

def miles_to_km(miles: float) -> float:
    return miles * KM_PER_MILE

def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9.0/5.0) + 32.0

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32.0) * 5.0/9.0

def kg_to_pounds(kg: float) -> float:
    return kg * LB_PER_KG

def pounds_to_kg(lb: float) -> float:
    return lb / LB_PER_KG

def convert_units(value: float, from_unit: str, to_unit: str) -> float:
    f, t = from_unit.strip().lower(), to_unit.strip().lower()
    table = {
        ("km", "miles"): km_to_miles,
        ("miles", "km"): miles_to_km,
        ("celsius", "fahrenheit"): celsius_to_fahrenheit,
        ("fahrenheit", "celsius"): fahrenheit_to_celsius,
        ("kg", "pounds"): kg_to_pounds,
        ("pounds", "kg"): pounds_to_kg,
    }
    if (f, t) not in table:
        raise ValueError(f"Conversion from '{from_unit}' to '{to_unit}' is not supported.")
    return table[(f, t)](value)

# unit.py

def length_converter(value, from_unit, to_unit):
    length_to_meter = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "mile": 1609.34,
        "foot": 0.3048
    }

    if from_unit not in length_to_meter or to_unit not in length_to_meter:
        return "Invalid unit"
    
    value_in_meter = value * length_to_meter[from_unit]
    result = value_in_meter / length_to_meter[to_unit]

    return result


def weight_converter(value, from_unit, to_unit):
    weight_to_kg = {
        "kilogram": 1,
        "gram": 0.001,
        "pound": 0.453592,
        "ounce": 0.0283495
    }

    if from_unit not in weight_to_kg or to_unit not in weight_to_kg:
        return "Invalid unit"
    value_in_kg = value * weight_to_kg[from_unit]
    result = value_in_kg / weight_to_kg[to_unit]

    return result


def temperature_converter(value, from_unit, to_unit):

    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9 / 5) + 32

    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5 / 9

    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15

    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15

    elif from_unit == to_unit:
        return value

    else:
        return "Invalid temperature unit"
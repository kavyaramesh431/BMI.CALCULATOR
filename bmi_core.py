# bmi_core.py - calculation and categorization logic

def convert_height_to_meters(height, unit):
    """Convert height to meters from meters or feet."""
    if unit.lower() == "meters":
        return height
    elif unit.lower() == "feet":
        return height * 0.3048
    else:
        raise ValueError("Unsupported height unit: " + unit)

def convert_weight_to_kg(weight, unit):
    """Convert weight to kilograms from kg or pounds."""
    if unit.lower() == "kg":
        return weight
    elif unit.lower() == "pounds":
        return weight * 0.453592
    else:
        raise ValueError("Unsupported weight unit: " + unit)

def calculate_bmi(weight_kg, height_m):
    """Calculate BMI. weight in kg, height in meters."""
    if height_m <= 0:
        raise ValueError('Height must be greater than 0')
    if weight_kg <= 0:
        raise ValueError('Weight must be greater than 0')
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def categorize_bmi(bmi):
    """Return WHO-like category for a BMI value."""
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal weight'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obesity'
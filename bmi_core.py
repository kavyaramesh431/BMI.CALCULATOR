# bmi_core.py - calculation and categorization logic

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

from bmi_core import convert_height_to_meters, convert_weight_to_kg, calculate_bmi, categorize_bmi

def main():
    print("BMI Calculator")
    height = float(input("Enter your height: "))
    height_unit = input("Enter height unit (Meters/Feet): ")
    weight = float(input("Enter your weight: "))
    weight_unit = input("Enter weight unit (Kg/Pounds): ")

    try:
        height_m = convert_height_to_meters(height, height_unit)
        weight_kg = convert_weight_to_kg(weight, weight_unit)
        bmi = calculate_bmi(weight_kg, height_m)
        category = categorize_bmi(bmi)
        print(f"Your BMI is: {bmi}")
        print(f"Category: {category}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
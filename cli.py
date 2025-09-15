# cli.py - simple command-line BMI calculator with option to save
from bmi_core import calculate_bmi, categorize_bmi
import db

def get_float(prompt):
    while True:
        try:
            v = input(prompt).strip()
            if v.endswith('cm'):
                # convert cm to meters
                num = float(v[:-2].strip())
                return num / 100.0
            if v.endswith('m'):
                num = float(v[:-1].strip())
                return num
            val = float(v)
            # assume meters if value < 3, else assume cm
            if val > 3:
                return val / 100.0
            return val
        except Exception as e:
            print('Invalid input, try again. Example inputs: 70, 70kg, 170cm, 1.7m')


def main():
    db.init_db()
    print('BMI Calculator (CLI)')
    weight = float(input('Enter weight in kg (e.g. 70): ').strip())
    height = get_float('Enter height (meters like 1.75 or cm like 175): ')
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    print(f'BMI = {bmi} -> {category}')
    save = input('Save this record to history? (y/n): ').strip().lower()
    if save == 'y':
        db.add_record(weight, height, bmi, category)
        print('Saved.')

if __name__ == '__main__':
    main()

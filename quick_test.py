# quick_test.py - demonstrate bmi_core usage
from bmi_core import calculate_bmi, categorize_bmi

def test():
    w = 70
    h = 1.75
    bmi = calculate_bmi(w, h)
    cat = categorize_bmi(bmi)
    print(f'Weight={w}kg Height={h}m -> BMI={bmi} Category={cat}')

if __name__ == '__main__':
    test()

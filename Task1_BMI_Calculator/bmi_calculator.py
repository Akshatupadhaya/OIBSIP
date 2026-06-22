"""
BMI Calculator
A command-line tool that calculates Body Mass Index (BMI) from user-provided
weight (kg) and height (m), then classifies the result into a health category.
"""


def get_positive_float(prompt, min_value, max_value, unit):
    """Repeatedly ask the user for a number until a valid value is given."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = float(raw_value)
        except ValueError:
            print(f"  Please enter a numeric value (e.g. 65.5). You entered: '{raw_value}'")
            continue

        if value <= 0:
            print(f"  {unit.capitalize()} must be greater than 0. Please try again.")
            continue

        if not (min_value <= value <= max_value):
            print(f"  That {unit} seems out of a realistic range "
                  f"({min_value}-{max_value}). Please try again.")
            continue

        return value


def calculate_bmi(weight_kg, height_m):
    """Return the BMI value rounded to 2 decimal places."""
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def classify_bmi(bmi):
    """Map a BMI value to a standard WHO health category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 45)
    print("           BMI CALCULATOR")
    print("=" * 45)

    weight = get_positive_float(
        "Enter your weight in kilograms (e.g. 65.5): ",
        min_value=2, max_value=400, unit="weight"
    )
    height = get_positive_float(
        "Enter your height in meters (e.g. 1.75): ",
        min_value=0.5, max_value=2.5, unit="height"
    )

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print("\n" + "-" * 45)
    print(f"Weight     : {weight} kg")
    print(f"Height     : {height} m")
    print(f"Your BMI   : {bmi}")
    print(f"Category   : {category}")
    print("-" * 45)

    print("\nReference ranges:")
    print("  Underweight    : BMI < 18.5")
    print("  Normal weight  : 18.5 <= BMI < 25")
    print("  Overweight     : 25 <= BMI < 30")
    print("  Obese          : BMI >= 30")


if __name__ == "__main__":
    while True:
        main()
        again = input("\nCalculate another BMI? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for using the BMI Calculator. Stay healthy!")
            break
        print()

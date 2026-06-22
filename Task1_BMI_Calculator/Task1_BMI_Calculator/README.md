# BMI Calculator (Python Programming Internship – Task 1)

## Objective
Build a command-line application that calculates a user's Body Mass Index
(BMI) from their weight and height, then classifies the result into a
standard health category (Underweight, Normal weight, Overweight, Obese).

## Tools Used
- Python 3
- Standard library only (no external packages required)

## Steps Performed
1. Wrote an input-validation function that loops until the user provides a
   numeric weight (kg) and height (m) within a realistic range, handling
   non-numeric input and out-of-range values gracefully.
2. Implemented the BMI formula: `BMI = weight (kg) / height (m)^2`.
3. Classified the calculated BMI into WHO-standard categories:
   - Underweight: BMI < 18.5
   - Normal weight: 18.5 ≤ BMI < 25
   - Overweight: 25 ≤ BMI < 30
   - Obese: BMI ≥ 30
4. Displayed the weight, height, BMI value, and category in a clean
   formatted summary, along with the reference ranges.
5. Added a loop so the user can calculate BMI for multiple people without
   restarting the program.

## How to Run
```bash
python3 bmi_calculator.py
```
Follow the on-screen prompts to enter weight (kg) and height (m).

## Sample Output
```
Enter your weight in kilograms (e.g. 65.5): 70
Enter your height in meters (e.g. 1.75): 1.75

---------------------------------------------
Weight     : 70.0 kg
Height     : 1.75 m
Your BMI   : 22.86
Category   : Normal weight
---------------------------------------------
```

## Outcome
A fully functional, validated command-line BMI calculator that accurately
computes BMI and classifies it into the correct health category, with
graceful handling of invalid input.

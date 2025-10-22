def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters."""
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """Return interpretation based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Input from user
try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    if height <= 0 or weight <= 0:
        print("Height and weight must be positive values.")
    else:
        bmi = calculate_bmi(weight, height)
        category = interpret_bmi(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
except ValueError:
    print("Please enter valid numeric inputs.")

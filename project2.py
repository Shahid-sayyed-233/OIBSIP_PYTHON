def get_valid_input(prompt, min_value, max_value):
    """Prompt user until a valid float within range is entered."""
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"⚠️ Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

def calculate_bmi(weight, height):
    """Return BMI value."""
    return weight / (height ** 2)

def categorize_bmi(bmi):
    """Return BMI category based on ranges."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=== BMI Calculator ===")
    weight = get_valid_input("Enter your weight (kg): ", 10, 300)
    height = get_valid_input("Enter your height (m): ", 0.5, 2.5)

    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)

    print(f"\n✅ Your BMI is: {bmi:.2f}")
    print(f"📊 Category: {category}")

if __name__ == "__main__":
    main()
# BMI (Body Mass Index) Calculator Program

# Take weight input from user in kilograms
weight = float(input("Enter your weight (kg): "))   # Example: 70

# Take height in feet from user
height_feet = int(input("Enter your height (feet): "))  # Example: 5

# Take additional height in inches from user
height_inches = int(input("Enter your height (inches): "))  # Example: 8

# Convert height from feet and inches to meters
# 1 foot = 12 inches
# 1 inch = 2.54 cm
# Divide by 100 to convert cm into meters
height_m = ((height_feet * 12 + height_inches) * 2.54) / 100

# Calculate BMI using formula:
# BMI = Weight (kg) / Height² (m²)
bmi = weight / (height_m * height_m)

# Check BMI category

# If BMI is less than 18.5
if (bmi < 18.5):
    print("Category: Underweight")

# If BMI is between 18.5 and 24.9
elif (bmi < 25):
    print("Category: Normal")

# If BMI is between 25 and 29.9
elif (bmi < 30):
    print("Category: Overweight")

# If BMI is 30 or more
else:
    print("Category: Obese")

# BMI Calculator

# height in cm

height_in_cm = int(input("Enter height (cm): "))

# weight in kg

weight = int(input("Enter weight (kg) "))

# convert height to meter

height = height_in_cm / 100

# BMI Formula

BMI = weight  / (height ** 2)

print("Your BMI is", BMI)
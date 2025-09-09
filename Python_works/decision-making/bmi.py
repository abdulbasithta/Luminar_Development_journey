"""

Underweight
Normal weight
Overweight
Obese

BMI = weight_in_kg / (height_in_m ** 2)

"""

height_in_cm = int(input("Enter your height in cm: "))

weight_in_kg = int(input("Enter your weight in kg: "))

height = height_in_cm / 100

BMI = weight_in_kg / (height ** 2)

print("Your BMI is:", round(BMI, 2))

if BMI >= 30:

    print("You are obese.")

elif BMI >= 25:

    print("You are overweight.")

elif BMI >= 18.5:

    print("You have a normal weight.")

else:

    print("You are underweight.")
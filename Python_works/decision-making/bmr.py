
gender = input("Enter your gender:")

age = int(input("Enter your age:"))

height = int(input("Enter your height in cm:"))

weight = int(input("Enter your weight in kg:"))

activity_level = 1.2

"""
The basel matabolic rate (BMR) =
10 * weight (kg) + 6.25 * height (cm) - 5 * age (y) + 5 (male)
10 * weight (kg) + 6.25 * height (cm) - 5 * age (y) - 161 (female)

"""

if gender == "male":
    
    BMR = 10 * weight + 6.25 * height -5 * age + 5

else:

    BMR = 10 * weight + 6.25 * height -5 * age - 161

calories = BMR * activity_level

print("Calories = ",calories)
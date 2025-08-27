
# Logical Operator (and, or, not)

# read a number display True if last digit of number is > 5 and / by 2

num = int(input("Enter a number: "))

last_digit = num % 10

print(last_digit > 5 and num % 2 == 0)
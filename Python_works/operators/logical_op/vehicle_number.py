
# read vehicle number last 4 digit
# last digit even
# last digit > 5

num = int(input("Enter a 4 digit number: "))

last_digit = num % 10

print(last_digit > 5 and num % 2 == 0)

# number = 13784

# loop:
    #extract digit
    #chk digit is odd , if yes exit from loop
    #floor number

number = int(input("Enter a number:"))

while (number != 0):

    digit = number % 10

    if digit%2 != 0:

        print(number, "is largest odd number")

        break

    number = number // 10

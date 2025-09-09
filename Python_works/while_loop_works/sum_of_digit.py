
# sum of digits in a number

num = int(input("Enter a number: ")) #345

sum = 0

while(num != 0):

    digit = num % 10  

    sum = sum + digit

    num = num // 10

print("Sum of digits:", sum) #12
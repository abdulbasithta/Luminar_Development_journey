
"""
num = int(input("Enter a number: "))

original = num
sum = 0
digit_count = 0

while(num != 0):

    digit = num % 10

    digit_count = digit_count + 1

    num = num // 10

num = original

while(num != 0):

    digit = num % 10

    sum = sum + digit ** digit_count

    num = num // 10

print(sum)

"""

num = int(input("Enter a number: "))

digit_count = len(str(num))

sum = 0

original = num

# print(digit_count)

while(num != 0):

    digit = num % 10

    exponent = digit ** digit_count

    sum = sum + exponent

    num = num // 10

if original == sum:

    print(original, "is amstrong")

else:

    print(original, "is not amstrong")
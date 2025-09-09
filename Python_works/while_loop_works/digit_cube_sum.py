
num = int(input("Enter a number: ")) # 132

sum = 0

while(num != 0):

    digit = num % 10 #2

    cube = digit ** 3 # 2^3

    sum = sum + cube

    num = num // 10

print(sum)
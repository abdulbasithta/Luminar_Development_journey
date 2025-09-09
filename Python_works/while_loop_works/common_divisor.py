
#common divisors

num1 =int(input("Enter first number: ")) #12

num2 =int(input("Enter second number: ")) #24

i =1

minimum =min(num1, num2)

while(i<= minimum): #1<= 12

    if num1% i ==0 and num2% i ==0:

        print(i)

    i+=1
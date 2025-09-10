
#read a number
#display all divisor of the number

num = int(input("Enter a number: ")) #12

for i in range(1,num+1): #num+1 means include the number

    if num % i ==0:

        print(i)



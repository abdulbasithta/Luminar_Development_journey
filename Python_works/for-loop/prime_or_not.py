
"""
read number
set is_prime as true

loop 2 to number-1
    set is_prime as false is divisor of number and break
 
"""

number = int(input("Enter number ")) #17

is_prime = True

for i in range(2,number):

    if number % i ==0:

        is_prime = False
        
        break
print(is_prime)



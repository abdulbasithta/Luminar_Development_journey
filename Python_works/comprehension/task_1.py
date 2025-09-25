
arr=[3,4,5,6,7,8,9,10]

# create a new list that contain cube of all number

cube=[num**3 for num in arr]

# create a new list if contain only even numbers

even_num=[num for num in arr if num%2 ==0]

print(even_num)

# create a new list of odd numbers

odd_num=[num for num in arr if num%2 !=0]

print(odd_num)
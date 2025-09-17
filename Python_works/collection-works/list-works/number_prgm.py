"""
numbers=[10,11,14,3,8,19,20,21,22,23,56]

q1)display all even numbers
q2)display all odd numbers
q3)display_sum of all even numbers
q4)display largest number
q5)display smallest number

"""
numbers = [10,11,14,3,8,19,20,21,22,23,56]

even_numbers =[]

even_sum = 0

largest = numbers[0]

smallest = numbers[0]

for num in numbers:

    if num % 2 == 0:

        even_numbers = num

        print("even numbers", num)

    if num % 2 != 0:
        print("odd numbers", num)

    if num % 2 == 0:

        even_sum += num

    if num > largest:

        largest = num

    if num < smallest:

        smallest = num

print("sum of even numbers", even_sum)
print("largest number", largest)
print("smallest number", smallest)

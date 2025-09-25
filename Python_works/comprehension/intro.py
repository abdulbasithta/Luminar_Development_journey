"""
list comprehension => easy way to create a list from iterable

syntax:

squares=[return_value iteration condition]

"""

arr=[10,20,30,40,50,10,30]

squares=[num**2 for num in arr]

print(squares)

cubes=[num**3 for num in arr]

print(cubes)

num_gt_25=[num for num in arr if num> 25]

print(num_gt_25)

num_add_5=[num+5 for num in arr]

print(num_add_5)
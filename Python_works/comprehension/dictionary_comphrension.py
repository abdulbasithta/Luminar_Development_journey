"""
dictionary comprehension => easy way of creating dictionay iterable

syntax:

variable_name={key:value iteration condition}
"""

arr=[10,11,12,13,14,15]
#     0  1  2  3  4  5
# op = {10:10^0,11:11^1,12:12^2,...}

# {10:100,11:121,...}

square_dic={num:num**2 for num in arr}

print(square_dic)

cube_dic={num:num**3 for num in arr}

print(cube_dic)

for index,value in enumerate(arr):

    print(index,value)

output={value:value**index for index,value in enumerate(arr)}

print(output)
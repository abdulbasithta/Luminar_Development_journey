# Count how many times a specific element appears in a list.
#  Example:
#  Input: [1,2,3,2,2,4], element=2 Output: 3

numbers=[1,2,3,2,2,4]

element =2

count =0

for num in numbers:

    if num == element:

        count+=1

# print(count)

#  Reverse a list without using the built-in reverse method.
#  Example:
#  Input: [1,2,3,4] Output: [4,3,2,1]

rev_numbers=[1,2,3,4]

rev_list =[]

for i in range(len(rev_numbers)-1,-1,-1):  # range(start, stop, step)

    rev_list.append(rev_numbers[i])

# print(rev_list)

#  Remove all duplicates from a list.
#  Example:
#  Input: [1,2,2,3,4,4,5] Output: [1,2,3,4,5]

dup_numbers=[1,2,2,3,4,5,4,5]

unique_num=[]

for num in dup_numbers:

    if num not in unique_num:

        unique_num.append(num)

# print(unique_num)

#  Check if a given element exists in a list.
#  Example:
#  Input: [1,2,3,4], element=3 Output: Yes

chk_numbers=[1,2,3,4,5]

element =3

if element in chk_numbers:

    print("Yes")

else:

    print("No")
#  Find the sum and average of elements in a list.
#  Example:
#  Input: [2,4,6,8] Output: Sum=20, Avg=5.0

numbers=[2,4,6,8]

sum =0

for num in numbers:

    sum += num

    avg = sum / len(numbers)

print("Sum =", sum, ",", "Avg =", avg)

# Sort a list in ascending and descending order.
# Example:
# Input: [3,1,4,2] Output Asc=[1,2,3,4], Desc=[4,3,2,1]

sorting_numbers=[3,1,4,2]

asc =sorting_numbers[:]

for i in range(len(asc)):

    for j in range(len(asc)-1):

        if asc[j] > asc[j+1]:

            asc[j], asc[j+1] = asc[j+1], asc[j]  # swap
            
desc = asc[::-1]

print("Asc =", asc, ",", "Desc =", desc)

#  Merge two lists into one.
#  Example:
#  Input: [1,2,3], [4,5,6] Output: [1,2,3,4,5,6]

list1=[1,2,3]
list2=[4,5,6]

merged=[]

for num in list1:

    merged.append(num)

for num in list2:

    merged.append(num)

print("Merged List:", merged)

# Print the second largest element in a list.
#  Example:
#  Input: [10, 20, 4, 8] Output: 10

s_numbers=[10,20,4,8]

s_numbers.sort(reverse=True) # desc

second_largest = s_numbers[1]

print("Second Largest:", second_largest)
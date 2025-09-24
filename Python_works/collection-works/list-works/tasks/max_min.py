#  Find the maximum and minimum number from a list.
#  Input: [10, 20, 5, 8] Output: Max=20, Min=5

numbers=[10,20,5,8]

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:

    if num > max_num:

        max_num = num

    if num < min_num:

        min_num = num

print("Max =", max_num, ",", "Min =", min_num)
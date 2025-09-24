
arr =[1,3,4,5,6,2]

# find least +ve missing number

arr.sort()

# [1,2,3,4,5,6]
#  0 1 2 3 4 5
#  c n
#          c n


for current in range(0,len(arr)-1):

    next =current+1

    difference = arr[next] - arr[current]

    if difference != 1:

        print(arr[current]+1,"is missing")

        break

if arr[next] == arr[-1]: # 6 == 6

    print(arr[-1]+1, "is missing") # 7 is missing




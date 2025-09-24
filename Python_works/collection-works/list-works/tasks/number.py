# Create a list of 5 numbers entered by the user.
# Input: 1 2 3 4 5 Output: [1, 2, 3, 4, 5]

def create_list():

    numbers=[]

    for i in range(5):

        num=int(input("Enter a number: "))

        numbers.append(num)

    return numbers

print(create_list())


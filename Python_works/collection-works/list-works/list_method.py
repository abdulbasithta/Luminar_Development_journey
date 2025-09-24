
"""
class list:

    def append(self,object): # appends object to end of list object
    def insert(self,index,object) # insert object at specific index of list object
    def pop(self,index=-1) remove and return item at specific index
    def index(self,object) return first index of value(object) (first occurence of index)
    def count(self,object) return number of occurence of object
    def reverse(self) reverse the current list of objrct
    def copy() return copy of the list
    def sort(self,reverse=False) Sort the list in ascending or decending order and return None.
    def extend(self,iterable) Extend list by appending elements from the iterable.
    def remove(self,object) Remove first occurrence of value. Raises ValueError if the value is not present.

"""

colors=["red","green","blue","red","green","blue"]
#         0      1       2     3      4       5

# colors.append("black")

# print(colors)

# colors.insert(1,"yellow")

# print(colors)

# colors.pop(0)

# print(colors)

# pos=colors.index("blue")

# print(pos)

# frequency =colors.count("red")

# print(frequency)

# colors.reverse()

# print(colors)

# colors_copy = colors.copy()

# print(colors_copy)

# colors.sort(reverse=False) # Ase
# colors.sort(reverse=True) # Dse

# print(colors)

# expences =[10000,12000,11000,15000,13000,14000]
# expences.sort(reverse=False)
# print(expences)

# arr1=[10,20,30,40]

# arr2=[100,200,300,400]

# arr2.extend(arr1)

# print(arr2)

colors.remove("red")

print(colors)